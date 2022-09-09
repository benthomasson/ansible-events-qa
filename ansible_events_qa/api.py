"""
Module for custom implementation of the api client
"""
import logging
import time
import typing
from functools import cached_property
from functools import lru_cache

import jwt

import ansible_events_api.apis as apis
import ansible_events_qa.exceptions as exceptions
from ansible_events_api.api_client import ApiClient as OpenApiClient
from ansible_events_api.configuration import (
    Configuration as OpenApiConfiguration,
)
from ansible_events_api.exceptions import ApiException
from ansible_events_qa.config import config
from ansible_events_qa.config import Settings


LOGGER = logging.getLogger("aeqe_api")


class Configuration(OpenApiConfiguration):
    """
    Custom implementation of client library configuration.
    Overrides some attributes for auth management and http config
    """

    def __init__(self, auth_backend=None, config=config, *args, **kwargs):
        self._access_token = None
        host = config.base_url
        self._auth_backend = auth_backend
        super().__init__(host=host, *args, **kwargs)
        self.verify_ssl = config.http.verify_ssl  # type: ignore comment;

    @property
    def access_token(self):
        if self._auth_backend is None or not hasattr(self._auth_backend, "get_token"):
            self._access_token = None
            return self._access_token
        return self._auth_backend.get_token()

    @access_token.setter
    def access_token(self, token: str) -> None:
        self._access_token = token


C = typing.TypeVar("C", bound="Response")


class Response:
    """
    Stores the wrapped response from the openapi-client response
    """

    status_code: typing.Optional[int]
    data: typing.Any

    def __str__(self) -> str:
        return f"{self.__class__}: status_code: {self.status_code}, data: {type(self.data)}"

    def __repr__(self) -> str:
        return f"{self.__class__}: status_code: {self.status_code}, data: {type(self.data)}"

    def __init__(self, status_code=None, data=None):
        self.status_code = status_code
        self.data = data

    @classmethod
    def from_response(cls: type[C], response: tuple) -> C:
        return cls(data=response[0], status_code=response[1])

    @classmethod
    def from_exception(cls: type[C], response: ApiException) -> C:
        return cls(status_code=response.status, data=response.body)


class BaseApi:
    """
    Base class to wrap openapi api's. All wrappers should inherit from this class.
    Implements client instantiation from the children as well as wraps the request and response
    """

    api: typing.Callable

    def __init__(self, client):
        self.client = client
        self.api_instance = self.api(client)

    def run(self, operation: str, *args, **kwargs) -> Response:
        caller = getattr(self.api_instance, operation)
        try:
            LOGGER.info(f"Running request '{operation}' with args {args} - {kwargs}")
            response = caller(_return_http_data_only=False, *args, **kwargs)
            response = Response.from_response(response)
        except ApiException as e:
            LOGGER.info(
                f"Request {operation} failed with status code: {e.status}, response: {e.body}"
            )
            response = Response.from_exception(e)

        return response


class UsersApi(BaseApi):
    """
    Wraps the openapi api for users endpoints
    """

    api = apis.UsersApi


class CurrentUserApi(UsersApi):
    """
    Wraps the openapi api for current user endpoints
    """

    def show(self):
        operation = "users_current_user_api_users_me_get"
        return self.run(operation)


class AuthApi(BaseApi):
    """
    Wraps the openapi api for auth endpoints
    """

    api = apis.AuthApi

    def login(self, username, password):
        operation = "auth_bearer_login_api_auth_bearer_login_post"
        return self.run(operation, username=username, password=password)


class ProjectsApi(BaseApi):
    """
    Wraps the openapi api for projects endpoints
    """

    api = apis.DefaultApi

    def list(self) -> Response:  # noqa: A003
        operation = "list_projects"
        return self.run(operation)


A = typing.TypeVar("A", bound="ApiClient")


class ApiClient:
    """
    Wraps the Openapi api client, provides instantiations for path groups
    """

    def __init__(self, api_config) -> None:
        self.api_client = OpenApiClient(api_config)

    @cached_property
    def auth(self):
        return AuthApi(self.api_client)

    @cached_property
    def projects(self):
        return ProjectsApi(self.api_client)

    @cached_property
    def current_user(self):
        return CurrentUserApi(self.api_client)


class BearerTokenAuth:
    """
    Auth backend for Bearer token
    """

    def __init__(
        self,
        user_profile,
        config: Settings = config,
    ):
        self.token: typing.Optional[str] = None
        self.expires: typing.Optional[int] = None
        self.user_profile = user_profile
        self.config = config

    def get_token(self) -> str:
        if self.token is None or self.is_expired():
            self.token = self._get_token()
        return self.token

    def is_expired(self) -> bool:
        if self.expires is None:
            return True
        now = int(time.time())
        return self.expires - 1 <= now

    def _get_token(self):
        client = ApiClient(Configuration())
        try:
            user: dict = self.config.users.get(self.user_profile)  # type: ignore comment;
        except KeyError:
            msg = f"User profile: {self.user_profile} not found in settings"
            LOGGER.error(msg)
            raise exceptions.AuthError(msg)
        LOGGER.info(f"Performing login with user {user['username']}")
        request = client.auth.login(username=user["username"], password=user["password"])
        if request.status_code != 200:
            msg = f"Login failed. rc: {request.status_code}, msg: {request.data}"
            LOGGER.error(msg)
            raise exceptions.AuthError(msg)
        self.token = request.data.access_token
        self._set_expiration()
        return request.data.access_token

    def _set_expiration(self):
        data = jwt.decode(self.token, options={"verify_signature": False})  # type: ignore comment;
        self.expires = data["exp"]


@lru_cache
def get_api_client(user_profile: typing.Optional[str] = None) -> ApiClient:
    """
    Api client factory. Only bearer auth backend is supported for now.
    """
    if user_profile is None:
        user_profile = config.default_user  # type: ignore comment;
    auth_backend = BearerTokenAuth(user_profile=user_profile)
    api_config = Configuration(auth_backend)
    return ApiClient(api_config=api_config)


# default api client
api_client = get_api_client()
