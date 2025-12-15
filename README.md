
# [Django Rest Framework](https://www.django-rest-framework.org/)

## ✅ **Summary of the Tutorial**

To build your **first Python API client** using the `requests` library and explains foundational concepts related to **REST APIs, endpoints, HTTP requests, JSON**, and how clients interact with APIs.

The main goal of the lesson is:
✔ Understanding what an API client is
✔ How to use Python's `requests` library
✔ Difference between regular HTTP response (HTML) and REST API response (JSON)
✔ How REST APIs allow software to communicate over the web

It demonstrates sending GET requests, receiving responses, sending JSON/form data, and reading status codes.

---

## 📝 **Important Pointers (Key Concepts)**

### **1. API Client Basics**

* A **client** is something that interacts with the internet or a web service.
* Python script using `requests` = API client.
* Browser (Chrome, Safari, Firefox) is also a client.

---

### **2. Endpoints**

* Endpoints = different URLs on a REST API that perform different functions.
* Example:

  ```
  https://httpbin.org
  https://httpbin.org/anything
  https://httpbin.org/status/200
  ```
* Normal website URLs return HTML.
* REST API endpoints return data (usually JSON).

---

### **3. HTTP GET Request Using Requests Library**

Example:

```python
import requests

endpoint = "https://httpbin.org/anything"
response = requests.get(endpoint)
```

* `response.text` → raw string response
* `response.json()` → parsed Python dictionary

---

### **4. HTML Response vs JSON Response**

#### **HTML (Non-API)**

* When you open a web page normally, you get HTML.
* Browsers read HTML and render the page.

#### **REST API Response**

* Sends JSON or XML, meant for machines, not humans.
* JSON is the standard.

---

## **5. JSON**

* Stands for: **JavaScript Object Notation**.
* Looks similar to a Python dictionary, but:

  * JSON uses `null`
  * Python uses `None`

Example JSON:

```json
{
  "query": "hello world",
  "data": null
}
```

---

## **6. Sending Data in a Request**

### **Sending JSON Data**

```python
requests.get(endpoint, json={"query": "hello world"})
```

* Server receives it as JSON.
* Header automatically becomes `Content-Type: application/json`.

### **Sending Form Data**

```python
requests.get(endpoint, data={"query": "hello world"})
```

* Server classifies it as form data.
* Header becomes `application/x-www-form-urlencoded`.

---

## **7. Status Codes**

* You can read them using:

  ```python
  response.status_code
  ```
* Common codes:

  * `200` → OK
  * `404` → Not Found
  * `400` → Bad Request
  * `500` → Internal Server Error

---

## **8. REST APIs Overview**

* A REST API is a **web-based API**.
* Allows software to talk to other software over HTTP.
* Not meant for humans; meant for programs.

---

## **9. Multiple Clients Can Use the Same API**

Examples:

* Python client
* Browser
* Mobile apps
* JavaScript front-end apps

Any client capable of HTTP requests can use the API.

---

# 📌 **Final Notes**

### ✔ REST API = Web API

### ✔ Uses HTTP requests (GET, POST, PUT, DELETE)

### ✔ Endpoints = different paths of the API

### ✔ Use Python `requests` library to interact with APIs

### ✔ JSON is the standard data format

### ✔ httpbin.org is great for testing

### ✔ Status codes are important for debugging

### ✔ REST APIs allow many clients to consume the same service

---

## 1. Running Django Locally for API Testing

### Using Multiple Terminal Tabs

* Open **two terminal tabs**:

  * One for running the Django server
  * One for running the Python client
* This makes it easy to **see server logs while testing requests**

### Running the Django Server

```bash
python manage.py runserver 8000
```

**Important notes:**

* `8000` is the default port, but explicitly specifying it avoids confusion
* If the port changes, your client **must match the same port**
* If Django is not running → client requests will fail with:

  * `Connection refused`
  * Same error in browser (`Site can’t be reached`)

---

## 2. Python Client → Django Endpoint

### Initial Behavior

