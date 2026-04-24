import importlib
import inspect
import pkgutil
from types import UnionType
from typing import Any, get_args, get_origin

from pydantic import BaseModel

from ops_manager_sdk.ops_manager_client import OpsManagerClient
from ops_manager_sdk.resources import __path__ as resources_pkg_path
from ops_manager_sdk.resources.base_resource import BaseResource
from pyomsdk.tests.shared import get_client


class _FakeResponse:
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code
        self.content = b"{}"

    def json(self) -> dict[str, Any]:
        return {}


def _list_resource_classes() -> list[type[BaseResource]]:
    classes: list[type[BaseResource]] = []
    for module_info in pkgutil.iter_modules(resources_pkg_path):
        if module_info.name in {"__init__", "base_resource"}:
            continue
        module = importlib.import_module(f"ops_manager_sdk.resources.{module_info.name}")
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj is BaseResource:
                continue
            if issubclass(obj, BaseResource) and obj.__module__ == module.__name__:
                classes.append(obj)
    return classes


def _public_api_methods(resource_cls: type[BaseResource]) -> list[str]:
    methods = []
    for method_name, method in inspect.getmembers(resource_cls, inspect.isfunction):
        if method_name.startswith("_"):
            continue
        if method.__qualname__.split(".", 1)[0] != resource_cls.__name__:
            continue
        methods.append(method_name)
    return methods


def _build_model(model_cls: type[BaseModel], depth: int = 0) -> BaseModel:
    if depth > 5:
        return model_cls.model_construct()

    payload: dict[str, Any] = {}
    for field_name, field in model_cls.model_fields.items():
        payload[field_name] = _build_value(field.annotation, field_name, depth + 1)
    return model_cls.model_construct(**payload)


def _build_value(annotation: Any, name: str, depth: int = 0) -> Any:
    if depth > 6:
        return None

    if annotation is inspect._empty:
        return _fallback_value(name)

    if annotation is Any:
        return _fallback_value(name)

    origin = get_origin(annotation)
    if origin in (list,):
        args = get_args(annotation)
        item_type = args[0] if args else Any
        return [_build_value(item_type, f"{name}_item", depth + 1)]

    if origin in (dict,):
        return {}

    if origin in (tuple,):
        return ()

    if origin in (UnionType,):
        non_none_types = [arg for arg in get_args(annotation) if arg is not type(None)]
        if not non_none_types:
            return None
        return _build_value(non_none_types[0], name, depth + 1)

    if str(origin) == "typing.Union":
        non_none_types = [arg for arg in get_args(annotation) if arg is not type(None)]
        if not non_none_types:
            return None
        return _build_value(non_none_types[0], name, depth + 1)

    if str(origin) == "typing.Literal":
        literal_args = get_args(annotation)
        return literal_args[0] if literal_args else _fallback_value(name)

    if inspect.isclass(annotation):
        if issubclass(annotation, BaseModel):
            return _build_model(annotation, depth + 1)
        if issubclass(annotation, bool):
            return True
        if issubclass(annotation, int):
            return 1
        if issubclass(annotation, float):
            return 1.0
        if issubclass(annotation, str):
            return _fallback_value(name)

    return _fallback_value(name)


def _fallback_value(name: str) -> Any:
    key_name = name.lower()
    if "id" in key_name:
        return "698117018b47f47002806d04"
    if "name" in key_name:
        return "test-name"
    if "port" in key_name:
        return 27017
    if "enabled" in key_name:
        return True
    return "test"


def _build_call_kwargs(method: Any) -> dict[str, Any]:
    kwargs: dict[str, Any] = {}
    signature = inspect.signature(method)
    for parameter in signature.parameters.values():
        if parameter.name == "self":
            continue

        if parameter.default is not inspect._empty:
            kwargs[parameter.name] = parameter.default
            continue

        kwargs[parameter.name] = _build_value(parameter.annotation, parameter.name)
    return kwargs


def test_all_resources_public_methods_http_code_200(monkeypatch) -> None:
    client = get_client()

    status_codes: list[int] = []

    def fake_request(method: str, url: str, params: Any = None, json: Any = None) -> _FakeResponse:
        status_codes.append(200)
        return _FakeResponse(200)

    monkeypatch.setattr(client._client, "request", fake_request)

    client_resources: dict[type[BaseResource], str] = {}
    for property_name, prop in inspect.getmembers(
        OpsManagerClient, lambda item: isinstance(item, property)
    ):
        if not property_name.endswith("_resource"):
            continue
        resource = getattr(client, property_name)
        client_resources[type(resource)] = property_name

    failures: list[str] = []
    for resource_cls in _list_resource_classes():
        resource_name = client_resources.get(resource_cls)
        if resource_name is None:
            failures.append(f"resource class not exposed on client: {resource_cls.__name__}")
            continue

        resource = getattr(client, resource_name)
        methods = _public_api_methods(resource_cls)
        if not methods:
            failures.append(f"resource has no public methods: {resource_cls.__name__}")
            continue

        for method_name in methods:
            bound_method = getattr(resource, method_name)
            kwargs = _build_call_kwargs(bound_method)
            previous_call_count = len(status_codes)
            try:
                bound_method(**kwargs)
            except Exception as exc:  # pylint: disable=broad-except
                failures.append(f"{resource_cls.__name__}.{method_name} raised {exc}")
                continue

            if len(status_codes) != previous_call_count + 1:
                failures.append(
                    f"{resource_cls.__name__}.{method_name} did not issue request exactly once"
                )
                continue

            if status_codes[-1] != 200:
                failures.append(
                    f"{resource_cls.__name__}.{method_name} returned status {status_codes[-1]}"
                )

    assert not failures, "\n".join(failures)
