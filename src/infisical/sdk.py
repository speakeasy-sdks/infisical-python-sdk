__doc__ = """ SDK Documentation: The Infisical REST API provides users an alternative way to programmatically access and manage secrets via HTTPS requests. This can be useful for automating tasks, such as rotating credentials, or for integrating secret management into a larger system.
https://infisical.com/docs/api-reference/overview/introduction - Infisical API documentation"""
import requests as requests_http
from . import utils
from .key import Key
from .log import Log
from .membership import Membership
from .organization import Organization
from .secret import Secret
from .snapshot import Snapshot
from .user import User
from .workspace import Workspace
from infisical.models import shared

SERVERS = [
	"https://app.infisical.com/api/v2",
]

class Infisical:
    r"""SDK Documentation: The Infisical REST API provides users an alternative way to programmatically access and manage secrets via HTTPS requests. This can be useful for automating tasks, such as rotating credentials, or for integrating secret management into a larger system.
    https://infisical.com/docs/api-reference/overview/introduction - Infisical API documentation"""
    key: Key
    log: Log
    membership: Membership
    organization: Organization
    secret: Secret
    snapshot: Snapshot
    user: User
    workspace: Workspace
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.6.0"
    _gen_version: str = "1.11.0"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.key = Key(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.log = Log(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.membership = Membership(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.organization = Organization(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.secret = Secret(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.snapshot = Snapshot(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user = User(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.workspace = Workspace(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    