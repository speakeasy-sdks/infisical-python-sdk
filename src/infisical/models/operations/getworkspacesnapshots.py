from __future__ import annotations
import dataclasses
import requests
from ..shared import errorresponse as shared_errorresponse
from typing import Any, Optional


@dataclasses.dataclass
class GetWorkspaceSnapshotsPathParams:
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetWorkspaceSnapshotsRequest:
    path_params: GetWorkspaceSnapshotsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetWorkspaceSnapshotsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    snapshots: Optional[list[Any]] = dataclasses.field(default=None)
    