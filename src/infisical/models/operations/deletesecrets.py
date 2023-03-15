from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import secret as shared_secret
from typing import Optional


@dataclasses.dataclass
class DeleteSecretsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    secrets: Optional[list[shared_secret.Secret]] = dataclasses.field(default=None)
    