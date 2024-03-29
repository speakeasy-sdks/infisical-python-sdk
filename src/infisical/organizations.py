"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from infisical.models import operations, shared
from typing import Optional

class Organizations:
    r"""Everything about organizations"""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def delete_membership(self, request: operations.DeleteOrgMembershipsRequest) -> operations.DeleteOrgMembershipsResponse:
        r"""Delete organization membership
        Delete organization membership
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteOrgMembershipsRequest, base_url, '/organizations/{organizationId}/memberships/{membershipId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Membership])
                res.membership = out
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def list_membership(self, request: operations.ListOrgMembershipsRequest) -> operations.ListOrgMembershipsResponse:
        r"""List organization memberships
        List organization memberships
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListOrgMembershipsRequest, base_url, '/organizations/{organizationId}/memberships', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListOrgMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.Membership]])
                res.memberships = out
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def update_membership(self, request: operations.UpdateOrgMembershipsRequest) -> operations.UpdateOrgMembershipsResponse:
        r"""Update organization membership
        Update organization membership
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateOrgMembershipsRequest, base_url, '/organizations/{organizationId}/memberships/{membershipId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "membership", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateOrgMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Membership])
                res.membership = out
        elif http_res.status_code in [401, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    