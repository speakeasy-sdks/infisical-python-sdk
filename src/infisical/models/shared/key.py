from __future__ import annotations
import dataclasses
from ..shared import sender as shared_sender
from dataclasses_json import Undefined, dataclass_json
from infisical import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Key:
    encryptedkey: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('encryptedkey'), 'exclude': lambda f: f is None }})
    nonce: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nonce'), 'exclude': lambda f: f is None }})
    receiver: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('receiver'), 'exclude': lambda f: f is None }})
    sender: Optional[shared_sender.Sender] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sender'), 'exclude': lambda f: f is None }})
    workspace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('workspace'), 'exclude': lambda f: f is None }})
    