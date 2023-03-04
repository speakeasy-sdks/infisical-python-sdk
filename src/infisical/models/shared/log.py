from __future__ import annotations
import dataclasses
from ..shared import action as shared_action
from dataclasses_json import Undefined, dataclass_json
from infisical import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Log:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id'), 'exclude': lambda f: f is None }})
    action_names: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actionNames'), 'exclude': lambda f: f is None }})
    actions: Optional[list[shared_action.Action]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions'), 'exclude': lambda f: f is None }})
    channel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel'), 'exclude': lambda f: f is None }})
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    ip_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ipAddress'), 'exclude': lambda f: f is None }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'exclude': lambda f: f is None }})
    user: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    workspace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace'), 'exclude': lambda f: f is None }})
    