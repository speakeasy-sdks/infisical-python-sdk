"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import secretversion as shared_secretversion
from typing import Optional


@dataclasses.dataclass
class ListVersionsRequest:
    
    secret_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'secretId', 'style': 'simple', 'explode': False }})
    r"""Secret ID"""  
    limit: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Limit"""  
    offset: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Offset"""  
    

@dataclasses.dataclass
class ListVersionsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""Unauthorized"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    secret_versions: Optional[list[shared_secretversion.SecretVersion]] = dataclasses.field(default=None)
    r"""OK"""  
    