from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import user as shared_user
from typing import Optional


@dataclasses.dataclass
class MyUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    user: Optional[shared_user.User] = dataclasses.field(default=None)
    