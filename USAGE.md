<!-- Start SDK Example Usage -->
```python
import infisical
from infisical.models import operations, shared

s = infisical.Infisical()
s.config_security(
    security=shared.Security(
        bearer_auth=shared.SchemeBearerAuth(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
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