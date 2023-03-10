<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/221301610-ba56dcf5-5eaa-459c-b0c4-d03d805ac896.svg">
    <p><strong>Open Source SecretOps</strong></p>
   <p>The Open Source, end-to-end, easy to use tool that lets you securely sync secrets and configs across your team, devices, and infrastructure</p>
   <a href="https://infisical.com/docs/api-reference/overview/introduction"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=bada5b&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/infisical-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/infisical-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://join.slack.com/t/infisical-users/shared_invite/zt-1kdbk07ro-RtoyEt_9E~fyzGo_xQYP6g"><img src="https://img.shields.io/static/v1?label=Slack&message=Join&color=7289da&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
</div>

<!-- Start SDK 
Installation -->
## SDK Installation

```bash
pip install infisical
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import infisical
from infisical.models import operations, shared

s = infisical.Infisical()
s.config_security(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    )
)
   
req = operations.GetWorkspaceKeysRequest(
    path_params=operations.GetWorkspaceKeysPathParams(
        workspace_id="unde",
    ),
)
    
res = s.key.get_workspace_keys(req)

if res.keys is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### key

* `get_workspace_keys` - Get workspace encrypted key

### log

* `get_workspace_logs` - Get workspace logs

### membership

* `delete_organization_membership` - Delete organization membership
* `delete_workspace_membership` - Delete workspace membership
* `get_organization_memberships` - Get organization memberships
* `get_workspace_memberships` - Get workspace memberships
* `update_organization_membership` - Update organization membership
* `update_workspace_membership` - Update workspace membership

### organization

* `delete_organization_membership` - Delete organization membership
* `get_organization_memberships` - Get organization memberships
* `get_organization_workspaces` - Get organization workspaces
* `update_organization_membership` - Update organization membership

### secret

* `create_secret` - Create secret
* `delete_secrets` - Delete secrets
* `get_secret_versions` - Get secret versions
* `get_secrets` - Get secrets
* `rollback_secret_versions` - Rollback secret versions
* `update_secrets` - Update secrets

### snapshot

* `get_workspace_snapshots` - Get workspace snapshots
* `rollback_snapshots` - Rollback workspace secret snapshots

### user

* `my_organizations` - Get current user organizations
* `my_user` - Get current user

### workspace

* `delete_workspace_membership` - Delete workspace membership
* `get_organization_workspaces` - Get organization workspaces
* `get_workspace_keys` - Get workspace encrypted key
* `get_workspace_logs` - Get workspace logs
* `get_workspace_memberships` - Get workspace memberships
* `get_workspace_snapshots` - Get workspace snapshots
* `rollback_snapshots` - Rollback workspace secret snapshots
* `update_workspace_membership` - Update workspace membership
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
