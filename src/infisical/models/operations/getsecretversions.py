from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import secretversion as shared_secretversion
from typing import Optional


@dataclasses.dataclass
class GetSecretVersionsPathParams:
    secret_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'secretId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSecretVersionsQueryParams:
    limit: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetSecretVersionsRequest:
    path_params: GetSecretVersionsPathParams = dataclasses.field()
    query_params: GetSecretVersionsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSecretVersionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    secret_versions: Optional[list[shared_secretversion.SecretVersion]] = dataclasses.field(default=None)
    