* When hitting Django’s root (`/`), the response is **HTML**
* Python client prints:

  * Raw HTML text
  * Status code (e.g. `200`)

This is expected because Django serves a **web page by default**, not JSON.

---

## 3. localhost vs 127.0.0.1

* Both usually work
* `localhost` is preferred:

  * More practical long-term
  * More consistent across environments
* Use **one consistently**

---

## 4. Creating Your First API App

### Step 1: Create App

```bash
python manage.py startapp api
```

### Step 2: Register App

In `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'api',
]
```

---

## 5. Creating Your First API View

### `api/views.py`

```python
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({
        "message": "Hi there, this is your Django API response"
    })
```

**Key points:**

* `JsonResponse` is built into Django
* Automatically converts Python dictionaries → JSON
* Function-based views are simplest for learning

---

## 6. API URLs Setup (Clean Architecture)

### `api/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
]
```

### Project-Level `urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]
```

**Final endpoint:**

```
http://localhost:8000/api/
```

---

## 7. Calling the API from Python Client

* Update Python client endpoint to include `/api/`
* Now response is:

  * Status code
  * Raw text
  * Parsed JSON
* You can directly access fields like:

```python
data["message"]
```

✅ **You now have a working Django API**

---

## 8. Reading Request Data in Django

### Understanding `request`

* `request` is a **Django HttpRequest object**
* It is **NOT** the same as `requests` (Python library)

Useful attributes:

* `request.body`
* `request.headers`
* `request.GET`
* `request.POST`

---

## 9. Reading JSON Body (`request.body`)

### Important Behavior

* `request.body` returns **bytes**
* Usually contains a **JSON string**

Example:

```python
body = request.body
```

### Convert JSON → Python Dictionary

```python
import json

data = {}
try:
    data = json.loads(request.body)
except:
    pass
```

**Key insight:**

* JSON arrives as bytes → string → dictionary
* Always guard with `try/except` (body may be empty)

---

## 10. Echoing Request Data Back (Debug Technique)

You can return received data to understand requests better:

```python
return JsonResponse(data)
```

This is similar to tools like **httpbin.org**

---

## 11. Working with Headers

### Access Headers

```python
request.headers
```

⚠️ **Problem:**

* `request.headers` is NOT JSON-serializable

### Solution

Convert to dictionary:

```python
headers = dict(request.headers)
```

---

## 12. Content Type

```python
request.content_type
```

* Often `application/json`
* Useful for validating request formats

---

## 13. Query Parameters (GET Params)

### Example URL

```
/api/?abc=123
```

### Access in Django

```python
params = dict(request.GET)
```

* Always available via `request.GET`
* Empty if no query parameters

---

## 14. Full Echo Example (Conceptual)

```python
data = {
    "body": parsed_json,
    "params": dict(request.GET),
    "headers": dict(request.headers),
    "content_type": request.content_type,
}
return JsonResponse(data)
```

---

## 15. Key Lessons & Takeaways

### Core Concepts Learned

* Django serves HTML by default
* APIs require `JsonResponse`
* `request.body` → bytes → JSON → dict
* Headers must be converted to dict
* Query params come from `request.GET`

### Why This Matters

* These are **fundamental building blocks**
* Same concepts apply when:

  * Using Django models
  * Querying the database
  * Moving to Django Rest Framework (DRF)

---

## Creating a Django Model & Returning It from an API View

## 1. Creating a New App for Models

### Create the `products` app

```bash
python manage.py startapp products
```

### Register the app

In `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'products',
]
```

---

## 2. Creating the Product Model

### `products/models.py`

```python
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=99.99
    )
```

### Field breakdown

* **title**

  * `CharField`
  * `max_length=120`
* **content**

  * `TextField`
  * Optional (`blank=True`, `null=True`)
* **price**

  * `DecimalField`
  * Precision-safe for money
  * Default value provided

📌 **Important**

* Django automatically adds an `id` field (primary key)
* Each row in the DB = one model instance

---

## 3. Running Migrations

### Create migration files

```bash
python manage.py makemigrations
```

### Apply migrations to database

```bash
python manage.py migrate
```

**Key concept**

* `makemigrations` → detects model changes
* `migrate` → applies changes to the database

---

## 4. Creating Product Records (Django Shell)

### Open Django shell

```bash
python manage.py shell
```

### Create products

```python
from products.models import Product

