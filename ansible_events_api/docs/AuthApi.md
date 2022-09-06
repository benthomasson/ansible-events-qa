# ansible_events_api.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_bearer_login_api_auth_bearer_login_post**](AuthApi.md#auth_bearer_login_api_auth_bearer_login_post) | **POST** /api/auth/bearer/login | Auth:Bearer.Login
[**auth_bearer_logout_api_auth_bearer_logout_post**](AuthApi.md#auth_bearer_logout_api_auth_bearer_logout_post) | **POST** /api/auth/bearer/logout | Auth:Bearer.Logout
[**auth_jwt_login_api_auth_jwt_login_post**](AuthApi.md#auth_jwt_login_api_auth_jwt_login_post) | **POST** /api/auth/jwt/login | Auth:Jwt.Login
[**auth_jwt_logout_api_auth_jwt_logout_post**](AuthApi.md#auth_jwt_logout_api_auth_jwt_logout_post) | **POST** /api/auth/jwt/logout | Auth:Jwt.Logout
[**register_register_api_auth_register_post**](AuthApi.md#register_register_api_auth_register_post) | **POST** /api/auth/register | Register:Register
[**reset_forgot_password_api_auth_forgot_password_post**](AuthApi.md#reset_forgot_password_api_auth_forgot_password_post) | **POST** /api/auth/forgot-password | Reset:Forgot Password
[**reset_reset_password_api_auth_reset_password_post**](AuthApi.md#reset_reset_password_api_auth_reset_password_post) | **POST** /api/auth/reset-password | Reset:Reset Password
[**verify_request_token_api_auth_request_verify_token_post**](AuthApi.md#verify_request_token_api_auth_request_verify_token_post) | **POST** /api/auth/request-verify-token | Verify:Request-Token
[**verify_verify_api_auth_verify_post**](AuthApi.md#verify_verify_api_auth_verify_post) | **POST** /api/auth/verify | Verify:Verify


# **auth_bearer_login_api_auth_bearer_login_post**
> BearerResponse auth_bearer_login_api_auth_bearer_login_post(username, password)

Auth:Bearer.Login

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from ansible_events_api.model.bearer_response import BearerResponse
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    username = "username_example" # str |
    password = "password_example" # str |
    grant_type = "passwor" # str |  (optional)
    scope = "" # str |  (optional) if omitted the server will use the default value of ""
    client_id = "client_id_example" # str |  (optional)
    client_secret = "client_secret_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Auth:Bearer.Login
        api_response = api_instance.auth_bearer_login_api_auth_bearer_login_post(username, password)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->auth_bearer_login_api_auth_bearer_login_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Auth:Bearer.Login
        api_response = api_instance.auth_bearer_login_api_auth_bearer_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->auth_bearer_login_api_auth_bearer_login_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **password** | **str**|  |
 **grant_type** | **str**|  | [optional]
 **scope** | **str**|  | [optional] if omitted the server will use the default value of ""
 **client_id** | **str**|  | [optional]
 **client_secret** | **str**|  | [optional]

### Return type

[**BearerResponse**](BearerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_bearer_logout_api_auth_bearer_logout_post**
> bool, date, datetime, dict, float, int, list, str, none_type auth_bearer_logout_api_auth_bearer_logout_post()

Auth:Bearer.Logout

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyCookie
configuration.api_key['APIKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyCookie'] = 'Bearer'

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ansible_events_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Auth:Bearer.Logout
        api_response = api_instance.auth_bearer_logout_api_auth_bearer_logout_post()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->auth_bearer_logout_api_auth_bearer_logout_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[APIKeyCookie](../README.md#APIKeyCookie), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_jwt_login_api_auth_jwt_login_post**
> bool, date, datetime, dict, float, int, list, str, none_type auth_jwt_login_api_auth_jwt_login_post(username, password)

Auth:Jwt.Login

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    username = "username_example" # str |
    password = "password_example" # str |
    grant_type = "passwor" # str |  (optional)
    scope = "" # str |  (optional) if omitted the server will use the default value of ""
    client_id = "client_id_example" # str |  (optional)
    client_secret = "client_secret_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Auth:Jwt.Login
        api_response = api_instance.auth_jwt_login_api_auth_jwt_login_post(username, password)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_login_api_auth_jwt_login_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Auth:Jwt.Login
        api_response = api_instance.auth_jwt_login_api_auth_jwt_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_login_api_auth_jwt_login_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **password** | **str**|  |
 **grant_type** | **str**|  | [optional]
 **scope** | **str**|  | [optional] if omitted the server will use the default value of ""
 **client_id** | **str**|  | [optional]
 **client_secret** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_jwt_logout_api_auth_jwt_logout_post**
> bool, date, datetime, dict, float, int, list, str, none_type auth_jwt_logout_api_auth_jwt_logout_post()

Auth:Jwt.Logout

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyCookie
configuration.api_key['APIKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyCookie'] = 'Bearer'

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ansible_events_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Auth:Jwt.Logout
        api_response = api_instance.auth_jwt_logout_api_auth_jwt_logout_post()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->auth_jwt_logout_api_auth_jwt_logout_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[APIKeyCookie](../README.md#APIKeyCookie), [OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_register_api_auth_register_post**
> UserRead register_register_api_auth_register_post(user_create)

Register:Register

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from ansible_events_api.model.user_create import UserCreate
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.error_model import ErrorModel
from ansible_events_api.model.user_read import UserRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    user_create = UserCreate(
        email="email_example",
        password="password_example",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    ) # UserCreate |

    # example passing only required values which don't have defaults set
    try:
        # Register:Register
        api_response = api_instance.register_register_api_auth_register_post(user_create)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->register_register_api_auth_register_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  |

### Return type

[**UserRead**](UserRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_forgot_password_api_auth_forgot_password_post**
> bool, date, datetime, dict, float, int, list, str, none_type reset_forgot_password_api_auth_forgot_password_post(body_reset_forgot_password_api_auth_forgot_password_post)

Reset:Forgot Password

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from ansible_events_api.model.body_reset_forgot_password_api_auth_forgot_password_post import BodyResetForgotPasswordApiAuthForgotPasswordPost
from ansible_events_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    body_reset_forgot_password_api_auth_forgot_password_post = BodyResetForgotPasswordApiAuthForgotPasswordPost(
        email="email_example",
    ) # BodyResetForgotPasswordApiAuthForgotPasswordPost |

    # example passing only required values which don't have defaults set
    try:
        # Reset:Forgot Password
        api_response = api_instance.reset_forgot_password_api_auth_forgot_password_post(body_reset_forgot_password_api_auth_forgot_password_post)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->reset_forgot_password_api_auth_forgot_password_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_reset_forgot_password_api_auth_forgot_password_post** | [**BodyResetForgotPasswordApiAuthForgotPasswordPost**](BodyResetForgotPasswordApiAuthForgotPasswordPost.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_reset_password_api_auth_reset_password_post**
> bool, date, datetime, dict, float, int, list, str, none_type reset_reset_password_api_auth_reset_password_post(body_reset_reset_password_api_auth_reset_password_post)

Reset:Reset Password

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from ansible_events_api.model.body_reset_reset_password_api_auth_reset_password_post import BodyResetResetPasswordApiAuthResetPasswordPost
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    body_reset_reset_password_api_auth_reset_password_post = BodyResetResetPasswordApiAuthResetPasswordPost(
        token="token_example",
        password="password_example",
    ) # BodyResetResetPasswordApiAuthResetPasswordPost |

    # example passing only required values which don't have defaults set
    try:
        # Reset:Reset Password
        api_response = api_instance.reset_reset_password_api_auth_reset_password_post(body_reset_reset_password_api_auth_reset_password_post)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->reset_reset_password_api_auth_reset_password_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_reset_reset_password_api_auth_reset_password_post** | [**BodyResetResetPasswordApiAuthResetPasswordPost**](BodyResetResetPasswordApiAuthResetPasswordPost.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_request_token_api_auth_request_verify_token_post**
> bool, date, datetime, dict, float, int, list, str, none_type verify_request_token_api_auth_request_verify_token_post(body_verify_request_token_api_auth_request_verify_token_post)

Verify:Request-Token

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from ansible_events_api.model.body_verify_request_token_api_auth_request_verify_token_post import BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost
from ansible_events_api.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    body_verify_request_token_api_auth_request_verify_token_post = BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost(
        email="email_example",
    ) # BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost |

    # example passing only required values which don't have defaults set
    try:
        # Verify:Request-Token
        api_response = api_instance.verify_request_token_api_auth_request_verify_token_post(body_verify_request_token_api_auth_request_verify_token_post)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->verify_request_token_api_auth_request_verify_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_verify_request_token_api_auth_request_verify_token_post** | [**BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost**](BodyVerifyRequestTokenApiAuthRequestVerifyTokenPost.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_verify_api_auth_verify_post**
> UserRead verify_verify_api_auth_verify_post(body_verify_verify_api_auth_verify_post)

Verify:Verify

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import auth_api
from ansible_events_api.model.body_verify_verify_api_auth_verify_post import BodyVerifyVerifyApiAuthVerifyPost
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.error_model import ErrorModel
from ansible_events_api.model.user_read import UserRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    body_verify_verify_api_auth_verify_post = BodyVerifyVerifyApiAuthVerifyPost(
        token="token_example",
    ) # BodyVerifyVerifyApiAuthVerifyPost |

    # example passing only required values which don't have defaults set
    try:
        # Verify:Verify
        api_response = api_instance.verify_verify_api_auth_verify_post(body_verify_verify_api_auth_verify_post)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling AuthApi->verify_verify_api_auth_verify_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_verify_verify_api_auth_verify_post** | [**BodyVerifyVerifyApiAuthVerifyPost**](BodyVerifyVerifyApiAuthVerifyPost.md)|  |

### Return type

[**UserRead**](UserRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
