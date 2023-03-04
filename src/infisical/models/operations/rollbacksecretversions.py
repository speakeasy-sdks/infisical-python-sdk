from __future__ import annotations
import dataclasses
import requests
from ..shared import errorresponse as shared_errorresponse
from ..shared import secret as shared_secret
from typing import Optional


@dataclasses.dataclass
class RollbackSecretVersionsPathParams:
    secret_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'secretId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RollbackSecretVersionsRequest:
    path_params: RollbackSecretVersionsPathParams = dataclasses.field()
    request: int = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class RollbackSecretVersionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    secret: Optional[shared_secret.Secret] = dataclasses.field(default=None)
    