Product.objects.create(
    title="Hello World",
    content="This is amazing!",
    price=0.00
)

Product.objects.create(
    title="Hello World Again",
    content="Another product",
    price=10.00
)
```

Now the database contains multiple products.

---

## 5. Fetching a Random Product

### Django ORM query

```python
Product.objects.all().order_by("?").first()
```

**What it does**

* Retrieves all products
* Randomly orders them
* Returns one product instance

📌 **Notes**

* Good for demos and learning
* Can be slow on large tables
* Returns `None` if no records exist

---

## 6. Returning Model Data from the API View

### Import the model

```python
from products.models import Product
```

### Query a random product

```python
model_data = Product.objects.all().order_by("?").first()
```

### Manually build response data

```python
data = {}

if model_data:
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['content'] = model_data.content
    data['price'] = model_data.price
```

### Return JSON

```python
from django.http import JsonResponse

return JsonResponse(data)
```

---

## 7. Why This Feels Tedious (On Purpose)

### What’s happening

* You are **manually serializing** a model instance
* Turning:

  ```
  Django Model Instance
      ↓
  Python Dictionary
      ↓
  JSON Response
  ```

### Why this matters

* This process is called **serialization**
* Every API must do this in some form
* Doing it manually helps you understand:

  * Data types
  * Field access
  * What JSON can and cannot handle

📌 **Key Insight**

> Django models cannot be returned directly as JSON — they must be converted first.

---

## 8. Common Errors & Fixes

### ❌ Error

```text
Product has no attribute 'object'
```

### ✅ Fix

```python
Product.objects
```

(Django always uses `objects`, plural.)

---

## 9. Observing API Output

* Each request returns:

  * A random product
  * Fields like `id`, `title`, `content`, `price`
* The `id` field:

  * Automatically added by Django
  * Useful for future lookups like:

    ```
    /api/products/1/
    ```

---

## 10. Why This Step Is Important

This tutorial section teaches:

* How Django models map to database tables
* How model instances represent database rows
* Why serialization is required for APIs
* How API endpoints eventually:

  * Accept IDs
  * Query the database
  * Return structured JSON

---

## Key tasks performed

* Created a `Product` model
* Migrated it to the database
* Inserted sample data
* Queried a random product
* Manually converted it to JSON
* Returned it from a Django API endpoint

---

## Converting a Django Model Instance to a Dictionary (Serialization Basics)

### 1. The Goal of This Section

* Convert a **Django model instance** into:

  ```
  Model Instance → Python Dictionary → JSON → API Response
  ```
* Learn a **built-in Django shortcut**
* Understand why **manual JSON handling is problematic**
* See why **Django Rest Framework (DRF)** is the preferred solution

---

### 2. Using `model_to_dict` (Built-in Django Helper)

#### Import

```python
from django.forms.models import model_to_dict
```

#### Basic Usage

```python
data = model_to_dict(model_data)
```

#### Result

* Automatically converts model fields into a dictionary
* Equivalent to manually writing:

  ```python
  {
      "id": model_data.id,
      "title": model_data.title,
      "content": model_data.content,
      "price": model_data.price,
  }
  ```

📌 **Key Insight**

> `model_to_dict` is a fast, clean way to serialize a single model instance.

---

### 3. Selecting Specific Fields

#### Limit returned fields

```python
data = model_to_dict(
    model_data,
    fields=['id', 'title']
)
```

#### Another example

```python
data = model_to_dict(
    model_data,
    fields=['id', 'title', 'price']
)
```

**Why this matters**

* Controls what your API exposes
* Avoids leaking unnecessary data
* Improves performance and clarity

---

### 4. Returning Data with `JsonResponse` (Recommended)

```python
from django.http import JsonResponse

