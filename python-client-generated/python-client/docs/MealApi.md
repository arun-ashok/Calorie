# swagger_client.MealApi

All URIs are relative to *https://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_meal**](MealApi.md#add_meal) | **POST** /meals | Add meal
[**delete_meal**](MealApi.md#delete_meal) | **DELETE** /meals/{meal_id} | Delete meal entry
[**get_meal_by_meal_id**](MealApi.md#get_meal_by_meal_id) | **GET** /meals/{meal_id} | Get meal by meal id
[**update_meal**](MealApi.md#update_meal) | **PUT** /meals/{meal_id} | Update Meal entry


# **add_meal**
> add_meal(body)

Add meal

This can only be done by the logged in user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MealApi()
body = swagger_client.Meal() # Meal | Meal object to Add

try:
    # Add meal
    api_instance.add_meal(body)
except ApiException as e:
    print("Exception when calling MealApi->add_meal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Meal**](Meal.md)| Meal object to Add | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meal**
> delete_meal(meal_id)

Delete meal entry

This can only be done by the logged in user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MealApi()
meal_id = 'meal_id_example' # str | The meal that needs to be deleted.

try:
    # Delete meal entry
    api_instance.delete_meal(meal_id)
except ApiException as e:
    print("Exception when calling MealApi->delete_meal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meal_id** | **str**| The meal that needs to be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meal_by_meal_id**
> Meal get_meal_by_meal_id(meal_id)

Get meal by meal id

Get Meal by specifying the meal ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MealApi()
meal_id = 'meal_id_example' # str | The meal that needs to be fetched.

try:
    # Get meal by meal id
    api_response = api_instance.get_meal_by_meal_id(meal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MealApi->get_meal_by_meal_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meal_id** | **str**| The meal that needs to be fetched. | 

### Return type

[**Meal**](Meal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meal**
> update_meal(meal_id, body)

Update Meal entry

This can only be done by the logged in user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MealApi()
meal_id = 'meal_id_example' # str | meal that needs to be updated
body = swagger_client.Meal() # Meal | Updated meal object

try:
    # Update Meal entry
    api_instance.update_meal(meal_id, body)
except ApiException as e:
    print("Exception when calling MealApi->update_meal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meal_id** | **str**| meal that needs to be updated | 
 **body** | [**Meal**](Meal.md)| Updated meal object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

