<!-- Start SDK Example Usage -->
```python
import infisical
from infisical.models import operations, shared

s = infisical.Infisical(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DeleteOrgMembershipsRequest(
    membership_id="corrupti",
    organization_id="provident",
)
    
res = s.organizations.delete_membership(req)

if res.membership is not None:
    # handle response
```
<!-- End SDK Example Usage -->