return JsonResponse(data)
```

#### What `JsonResponse` does for you

* Converts Python dict → JSON automatically
* Sets correct headers:

  ```
  Content-Type: application/json
  ```
* Handles many data type conversions for you

✅ **This is the correct approach when using plain Django**

---

### 5. Trying the “Hard Way” with `HttpResponse`

#### Switching to `HttpResponse`

```python
from django.http import HttpResponse

return HttpResponse(data)
```

#### What goes wrong

* `HttpResponse` expects a **string**
* Default content type:

  ```
  text/html
  ```
* Python client fails when calling `.json()`

---

### 6. Fixing Headers Manually (Still Not Enough)

#### Set JSON content type

```python
return HttpResponse(
    data,
    content_type="application/json"
)
```

Now headers look correct, BUT…

---

### 7. JSON Serialization Errors

#### Problem #1 – Dictionary is not JSON

```text
TypeError: the JSON object must be str, bytes or bytearray
```

#### Fix attempt

```python
import json
json_data = json.dumps(data)
return HttpResponse(json_data, content_type="application/json")
```

---

### 8. Problem #2 – DecimalField Serialization

#### Error

```text
Object of type Decimal is not JSON serializable
```

#### Why this happens

* Django `DecimalField` returns a `Decimal`
* Python’s `json.dumps()` cannot serialize `Decimal` by default

Example problematic value:

```python
Decimal('99.99')
```

#### Possible fixes (not recommended here)

* Convert price to `float`
* Convert price to `str`
* Write a custom JSON encoder

📌 **Key Lesson**

> Manual JSON serialization quickly becomes complex and error-prone.

---

### 9. Why `JsonResponse` Works

```python
return JsonResponse(data)
```

* Automatically handles:

  * Decimals
  * Dates
  * Booleans
* Eliminates manual `json.dumps()`
* Sets headers correctly

✅ **Less code, fewer bugs**

---

### 10. Core Concept: Serialization

#### What is serialization?

* Converting complex Python objects (models) into:

  * Dictionaries
  * JSON-safe types

### What you learned

* Manual serialization is tedious
* `model_to_dict` helps but has limits
* `JsonResponse` simplifies a lot
* **DRF solves this problem completely**

---

### 11. Why Django Rest Framework Exists

DRF provides:

* Serializers
* Validation
* Automatic type handling
* Cleaner API views
* Better error handling
* Faster development

📌 **Big takeaway**

> Everything you struggled with here is exactly what DRF is designed to solve.

---

### 12. What This Section Did NOT Cover (On Purpose)

* Sending data (POST / PUT)
* Validation
* Authentication
* Permissions

These are **much harder** without DRF.

---

### 13. Final Takeaways

* `model_to_dict()` is a useful shortcut
* `JsonResponse` should always be preferred over `HttpResponse` for APIs
* Manual JSON handling breaks easily
* Decimal fields are a common pitfall
* DRF will clean all of this up

---

### In Short

```python
from django.forms.models import model_to_dict
from django.http import JsonResponse

data = model_to_dict(model_data, fields=['id', 'title', 'price'])
return JsonResponse(data)
```

✔ Clean
✔ Safe
✔ JSON-ready

---

## Converting `api_home` into a Django Rest Framework (DRF) View

## 1. What Changes When Moving to DRF

To convert a normal Django API view into a **DRF API view**, two key changes are required:

1. Replace `JsonResponse` with DRF’s `Response`
2. Decorate the view with `@api_view`

---

## 2. Importing DRF Components

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
```

### Why these matter

* `Response` replaces `JsonResponse`
* `@api_view` turns a normal Django view into a **DRF-powered API endpoint**

---

## 3. Converting the View

### Before (Plain Django)

```python
from django.http import JsonResponse

def api_home(request):
    data = {"message": "Hello World"}
    return JsonResponse(data)
```

---

### After (Django Rest Framework)

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_home(request):
    data = {"message": "Hello World"}
    return Response(data)
