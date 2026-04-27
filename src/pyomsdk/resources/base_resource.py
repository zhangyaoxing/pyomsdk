from typing import Any, Optional
from httpx import Client
from pydantic import BaseModel


class BaseResource:
    def __init__(self, client: Client) -> None:
        self._client = client

    def _param_to_dict(self, params):
        if params is None:
            return None
        if isinstance(params, dict):
            return params
        if hasattr(params, "model_dump"):
            return params.model_dump(by_alias=True, exclude_none=True)
        if isinstance(params, list):
            return [self._param_to_dict(param) for param in params]
        raise ValueError(f"Unsupported parameter type: {type(params)}")

    def _build_path(self, path_template: str, path_params: Optional[dict[str, Any]]) -> str:
        if not path_params:
            return path_template
        for key, value in path_params.items():
            placeholder = f"{{{key}}}"
            if placeholder in path_template:
                path_template = path_template.replace(placeholder, str(value))
        return path_template

    def _request(
        self,
        method: str,
        path_template: str,
        path_params: Optional[BaseModel],
        query_params: Optional[BaseModel],
        body_params: Optional[BaseModel | list],
    ) -> Any:
        path = self._build_path(path_template, self._param_to_dict(path_params))
        query = self._param_to_dict(query_params)
        body = self._param_to_dict(body_params)
        if body is None and method in ("POST", "PUT", "PATCH"):
            body = {}
        response = self._client.request(method=method, url=path, params=query, json=body)
        if not response.content:
            return None
        return response.json()
