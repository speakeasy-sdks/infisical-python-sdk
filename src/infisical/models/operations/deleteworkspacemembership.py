from __future__ import annotations
import dataclasses
import requests
from ..shared import errorresponse as shared_errorresponse
from ..shared import membership as shared_membership
from typing import Optional


@dataclasses.dataclass
class DeleteWorkspaceMembershipPathParams:
    membership_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'membershipId', 'style': 'simple', 'explode': False }})
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteWorkspaceMembershipRequest:
    path_params: DeleteWorkspaceMembershipPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteWorkspaceMembershipResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    membership: Optional[shared_membership.Membership] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    