```

✅ This is now a **DRF API View**

---

## 4. HTTP Method Enforcement (Automatic)

### What happens if `@api_view` is missing?

* DRF doesn’t know:

  * Allowed HTTP methods
  * How to handle method validation
* Results in:

  ```
  API view missing list of allowed HTTP methods
  ```

### Declaring allowed methods

```python
@api_view(['GET'])
```

Other examples:

```python
@api_view(['POST'])
@api_view(['GET', 'POST'])
```

---

## 5. Built-in Method Validation (Huge Win)

### With DRF

```python
@api_view(['GET'])
```

If client sends POST:

```
405 Method Not Allowed
{
  "detail": "Method \"POST\" not allowed."
}
```

✔ Automatic
✔ Correct status code
✔ Standard error format

---

### Without DRF (Manual Django Way)

```python
def api_home(request):
    if request.method != 'GET':
        return JsonResponse(
            {"detail": "GET not allowed"},
            status=405
        )
```

❌ More code
❌ Must remember status codes
❌ Easy to get wrong

---

## 6. Why `Response` is Better Than `JsonResponse`

`Response` provides:

* Automatic content negotiation
* Correct JSON rendering
* Proper headers
* Integration with:

  * Serializers
  * Authentication
  * Permissions
  * Throttling

Example:

```python
return Response(data, status=200)
```

---

## 7. Authentication & Permissions (Preview)

Plain Django views:

* Authentication is **hard to bolt on**
* Requires custom middleware or logic

DRF views:

* Authentication is **built-in**
* Easily added later:

```python
@api_view(['GET'])
@permission_classes([IsAuthenticated])
```

📌 **Key Insight**

> DRF is not just about JSON — it’s about API infrastructure.

---

## 8. Why `@api_view` Is Required (Core Explanation)

### What `@api_view` actually does

It:

* Wraps your function in a DRF `APIView`
* Enables:

  * Method checking
  * Request parsing
  * Response rendering
  * Authentication hooks
  * Permission hooks

Without it:

* Your view is just a normal Django function
* DRF features will **not activate**

---

## 9. Simple Mental Model

```text
Normal Django View
        ↓
@api_view
        ↓
DRF APIView
        ↓
Full REST features enabled
```

---

## 10. Minimal Example Showing the Difference

### ❌ Without `@api_view`

```python
def hello(request):
    return Response({"msg": "Hi"})
```

Result:

```
AssertionError: APIView missing allowed methods
```

---

### ✅ With `@api_view`

```python
@api_view(['GET'])
def hello(request):
    return Response({"msg": "Hi"})
```

Works correctly ✔

---

## 11. Why DRF Forces Method Declaration

* REST APIs must be **explicit**
* Prevents accidental access
* Improves security
* Encourages clean API design

---

## 12. What Comes Next

### Current state

* DRF API view working
* GET method enforced
* Response rendering handled

### Next step

* Replace `model_to_dict`
* Use DRF **Serializers**
* Clean, reusable data transformation

---

## In short

* `@api_view` is **required** for function-based DRF views
* It activates:

  * Method validation
  * DRF request/response handling
* `Response` > `JsonResponse`
* DRF removes boilerplate and mistakes
* This sets the foundation for authentication, permissions, and serializers

---

## 📦 Django REST Framework – Model Serializers (Stage Setting)

## 🎯 Goal of This Section

* Explain **why Django REST Framework serializers are needed**
* Show limitations of `model_to_dict`
* Introduce **ModelSerializer**
* Demonstrate how serializers can:

  * Include computed properties
  * Rename fields
  * Add custom logic
  * Control API output cleanly

---

## 1️⃣ Problem Setup: Model Property Not Appearing in API

### Product Model Example

```python
class Product(models.Model):
    title = models.CharField(...)
    price = models.DecimalField(...)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)
