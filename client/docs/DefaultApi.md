# greeting.DefaultApi

All URIs are relative to *http://swagger.dev:8080/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_hello_get**](DefaultApi.md#api_hello_get) | **GET** /hello | 
[**api_hello_post**](DefaultApi.md#api_hello_post) | **POST** /hello | 
[**api_member_get**](DefaultApi.md#api_member_get) | **GET** /member/{id} | 


# **api_hello_get**
> api_hello_get()



### Example 
```python
import time
import greeting
from greeting.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = greeting.DefaultApi()

try: 
    api_instance.api_hello_get()
except ApiException as e:
    print "Exception when calling DefaultApi->api_hello_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_hello_post**
> api_hello_post(name=name, year=year)



### Example 
```python
import time
import greeting
from greeting.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = greeting.DefaultApi()
name = 'name_example' # str | name (optional)
year = 'year_example' # str | year (optional)

try: 
    api_instance.api_hello_post(name=name, year=year)
except ApiException as e:
    print "Exception when calling DefaultApi->api_hello_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 
 **year** | **str**| year | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_member_get**
> api_member_get(id)



### Example 
```python
import time
import greeting
from greeting.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = greeting.DefaultApi()
id = 'id_example' # str | ID

try: 
    api_instance.api_member_get(id)
except ApiException as e:
    print "Exception when calling DefaultApi->api_member_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

