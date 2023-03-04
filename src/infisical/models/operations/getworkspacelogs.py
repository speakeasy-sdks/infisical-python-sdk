from __future__ import annotations
import dataclasses
import requests
from ..shared import errorresponse as shared_errorresponse
from ..shared import log as shared_log
from typing import Optional


@dataclasses.dataclass
class GetWorkspaceLogsPathParams:
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetWorkspaceLogsRequest:
    path_params: GetWorkspaceLogsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetWorkspaceLogsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    logs: Optional[list[shared_log.Log]] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    