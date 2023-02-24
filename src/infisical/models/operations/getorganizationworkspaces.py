from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import workspace as shared_workspace
from typing import Optional


@dataclasses.dataclass
class GetOrganizationWorkspacesPathParams:
    organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetOrganizationWorkspacesRequest:
    path_params: GetOrganizationWorkspacesPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetOrganizationWorkspacesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    workspaces: Optional[list[shared_workspace.Workspace]] = dataclasses.field(default=None)
    