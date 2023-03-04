from __future__ import annotations
import dataclasses
import requests
from ..shared import errorresponse as shared_errorresponse
from ..shared import key as shared_key
from typing import Optional


@dataclasses.dataclass
class GetWorkspaceKeysPathParams:
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetWorkspaceKeysRequest:
    path_params: GetWorkspaceKeysPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetWorkspaceKeysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    keys: Optional[list[shared_key.Key]] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    