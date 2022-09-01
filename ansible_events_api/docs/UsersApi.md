# ansible_events_api.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_current_user_api_users_me_get**](UsersApi.md#users_current_user_api_users_me_get) | **GET** /api/users/me | Users:Current User
[**users_delete_user_api_users_id_delete**](UsersApi.md#users_delete_user_api_users_id_delete) | **DELETE** /api/users/{id} | Users:Delete User
[**users_patch_current_user_api_users_me_patch**](UsersApi.md#users_patch_current_user_api_users_me_patch) | **PATCH** /api/users/me | Users:Patch Current User
[**users_patch_user_api_users_id_patch**](UsersApi.md#users_patch_user_api_users_id_patch) | **PATCH** /api/users/{id} | Users:Patch User
[**users_user_api_users_id_get**](UsersApi.md#users_user_api_users_id_get) | **GET** /api/users/{id} | Users:User


# **users_current_user_api_users_me_get**
> UserRead users_current_user_api_users_me_get()

Users:Current User

### Example

* Api Key Authentication (APIKeyCookie):

```python
import time
import ansible_events_api
from ansible_events_api.api import users_api
from ansible_events_api.model.user_read import UserRead
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

# Enter a context with an instance of the API client
with ansible_events_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Users:Current User
        api_response = api_instance.users_current_user_api_users_me_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling UsersApi->users_current_user_api_users_me_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserRead**](UserRead.md)

### Authorization

[APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_user_api_users_id_delete**
> users_delete_user_api_users_id_delete(id)

Users:Delete User

### Example

* Api Key Authentication (APIKeyCookie):

```python
import time
import ansible_events_api
from ansible_events_api.api import users_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
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

# Enter a context with an instance of the API client
with ansible_events_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type |

    # example passing only required values which don't have defaults set
    try:
        # Users:Delete User
        api_instance.users_delete_user_api_users_id_delete(id)
    except ansible_events_api.ApiException as e:
        print("Exception when calling UsersApi->users_delete_user_api_users_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

void (empty response body)

### Authorization

[APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_patch_current_user_api_users_me_patch**
> UserRead users_patch_current_user_api_users_me_patch(user_update)

Users:Patch Current User

### Example

* Api Key Authentication (APIKeyCookie):

```python
import time
import ansible_events_api
from ansible_events_api.api import users_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.user_update import UserUpdate
from ansible_events_api.model.error_model import ErrorModel
from ansible_events_api.model.user_read import UserRead
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

# Enter a context with an instance of the API client
with ansible_events_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_update = UserUpdate(
        password="password_example",
        email="email_example",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    ) # UserUpdate |

    # example passing only required values which don't have defaults set
    try:
        # Users:Patch Current User
        api_response = api_instance.users_patch_current_user_api_users_me_patch(user_update)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling UsersApi->users_patch_current_user_api_users_me_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update** | [**UserUpdate**](UserUpdate.md)|  |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_patch_user_api_users_id_patch**
> UserRead users_patch_user_api_users_id_patch(id, user_update)

Users:Patch User

### Example

* Api Key Authentication (APIKeyCookie):

```python
import time
import ansible_events_api
from ansible_events_api.api import users_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.user_update import UserUpdate
from ansible_events_api.model.error_model import ErrorModel
from ansible_events_api.model.user_read import UserRead
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

# Enter a context with an instance of the API client
with ansible_events_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type |
    user_update = UserUpdate(
        password="password_example",
        email="email_example",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    ) # UserUpdate |

    # example passing only required values which don't have defaults set
    try:
        # Users:Patch User
        api_response = api_instance.users_patch_user_api_users_id_patch(id, user_update)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling UsersApi->users_patch_user_api_users_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **user_update** | [**UserUpdate**](UserUpdate.md)|  |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_api_users_id_get**
> UserRead users_user_api_users_id_get(id)

Users:User

### Example

* Api Key Authentication (APIKeyCookie):

```python
import time
import ansible_events_api
from ansible_events_api.api import users_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.user_read import UserRead
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

# Enter a context with an instance of the API client
with ansible_events_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type |

    # example passing only required values which don't have defaults set
    try:
        # Users:User
        api_response = api_instance.users_user_api_users_id_get(id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling UsersApi->users_user_api_users_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
