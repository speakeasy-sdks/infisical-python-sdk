from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import secret as shared_secret
from typing import Optional


@dataclasses.dataclass
class RollbackSnapshotsRequest:
    request_body: int = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RollbackSnapshotsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    secrets: Optional[list[shared_secret.Secret]] = dataclasses.field(default=None)
    