```

✔ Works perfectly in Django shell:

```python
product.sale_price
```

❌ But **does NOT appear** when using:

```python
model_to_dict(instance)
```

### ❗ Key Limitation

* `model_to_dict`:

  * Only serializes **actual model fields**
  * Ignores:

    * `@property`
    * Instance methods
    * Computed values

---

## 2️⃣ Why This Pushes Us Toward DRF Serializers

Instead of manually adding keys like:

```python
data["sale_price"] = instance.sale_price
```

👉 **DRF serializers solve this cleanly and scalably**

---

## 3️⃣ Introducing `serializers.py`

Create a new file:

```text
products/
 ├── models.py
 ├── views.py
 ├── serializers.py  ✅
```

---

## 4️⃣ Serializer vs ModelForm (Important Analogy)

### ModelForm (Django)

```python
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "content", "price"]
```

### ModelSerializer (DRF)

```python
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "content", "price"]
```

🧠 **Key Insight**

> ModelSerializers are to APIs what ModelForms are to HTML forms

---

## 5️⃣ Using the Serializer in the View

```python
serializer = ProductSerializer(instance)
data = serializer.data
return Response(data)
```

### What Happens?

* Serializer:

  * Converts model → Python dict
  * Handles JSON formatting
  * Handles decimals, dates, etc.
  * Removes need for `json.dumps`

---

## 6️⃣ Automatically Including Properties

If you add this to `fields`:

```python
fields = ["title", "price", "sale_price"]
```

✔ `@property sale_price` is now included
✔ No extra code needed

---

## 7️⃣ Adding Instance Methods (Problem)

Model method:

```python
def get_discount(self):
    return 122
```

If added directly to `fields`:

```python
fields = ["get_discount"]
```

❌ Output field name becomes `"get_discount"`
❌ Not API-friendly

---

## 8️⃣ Renaming Fields Using `SerializerMethodField`

### Step 1: Define Field

```python
discount = serializers.SerializerMethodField(read_only=True)
```

### Step 2: Define Method

```python
def get_discount(self, obj):
    return obj.get_discount()
```

### Result

```json
{
  "discount": 122
}
```

✅ Clean API name
✅ Backed by model logic
✅ Read-only and safe

---

## 9️⃣ Access to Full Model Instance

Inside serializer methods:

```python
def get_discount(self, obj):
    return obj.id
```

✔ `obj` is the **actual model instance**
✔ You can access:

* `obj.user.username`
* `obj.category.name`
* Any FK / related field

---

## 🔑 Key Advantages of ModelSerializers

### ✅ 1. Replaces `model_to_dict`

* Handles:

  * Decimals
  * Dates
  * JSON compatibility

### ✅ 2. Enriches API Output

* Add:

  * Computed fields
  * Renamed fields
  * Custom logic

### ✅ 3. Clean Separation

* Models → data structure
* Serializers → data representation
* Views → request/response logic

---

## 10️⃣ Multiple Serializers for Same Model

```python
class ProductSerializer(serializers.ModelSerializer): ...
class ProductDetailSerializer(serializers.ModelSerializer): ...
```

✔ Different API responses
✔ Same underlying model
✔ Very common in real projects

---

## 11️⃣ Serializer ≠ Just Output (Important Teaser)

Serializers can also:

* Accept input data
* Validate data
* Clean data
* Replace forms for APIs

➡️ This leads to:

* `POST`
* `PUT`
* `PATCH`
* Validation errors
* Input sanitization

---

## 🧠 Big Picture Takeaway

> **ModelSerializers are the heart of Django REST Framework**

They:

* Serialize data
* Add computed fields
* Rename fields
* Control representation
* Prepare for input validation
* Scale far better than manual JSON handling

---

## ✅ In Short

* `model_to_dict` is limited
* ModelSerializer:

  * Automatically serializes models
  * Includes properties & methods
  * Supports custom fields
  * Produces clean API responses
* Serializer logic = API contract

Note - ModelForm is generally preferred for model-related forms because it follows Django's "don't repeat yourself" principle and reduces boilerplate code significantly.

---

summaries this tutorial transcript in markdown form also make note of all important pointers