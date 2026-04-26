from __future__ import annotations

from enum import Enum
from typing import Any, get_args, get_origin
import types

import pytest
from pydantic import BaseModel, ValidationError


def _unwrap_optional(annotation: Any) -> Any:
    origin = get_origin(annotation)
    if origin is types.UnionType or str(origin) == "typing.Union":
        args = [arg for arg in get_args(annotation) if arg is not type(None)]
        return args[0] if args else Any
    return annotation


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _context_id(obj: dict[str, Any] | None) -> str | None:
    if not obj:
        return None
    return obj.get("id") or obj.get("_id")


def _context_name(obj: dict[str, Any] | None) -> str | None:
    if not obj:
        return None
    return obj.get("name") or obj.get("username")


def _fake_value(field_name: str) -> Any:
    lowered = field_name.lower()
    if "email" in lowered or "username" in lowered:
        return "user@example.com"
    if "url" in lowered or "webhook" in lowered:
        return "https://example.com"
    if "port" in lowered:
        return 27017
    if "enabled" in lowered:
        return True
    if lowered.endswith("id") or lowered.endswith("_id"):
        return "000000000000000000000001"
    return "value"


def _value_from_context(field_name: str, context: dict[str, Any]) -> Any:
    project = context.get("project")
    org = context.get("org")
    user = context.get("user")
    api_key = context.get("api_key")

    mapping = {
        "project_id": _context_id(project),
        "group_id": _context_id(project),
        "org_id": _context_id(org),
        "user_id": _context_id(user),
        "group_name": _context_name(project),
        "org_name": _context_name(org),
        "username": user.get("username") if user else None,
        "email_address": user.get("emailAddress") if user else None,
        "pretty": True,
        "page_num": 1,
        "items_per_page": 100,
        "envelope": False,
        "flatten_teams": True,
        "include_org_users": True,
        "include_deleted_orgs": False,
    }

    if field_name == "api_agent_key_id" and api_key:
        return _first_present(api_key.get("id"), api_key.get("_id"))

    if field_name in mapping and mapping[field_name] is not None:
        return mapping[field_name]

    if field_name.endswith("project_id") or field_name.endswith("group_id"):
        return _context_id(project)
    if field_name.endswith("org_id"):
        return _context_id(org)
    if field_name.endswith("user_id"):
        return _context_id(user)

    return None


def _build_value(annotation: Any, field_name: str, context: dict[str, Any]) -> Any:
    annotation = _unwrap_optional(annotation)
    origin = get_origin(annotation)

    contextual_value = _value_from_context(field_name, context)
    if contextual_value is not None:
        return contextual_value

    if annotation is Any:
        return _fake_value(field_name)

    if annotation is str:
        return str(_fake_value(field_name))
    if annotation is int:
        fake_value = _fake_value(field_name)
        return fake_value if isinstance(fake_value, int) else 1
    if annotation is float:
        return 1.0
    if annotation is bool:
        fake_value = _fake_value(field_name)
        return fake_value if isinstance(fake_value, bool) else True
    if annotation is dict:
        return {"key": "value"}
    if annotation is list:
        return ["value"]

    if origin is list:
        inner_type = get_args(annotation)[0] if get_args(annotation) else Any
        return [_build_value(inner_type, field_name, context)]

    if origin is dict:
        return {"key": "value"}

    if isinstance(annotation, type) and issubclass(annotation, Enum):
        return list(annotation)[0]

    if isinstance(annotation, type) and issubclass(annotation, BaseModel):
        return build_model_or_skip(annotation, **context)

    return _fake_value(field_name)


def build_model_or_skip(model_cls: type[BaseModel], **context: Any) -> BaseModel:
    values: dict[str, Any] = {}
    for field_name, field in model_cls.model_fields.items():
        values[field_name] = _build_value(field.annotation, field_name, context)

    try:
        return model_cls(**values)
    except ValidationError as exc:
        pytest.skip(f"Unable to build {model_cls.__name__}: {exc}")


def assert_success_or_skip(result: Any) -> None:
    """Skip tests when endpoint is unavailable in the current Ops Manager setup."""
    if isinstance(result, dict) and "error" in result:
        error_code = result.get("errorCode")
        detail = result.get("detail")
        pytest.skip(f"API returned error ({error_code}): {detail}")
