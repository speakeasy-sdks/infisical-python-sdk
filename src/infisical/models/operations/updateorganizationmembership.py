from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import membership as shared_membership
from typing import Optional


@dataclasses.dataclass
class UpdateOrganizationMembershipPathParams:
    membership_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'membershipId', 'style': 'simple', 'explode': False }})
    organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateOrganizationMembershipRequest:
    path_params: UpdateOrganizationMembershipPathParams = dataclasses.field()
    request: shared_membership.Membership = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateOrganizationMembershipResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    membership: Optional[shared_membership.Membership] = dataclasses.field(default=None)
    