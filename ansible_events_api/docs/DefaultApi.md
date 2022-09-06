# ansible_events_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticated_route_api_authenticated_route_get**](DefaultApi.md#authenticated_route_api_authenticated_route_get) | **GET** /api/authenticated-route | Authenticated Route
[**create_activation**](DefaultApi.md#create_activation) | **POST** /api/activations/ | Create Activation
[**create_activation_instance_api_activation_instance_post**](DefaultApi.md#create_activation_instance_api_activation_instance_post) | **POST** /api/activation_instance/ | Create Activation Instance
[**create_extra_vars_api_extra_vars_post**](DefaultApi.md#create_extra_vars_api_extra_vars_post) | **POST** /api/extra_vars/ | Create Extra Vars
[**create_inventory_api_inventory_post**](DefaultApi.md#create_inventory_api_inventory_post) | **POST** /api/inventory/ | Create Inventory
[**create_job_instance_api_job_instance_post**](DefaultApi.md#create_job_instance_api_job_instance_post) | **POST** /api/job_instance/ | Create Job Instance
[**create_projects**](DefaultApi.md#create_projects) | **POST** /api/projects/ | Create Project
[**create_rulebook_api_rulebooks_post**](DefaultApi.md#create_rulebook_api_rulebooks_post) | **POST** /api/rulebooks/ | Create Rulebook
[**deactivate_api_deactivate_post**](DefaultApi.md#deactivate_api_deactivate_post) | **POST** /api/deactivate/ | Deactivate
[**delete_activation_instance**](DefaultApi.md#delete_activation_instance) | **DELETE** /api/activation_instance/{activation_instance_id} | Delete Activation Instance
[**delete_job_instance**](DefaultApi.md#delete_job_instance) | **DELETE** /api/job_instance/{job_instance_id} | Delete Job Instance
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /api/project/{project_id} | Delete Project
[**list_activation_instance_logs_api_activation_instance_logs_get**](DefaultApi.md#list_activation_instance_logs_api_activation_instance_logs_get) | **GET** /api/activation_instance_logs/ | List Activation Instance Logs
[**list_activation_instances_api_activation_instances_get**](DefaultApi.md#list_activation_instances_api_activation_instances_get) | **GET** /api/activation_instances/ | List Activation Instances
[**list_extra_vars_api_extra_vars_get**](DefaultApi.md#list_extra_vars_api_extra_vars_get) | **GET** /api/extra_vars/ | List Extra Vars
[**list_inventories_api_inventories_get**](DefaultApi.md#list_inventories_api_inventories_get) | **GET** /api/inventories/ | List Inventories
[**list_job_instances_api_job_instances_get**](DefaultApi.md#list_job_instances_api_job_instances_get) | **GET** /api/job_instances/ | List Job Instances
[**list_playbooks_api_playbooks_get**](DefaultApi.md#list_playbooks_api_playbooks_get) | **GET** /api/playbooks/ | List Playbooks
[**list_projects**](DefaultApi.md#list_projects) | **GET** /api/projects/ | List Projects
[**list_rulebooks_api_rulebooks_get**](DefaultApi.md#list_rulebooks_api_rulebooks_get) | **GET** /api/rulebooks/ | List Rulebooks
[**list_rules**](DefaultApi.md#list_rules) | **GET** /api/rules/ | List Rules
[**list_tasks_api_tasks_get**](DefaultApi.md#list_tasks_api_tasks_get) | **GET** /api/tasks/ | List Tasks
[**ping_ping_get**](DefaultApi.md#ping_ping_get) | **GET** /ping | Ping
[**read_activation_instance_api_activation_instance_activation_instance_id_get**](DefaultApi.md#read_activation_instance_api_activation_instance_activation_instance_id_get) | **GET** /api/activation_instance/{activation_instance_id} | Read Activation Instance
[**read_activation_instance_job_instances_api_activation_instance_job_instances_activation_instance_id_get**](DefaultApi.md#read_activation_instance_job_instances_api_activation_instance_job_instances_activation_instance_id_get) | **GET** /api/activation_instance_job_instances/{activation_instance_id} | Read Activation Instance Job Instances
[**read_extravar_api_extra_var_extra_var_id_get**](DefaultApi.md#read_extravar_api_extra_var_extra_var_id_get) | **GET** /api/extra_var/{extra_var_id} | Read Extravar
[**read_inventory_api_inventory_inventory_id_get**](DefaultApi.md#read_inventory_api_inventory_inventory_id_get) | **GET** /api/inventory/{inventory_id} | Read Inventory
[**read_job_instance_api_job_instance_job_instance_id_get**](DefaultApi.md#read_job_instance_api_job_instance_job_instance_id_get) | **GET** /api/job_instance/{job_instance_id} | Read Job Instance
[**read_job_instance_events_api_job_instance_events_job_instance_id_get**](DefaultApi.md#read_job_instance_events_api_job_instance_events_job_instance_id_get) | **GET** /api/job_instance_events/{job_instance_id} | Read Job Instance Events
[**read_playbook_api_playbook_playbook_id_get**](DefaultApi.md#read_playbook_api_playbook_playbook_id_get) | **GET** /api/playbook/{playbook_id} | Read Playbook
[**read_project**](DefaultApi.md#read_project) | **GET** /api/projects/{project_id} | Read Project
[**read_rulebook_api_rulebooks_rulebook_id_get**](DefaultApi.md#read_rulebook_api_rulebooks_rulebook_id_get) | **GET** /api/rulebooks/{rulebook_id} | Read Rulebook
[**read_rulebook_json_api_rulebook_json_rulebook_id_get**](DefaultApi.md#read_rulebook_json_api_rulebook_json_rulebook_id_get) | **GET** /api/rulebook_json/{rulebook_id} | Read Rulebook Json
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**show_rule**](DefaultApi.md#show_rule) | **GET** /api/rules/{rule_id}/ | Show Rule
[**update_project**](DefaultApi.md#update_project) | **PATCH** /api/projects/{project_id} | Update Project


# **authenticated_route_api_authenticated_route_get**
> bool, date, datetime, dict, float, int, list, str, none_type authenticated_route_api_authenticated_route_get()

Authenticated Route

### Example

* Api Key Authentication (APIKeyCookie):
* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Authenticated Route
        api_response = api_instance.authenticated_route_api_authenticated_route_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->authenticated_route_api_authenticated_route_get: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activation**
> Activation create_activation(activation)

Create Activation

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.activation import Activation
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
    api_instance = default_api.DefaultApi(api_client)
    activation = Activation(
        id=1,
        name="name_example",
        description="description_example",
        execution_env_id=1,
        rulebook_id=1,
        inventory_id=1,
        restart_policy_id=1,
        playbook_id=1,
        activation_enabled=True,
        extra_var_id=1,
    ) # Activation |

    # example passing only required values which don't have defaults set
    try:
        # Create Activation
        api_response = api_instance.create_activation(activation)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->create_activation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation** | [**Activation**](Activation.md)|  |

### Return type

[**Activation**](Activation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activation_instance_api_activation_instance_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_activation_instance_api_activation_instance_post(activation_instance)

Create Activation Instance

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.activation_instance import ActivationInstance
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
    api_instance = default_api.DefaultApi(api_client)
    activation_instance = ActivationInstance(
        id=1,
        name="name_example",
        rulebook_id=1,
        inventory_id=1,
        extra_var_id=1,
    ) # ActivationInstance |

    # example passing only required values which don't have defaults set
    try:
        # Create Activation Instance
        api_response = api_instance.create_activation_instance_api_activation_instance_post(activation_instance)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->create_activation_instance_api_activation_instance_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_instance** | [**ActivationInstance**](ActivationInstance.md)|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_extra_vars_api_extra_vars_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_extra_vars_api_extra_vars_post(extravars)

Create Extra Vars

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.extravars import Extravars
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    extravars = Extravars(
        name="name_example",
        extra_var="extra_var_example",
        id=1,
    ) # Extravars |

    # example passing only required values which don't have defaults set
    try:
        # Create Extra Vars
        api_response = api_instance.create_extra_vars_api_extra_vars_post(extravars)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->create_extra_vars_api_extra_vars_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extravars** | [**Extravars**](Extravars.md)|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inventory_api_inventory_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_inventory_api_inventory_post(inventory)

Create Inventory

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.inventory import Inventory
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
    api_instance = default_api.DefaultApi(api_client)
    inventory = Inventory(
        name="name_example",
        inventory="inventory_example",
        id=1,
    ) # Inventory |

    # example passing only required values which don't have defaults set
    try:
        # Create Inventory
        api_response = api_instance.create_inventory_api_inventory_post(inventory)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->create_inventory_api_inventory_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory** | [**Inventory**](Inventory.md)|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_instance_api_job_instance_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_job_instance_api_job_instance_post(job_instance)

Create Job Instance

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.job_instance import JobInstance
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    job_instance = JobInstance(
        id=1,
        playbook_id=1,
        inventory_id=1,
        extra_var_id=1,
    ) # JobInstance |

    # example passing only required values which don't have defaults set
    try:
        # Create Job Instance
        api_response = api_instance.create_job_instance_api_job_instance_post(job_instance)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->create_job_instance_api_job_instance_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance** | [**JobInstance**](JobInstance.md)|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_projects**
> ProjectRead create_projects(project_create)

Create Project

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.project_read import ProjectRead
from ansible_events_api.model.project_create import ProjectCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    project_create = ProjectCreate(
        id=1,
        git_hash="git_hash_example",
        url="url_example",
        name="name_example",
        description="description_example",
    ) # ProjectCreate |

    # example passing only required values which don't have defaults set
    try:
        # Create Project
        api_response = api_instance.create_projects(project_create)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->create_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  |

### Return type

[**ProjectRead**](ProjectRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rulebook_api_rulebooks_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_rulebook_api_rulebooks_post(rulebook)

Create Rulebook

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.rulebook import Rulebook
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
    api_instance = default_api.DefaultApi(api_client)
    rulebook = Rulebook(
        name="name_example",
        rulesets="rulesets_example",
        id=1,
    ) # Rulebook |

    # example passing only required values which don't have defaults set
    try:
        # Create Rulebook
        api_response = api_instance.create_rulebook_api_rulebooks_post(rulebook)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->create_rulebook_api_rulebooks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rulebook** | [**Rulebook**](Rulebook.md)|  |

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_api_deactivate_post**
> bool, date, datetime, dict, float, int, list, str, none_type deactivate_api_deactivate_post(activation_instance_id)

Deactivate

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    activation_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Deactivate
        api_response = api_instance.deactivate_api_deactivate_post(activation_instance_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->deactivate_api_deactivate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_instance_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activation_instance**
> delete_activation_instance(activation_instance_id)

Delete Activation Instance

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    activation_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Delete Activation Instance
        api_instance.delete_activation_instance(activation_instance_id)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_activation_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_instance_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_instance**
> delete_job_instance(job_instance_id)

Delete Job Instance

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    job_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Delete Job Instance
        api_instance.delete_job_instance(job_instance_id)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_job_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Delete Project

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    project_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Delete Project
        api_instance.delete_project(project_id)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activation_instance_logs_api_activation_instance_logs_get**
> [ActivationLog] list_activation_instance_logs_api_activation_instance_logs_get(activation_instance_id)

List Activation Instance Logs

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.activation_log import ActivationLog
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
    api_instance = default_api.DefaultApi(api_client)
    activation_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # List Activation Instance Logs
        api_response = api_instance.list_activation_instance_logs_api_activation_instance_logs_get(activation_instance_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_activation_instance_logs_api_activation_instance_logs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_instance_id** | **int**|  |

### Return type

[**[ActivationLog]**](ActivationLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activation_instances_api_activation_instances_get**
> bool, date, datetime, dict, float, int, list, str, none_type list_activation_instances_api_activation_instances_get()

List Activation Instances

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Activation Instances
        api_response = api_instance.list_activation_instances_api_activation_instances_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_activation_instances_api_activation_instances_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_extra_vars_api_extra_vars_get**
> bool, date, datetime, dict, float, int, list, str, none_type list_extra_vars_api_extra_vars_get()

List Extra Vars

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Extra Vars
        api_response = api_instance.list_extra_vars_api_extra_vars_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_extra_vars_api_extra_vars_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventories_api_inventories_get**
> bool, date, datetime, dict, float, int, list, str, none_type list_inventories_api_inventories_get()

List Inventories

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Inventories
        api_response = api_instance.list_inventories_api_inventories_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_inventories_api_inventories_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_instances_api_job_instances_get**
> bool, date, datetime, dict, float, int, list, str, none_type list_job_instances_api_job_instances_get()

List Job Instances

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Job Instances
        api_response = api_instance.list_job_instances_api_job_instances_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_job_instances_api_job_instances_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_playbooks_api_playbooks_get**
> bool, date, datetime, dict, float, int, list, str, none_type list_playbooks_api_playbooks_get()

List Playbooks

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Playbooks
        api_response = api_instance.list_playbooks_api_playbooks_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_playbooks_api_playbooks_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> [ProjectList] list_projects()

List Projects

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.project_list import ProjectList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Projects
        api_response = api_instance.list_projects()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_projects: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ProjectList]**](ProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rulebooks_api_rulebooks_get**
> bool, date, datetime, dict, float, int, list, str, none_type list_rulebooks_api_rulebooks_get()

List Rulebooks

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Rulebooks
        api_response = api_instance.list_rulebooks_api_rulebooks_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_rulebooks_api_rulebooks_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rules**
> [Rule] list_rules()

List Rules

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Rules
        api_response = api_instance.list_rules()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_rules: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Rule]**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks_api_tasks_get**
> bool, date, datetime, dict, float, int, list, str, none_type list_tasks_api_tasks_get()

List Tasks

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Tasks
        api_response = api_instance.list_tasks_api_tasks_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->list_tasks_api_tasks_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_ping_get**
> bool, date, datetime, dict, float, int, list, str, none_type ping_ping_get()

Ping

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Ping
        api_response = api_instance.ping_ping_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->ping_ping_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_activation_instance_api_activation_instance_activation_instance_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_activation_instance_api_activation_instance_activation_instance_id_get(activation_instance_id)

Read Activation Instance

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    activation_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Activation Instance
        api_response = api_instance.read_activation_instance_api_activation_instance_activation_instance_id_get(activation_instance_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_activation_instance_api_activation_instance_activation_instance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_instance_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_activation_instance_job_instances_api_activation_instance_job_instances_activation_instance_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_activation_instance_job_instances_api_activation_instance_job_instances_activation_instance_id_get(activation_instance_id)

Read Activation Instance Job Instances

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    activation_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Activation Instance Job Instances
        api_response = api_instance.read_activation_instance_job_instances_api_activation_instance_job_instances_activation_instance_id_get(activation_instance_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_activation_instance_job_instances_api_activation_instance_job_instances_activation_instance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_instance_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_extravar_api_extra_var_extra_var_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_extravar_api_extra_var_extra_var_id_get(extra_var_id)

Read Extravar

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    extra_var_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Extravar
        api_response = api_instance.read_extravar_api_extra_var_extra_var_id_get(extra_var_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_extravar_api_extra_var_extra_var_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extra_var_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_inventory_api_inventory_inventory_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_inventory_api_inventory_inventory_id_get(inventory_id)

Read Inventory

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    inventory_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Inventory
        api_response = api_instance.read_inventory_api_inventory_inventory_id_get(inventory_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_inventory_api_inventory_inventory_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_job_instance_api_job_instance_job_instance_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_job_instance_api_job_instance_job_instance_id_get(job_instance_id)

Read Job Instance

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    job_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Job Instance
        api_response = api_instance.read_job_instance_api_job_instance_job_instance_id_get(job_instance_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_job_instance_api_job_instance_job_instance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_job_instance_events_api_job_instance_events_job_instance_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_job_instance_events_api_job_instance_events_job_instance_id_get(job_instance_id)

Read Job Instance Events

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    job_instance_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Job Instance Events
        api_response = api_instance.read_job_instance_events_api_job_instance_events_job_instance_id_get(job_instance_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_job_instance_events_api_job_instance_events_job_instance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_instance_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_playbook_api_playbook_playbook_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_playbook_api_playbook_playbook_id_get(playbook_id)

Read Playbook

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    playbook_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Playbook
        api_response = api_instance.read_playbook_api_playbook_playbook_id_get(playbook_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_playbook_api_playbook_playbook_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbook_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project**
> ProjectDetail read_project(project_id)

Read Project

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.project_detail import ProjectDetail
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
    api_instance = default_api.DefaultApi(api_client)
    project_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Project
        api_response = api_instance.read_project(project_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_rulebook_api_rulebooks_rulebook_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_rulebook_api_rulebooks_rulebook_id_get(rulebook_id)

Read Rulebook

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    rulebook_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Rulebook
        api_response = api_instance.read_rulebook_api_rulebooks_rulebook_id_get(rulebook_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_rulebook_api_rulebooks_rulebook_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rulebook_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_rulebook_json_api_rulebook_json_rulebook_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_rulebook_json_api_rulebook_json_rulebook_id_get(rulebook_id)

Read Rulebook Json

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    rulebook_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Read Rulebook Json
        api_response = api_instance.read_rulebook_json_api_rulebook_json_rulebook_id_get(rulebook_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->read_rulebook_json_api_rulebook_json_rulebook_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rulebook_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> bool, date, datetime, dict, float, int, list, str, none_type root_get()

Root

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Root
        api_response = api_instance.root_get()
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_rule**
> Rule show_rule(rule_id)

Show Rule

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    rule_id = 1 # int |

    # example passing only required values which don't have defaults set
    try:
        # Show Rule
        api_response = api_instance.show_rule(rule_id)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->show_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**|  |

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ProjectRead update_project(project_id, project_update)

Update Project

### Example


```python
import time
import ansible_events_api
from ansible_events_api.api import default_api
from ansible_events_api.model.project_update import ProjectUpdate
from ansible_events_api.model.http_validation_error import HTTPValidationError
from ansible_events_api.model.project_read import ProjectRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible_events_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ansible_events_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    project_id = 1 # int |
    project_update = ProjectUpdate(
        name="name_example",
    ) # ProjectUpdate |

    # example passing only required values which don't have defaults set
    try:
        # Update Project
        api_response = api_instance.update_project(project_id, project_update)
        pprint(api_response)
    except ansible_events_api.ApiException as e:
        print("Exception when calling DefaultApi->update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **project_update** | [**ProjectUpdate**](ProjectUpdate.md)|  |

### Return type

[**ProjectRead**](ProjectRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
