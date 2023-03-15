from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import secret as shared_secret
from dataclasses_json import Undefined, dataclass_json
from infisical import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateSecretsRequestBody:
    secrets: Optional[list[shared_secret.Secret]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secrets'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateSecretsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    secrets: Optional[list[shared_secret.Secret]] = dataclasses.field(default=None)
    