"""
    Ansible Events API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""
import re  # noqa: F401
import sys  # noqa: F401

from ansible_events_api.api_client import ApiClient
from ansible_events_api.api_client import Endpoint as _Endpoint
from ansible_events_api.model.body_reset_forgot_password_api_auth_forgot_password_post import (
    BodyResetForgotPasswordApiAuthForgotPasswordPost,
)
from ansible_events_api.model.body_reset_reset_password_api_auth_reset_password_post import (
    BodyResetResetPasswordApiAuthResetPasswordPost,
)
from ansible_events_api.model.body_verify_request_token_api_auth_request_verify_token_post import (
    BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost,
)
from ansible_events_api.model.body_verify_verify_api_auth_verify_post import (
    BodyVerifyVerifyApiAuthVerifyPost,
)
from ansible_events_api.model.error_model import ErrorModel
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.user_create import UserCreate
from ansible_events_api.model.user_read import UserRead
from ansible_events_api.model_utils import check_allowed_values
from ansible_events_api.model_utils import check_validations
from ansible_events_api.model_utils import date
from ansible_events_api.model_utils import datetime
from ansible_events_api.model_utils import file_type
from ansible_events_api.model_utils import none_type
from ansible_events_api.model_utils import validate_and_convert_types


class AuthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.auth_jwt_login_api_auth_jwt_login_post_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": [],
                "endpoint_path": "/api/auth/jwt/login",
                "operation_id": "auth_jwt_login_api_auth_jwt_login_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "username",
                    "password",
                    "grant_type",
                    "scope",
                    "client_id",
                    "client_secret",
                ],
                "required": [
                    "username",
                    "password",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "grant_type",
                ],
            },
            root_map={
                "validations": {
                    ("grant_type",): {
                        "regex": {
                            "pattern": r"password",  # noqa: E501
                        },
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "username": (str,),
                    "password": (str,),
                    "grant_type": (str,),
                    "scope": (str,),
                    "client_id": (str,),
                    "client_secret": (str,),
                },
                "attribute_map": {
                    "username": "username",
                    "password": "password",
                    "grant_type": "grant_type",
                    "scope": "scope",
                    "client_id": "client_id",
                    "client_secret": "client_secret",
                },
                "location_map": {
                    "username": "form",
                    "password": "form",
                    "grant_type": "form",
                    "scope": "form",
                    "client_id": "form",
                    "client_secret": "form",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/x-www-form-urlencoded"],
            },
            api_client=api_client,
        )
        self.auth_jwt_logout_api_auth_jwt_logout_post_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": ["APIKeyCookie"],
                "endpoint_path": "/api/auth/jwt/logout",
                "operation_id": "auth_jwt_logout_api_auth_jwt_logout_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={"all": [], "required": [], "nullable": [], "enum": [], "validation": []},
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.register_register_api_auth_register_post_endpoint = _Endpoint(
            settings={
                "response_type": (UserRead,),
                "auth": [],
                "endpoint_path": "/api/auth/register",
                "operation_id": "register_register_api_auth_register_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "user_create",
                ],
                "required": [
                    "user_create",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user_create": (UserCreate,),
                },
                "attribute_map": {},
                "location_map": {
                    "user_create": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )
        self.reset_forgot_password_api_auth_forgot_password_post_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": [],
                "endpoint_path": "/api/auth/forgot-password",
                "operation_id": "reset_forgot_password_api_auth_forgot_password_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body_reset_forgot_password_api_auth_forgot_password_post",
                ],
                "required": [
                    "body_reset_forgot_password_api_auth_forgot_password_post",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body_reset_forgot_password_api_auth_forgot_password_post": (
                        BodyResetForgotPasswordApiAuthForgotPasswordPost,
                    ),
                },
                "attribute_map": {},
                "location_map": {
                    "body_reset_forgot_password_api_auth_forgot_password_post": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )
        self.reset_reset_password_api_auth_reset_password_post_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": [],
                "endpoint_path": "/api/auth/reset-password",
                "operation_id": "reset_reset_password_api_auth_reset_password_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body_reset_reset_password_api_auth_reset_password_post",
                ],
                "required": [
                    "body_reset_reset_password_api_auth_reset_password_post",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body_reset_reset_password_api_auth_reset_password_post": (
                        BodyResetResetPasswordApiAuthResetPasswordPost,
                    ),
                },
                "attribute_map": {},
                "location_map": {
                    "body_reset_reset_password_api_auth_reset_password_post": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )
        self.verify_request_token_api_auth_request_verify_token_post_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": [],
                "endpoint_path": "/api/auth/request-verify-token",
                "operation_id": "verify_request_token_api_auth_request_verify_token_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body_verify_request_token_api_auth_request_verify_token_post",
                ],
                "required": [
                    "body_verify_request_token_api_auth_request_verify_token_post",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body_verify_request_token_api_auth_request_verify_token_post": (
                        BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost,
                    ),
                },
                "attribute_map": {},
                "location_map": {
                    "body_verify_request_token_api_auth_request_verify_token_post": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )
        self.verify_verify_api_auth_verify_post_endpoint = _Endpoint(
            settings={
                "response_type": (UserRead,),
                "auth": [],
                "endpoint_path": "/api/auth/verify",
                "operation_id": "verify_verify_api_auth_verify_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body_verify_verify_api_auth_verify_post",
                ],
                "required": [
                    "body_verify_verify_api_auth_verify_post",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body_verify_verify_api_auth_verify_post": (BodyVerifyVerifyApiAuthVerifyPost,),
                },
                "attribute_map": {},
                "location_map": {
                    "body_verify_verify_api_auth_verify_post": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def auth_jwt_login_api_auth_jwt_login_post(self, username, password, **kwargs):
        """Auth:Jwt.Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_jwt_login_api_auth_jwt_login_post(username, password, async_req=True)
        >>> result = thread.get()

        Args:
            username (str):
            password (str):

        Keyword Args:
            grant_type (str): [optional]
            scope (str): [optional] if omitted the server will use the default value of ""
            client_id (str): [optional]
            client_secret (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["username"] = username
        kwargs["password"] = password
        return self.auth_jwt_login_api_auth_jwt_login_post_endpoint.call_with_http_info(**kwargs)

    def auth_jwt_logout_api_auth_jwt_logout_post(self, **kwargs):
        """Auth:Jwt.Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_jwt_logout_api_auth_jwt_logout_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.auth_jwt_logout_api_auth_jwt_logout_post_endpoint.call_with_http_info(**kwargs)

    def register_register_api_auth_register_post(self, user_create, **kwargs):
        """Register:Register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.register_register_api_auth_register_post(user_create, async_req=True)
        >>> result = thread.get()

        Args:
            user_create (UserCreate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            UserRead
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["user_create"] = user_create
        return self.register_register_api_auth_register_post_endpoint.call_with_http_info(**kwargs)

    def reset_forgot_password_api_auth_forgot_password_post(
        self, body_reset_forgot_password_api_auth_forgot_password_post, **kwargs
    ):
        """Reset:Forgot Password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reset_forgot_password_api_auth_forgot_password_post(body_reset_forgot_password_api_auth_forgot_password_post, async_req=True)
        >>> result = thread.get()

        Args:
            body_reset_forgot_password_api_auth_forgot_password_post (BodyResetForgotPasswordApiAuthForgotPasswordPost):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs[
            "body_reset_forgot_password_api_auth_forgot_password_post"
        ] = body_reset_forgot_password_api_auth_forgot_password_post
        return (
            self.reset_forgot_password_api_auth_forgot_password_post_endpoint.call_with_http_info(
                **kwargs
            )
        )

    def reset_reset_password_api_auth_reset_password_post(
        self, body_reset_reset_password_api_auth_reset_password_post, **kwargs
    ):
        """Reset:Reset Password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reset_reset_password_api_auth_reset_password_post(body_reset_reset_password_api_auth_reset_password_post, async_req=True)
        >>> result = thread.get()

        Args:
            body_reset_reset_password_api_auth_reset_password_post (BodyResetResetPasswordApiAuthResetPasswordPost):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs[
            "body_reset_reset_password_api_auth_reset_password_post"
        ] = body_reset_reset_password_api_auth_reset_password_post
        return self.reset_reset_password_api_auth_reset_password_post_endpoint.call_with_http_info(
            **kwargs
        )

    def verify_request_token_api_auth_request_verify_token_post(
        self, body_verify_request_token_api_auth_request_verify_token_post, **kwargs
    ):
        """Verify:Request-Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_request_token_api_auth_request_verify_token_post(body_verify_request_token_api_auth_request_verify_token_post, async_req=True)
        >>> result = thread.get()

        Args:
            body_verify_request_token_api_auth_request_verify_token_post (BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs[
            "body_verify_request_token_api_auth_request_verify_token_post"
        ] = body_verify_request_token_api_auth_request_verify_token_post
        return self.verify_request_token_api_auth_request_verify_token_post_endpoint.call_with_http_info(
            **kwargs
        )

    def verify_verify_api_auth_verify_post(self, body_verify_verify_api_auth_verify_post, **kwargs):
        """Verify:Verify  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_verify_api_auth_verify_post(body_verify_verify_api_auth_verify_post, async_req=True)
        >>> result = thread.get()

        Args:
            body_verify_verify_api_auth_verify_post (BodyVerifyVerifyApiAuthVerifyPost):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            UserRead
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["body_verify_verify_api_auth_verify_post"] = body_verify_verify_api_auth_verify_post
        return self.verify_verify_api_auth_verify_post_endpoint.call_with_http_info(**kwargs)