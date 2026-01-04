
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

- [Serialization in django rest framework](https://chatgpt.com/share/694582f2-c308-8004-a4d2-16c111a7785d)
---

## Django REST Framework – Views, Serializers & POST Requests (Summary)

## 1. Why “Template Does Not Exist” Appears

* When visiting a DRF API endpoint in the browser, you may see:

  ```
  TemplateDoesNotExist
  ```
* **Reason**:

  * Django REST Framework (DRF) was installed, but **not added to `INSTALLED_APPS`**.
* **Fix**:

  ```python
  INSTALLED_APPS = [
      ...
      'rest_framework',
  ]
  ```
* **Result**:

  * Browser now shows the **Browsable API**, which:

    * Is better formatted
    * Allows testing APIs directly from the browser

---

## 2. Switching from GET to POST Requests

* The API view is changed to accept **POST requests only**.
* POST requests are used to:

  * Ingest data
  * Be more secure
  * Work well with JSON payloads

### Important:

* ❌ `request.POST` is **not recommended**
* ✅ Use:

  ```python
  request.data
  ```
* `request.data` works for:

  * JSON
  * Form data
  * API clients

---

## 3. CSRF Error Explained

* Error:

  ```
  Forbidden (CSRF cookie not set)
  ```
* **Why it happens**:

  * Pure Django views require CSRF protection.
* **Solution**:

  * Use **DRF API views**, which do not require CSRF tokens for API clients.

---

## 4. Echoing POST Data Back

* Initial test:

  * API simply echoes back whatever JSON is sent.
* Example payload:

  ```json
  {
    "title": "Hello World"
  }
  ```
* Confirms:

  * Data is received correctly
  * `request.data` works

---

## 5. Introducing Serializers

* Serializers are used to:

  * Validate incoming data
  * Control data structure
  * Map data to models

### Creating a Serializer Instance

```python
serializer = ProductSerializer(data=request.data)
```

### Validation

```python
if serializer.is_valid():
    data = serializer.data
```

* `serializer.data`:

  * Contains validated data
  * Matches serializer fields

---

## 6. Saving Data with `serializer.save()`

* Calling:

  ```python
  instance = serializer.save()
  ```
* This:

  * Creates a **model instance**
  * Writes data to the database

### Common Mistake

* Returning `instance` directly causes:

  ```
  Object of type Product is not JSON serializable
  ```

### Correct Approach

* Always return:

  ```python
  serializer.data
  ```

---

## 7. Serializer Method Fields & Instances

* `SerializerMethodField` assumes:

  * A **model instance exists**
* If `.save()` is NOT called:

  * There is **no instance**
  * Instance methods (e.g. `get_discount`) fail

### Error Example

```
Object has no attribute get_discount
```

### Fix (Defensive Programming)

```python
if not hasattr(obj, 'id'):
    return None
```

or

```python
if not isinstance(obj, Product):
    return None
```

✔ Prevents errors when serializer is used **without saving**

---

## 8. Validation Errors & Error Handling

### Missing Required Field

* Example: `title` missing
* Error raised:

  ```json
  {
    "title": ["This field is required."]
  }
  ```

### Invalid Field Type

* Example:

  ```json
  {
    "price": "abc123"
  }
  ```
* Error:

  ```
  Invalid number
  ```

---

## 9. `is_valid()` vs `is_valid(raise_exception=True)`

* Without exception:

  * You must manually handle errors
  * Limited feedback
* With exception:

  ```python
  serializer.is_valid(raise_exception=True)
  ```

  * Automatically returns:

    * Detailed validation errors
    * Proper HTTP 400 response

✔ Recommended for APIs

---

## 10. Key Takeaways (Very Important)

### 🔑 Core Concepts

* **DRF must be added to `INSTALLED_APPS`**
* Use **POST** for data ingestion
* Always use:

  ```python
  request.data
  ```
* **Serializers validate before models**
* `serializer.data` ≠ model instance
* `serializer.save()` creates a database record
* Serializer method fields need an **instance**
* Defensive checks prevent runtime crashes
* `raise_exception=True` gives better API errors

---

## 11. Why Views + Serializers Matter

* They are the **core of Django REST Framework**
* Together they:

  * Validate input
  * Secure APIs
  * Control data flow
  * Handle errors cleanly

---

## 1. Django Rest Framework Generics RetrieveAPIView

* Using **class-based generic views** instead of function-based views
* Implementing a **detail (single object) API endpoint**
* Understanding how **querysets**, **serializers**, and **URL lookups** work together
* Seeing how DRF automatically handles:

  * 404 errors
  * Object retrieval
  * Serialization
* Structuring URLs using `include()`
* Testing APIs using:

  * Python client
  * DRF Browsable API

The key takeaway:

> **Generic API views dramatically reduce boilerplate code while providing powerful, production-ready behavior out of the box.**

---

## 2. What Are Generic API Views?

### Definition

**Generic API Views** are **pre-built class-based views** provided by DRF that implement common API patterns like:

* Retrieve a single object
* List objects
* Create objects
* Update objects
* Delete objects

They combine:

* `APIView`
* Django ORM logic
* Serialization
* HTTP method handling

---

## 3. Key Generic View Used in the Tutorial

### `RetrieveAPIView`

Used to **fetch a single object** from the database.

### Core Responsibilities

* Fetch object using primary key (or another field)
* Serialize the object
* Return JSON response
* Automatically return `404 Not Found` if object doesn’t exist

---

## 4. Product Detail API – Core Components Explained

### 4.1 Model (Example)

```python
# products/models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

---

### 4.2 Serializer

Serializers convert model instances → JSON.

```python
# products/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

---

### 4.3 Generic API View (RetrieveAPIView)

```python
# products/views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'  # default
```

#### Important Concepts Here:

| Component          | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `RetrieveAPIView`  | Handles GET request for one object          |
| `queryset`         | Defines what data to search                 |
| `serializer_class` | Defines how data is serialized              |
| `lookup_field`     | Field used to fetch object (default = `pk`) |

---

### 4.4 URL Configuration (App Level)

```python
# products/urls.py
from django.urls import path
from .views import ProductDetailAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
]
```

#### Why `<int:pk>`?

* `pk` matches `lookup_field`
* Django passes it as a keyword argument
* DRF uses it internally to fetch the object

---

### 4.5 Main Project URLs

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
    path('products/', include('products.urls')),
]
```

This results in:

```
GET /products/1/
```

---

## 5. Automatic Features You Get for Free 🚀

Without writing any extra logic, DRF gives you:

| Feature          | Handled Automatically |
| ---------------- | --------------------- |
| Object retrieval | ✅                     |
| Serialization    | ✅                     |
| 404 response     | ✅                     |
| JSON response    | ✅                     |
| Browsable API    | ✅                     |

Example response:

```json
{
  "id": 1,
  "title": "Laptop",
  "price": "799.99"
}
```

---

## 6. Why Trailing Slashes Matter

```text
/products/1/   ✅ Works
/products/1    ❌ May fail
```

DRF expects trailing slashes by default. Consistency is important.

---

## 7. Testing the Endpoint (Python Client Example)

```python
import requests

response = requests.get("http://127.0.0.1:8000/products/1/")
print(response.json())
```

---

## 8. Function-Based Views (FBV) vs Class-Based Views (CBV)

### 8.1 Function-Based View Example

```python
# products/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)
```

#### FBV Characteristics

* Explicit logic
* Easy to understand
* More boilerplate
* Manual error handling

---

### 8.2 Class-Based Generic View Example

```python
from rest_framework import generics

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

#### CBV Characteristics

* Less code
* Reusable
* Built-in behaviors
* Easier to extend for large projects

---

## 9. FBV vs CBV – Side-by-Side Comparison

| Aspect            | Function-Based View    | Class-Based View      |
| ----------------- | ---------------------- | --------------------- |
| Code length       | Longer                 | Shorter               |
| Readability       | Simple for small logic | Cleaner for APIs      |
| Reusability       | Low                    | High                  |
| Built-in behavior | Minimal                | Extensive             |
| Error handling    | Manual                 | Automatic             |
| Best for          | Small/simple APIs      | Production-grade APIs |

---

## 10. Why Generic Views Are So Important

Generic views:

* Reduce bugs
* Improve consistency
* Enforce REST standards
* Speed up development
* Scale better for real-world APIs

They let you focus on **business logic**, not plumbing.

---

## 11. Mental Model to Remember 🧠

> **Generic API Views = Pre-written, battle-tested CRUD logic + Your models & serializers**

Once you understand:

* Querysets
* Serializers
* URL lookups

You understand **80% of DRF**.

- [APIView and GenericAPIView](https://chatgpt.com/share/6946ae0a-86b8-8004-a35b-4175896cd9cb)

- [GenericAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)

---

## 1. High-Level Summary of Django Rest Framework Generic CreateAPIView

This part of the tutorial introduces **creating data using Django REST Framework’s `CreateAPIView`**.

Key Pointers:

* Use `generics.CreateAPIView` to create database records
* Reuse the same **queryset** and **serializer**
* Configure URLs correctly (avoiding double slashes)
* Send POST requests using a Python client
* Handle serializer validation errors
* Customize object creation using `perform_create()`
* Access and modify `serializer.validated_data`
* Auto-fill or modify fields before saving
* Prepare for future enhancements like user-based data and permissions

Key takeaway:

> **`CreateAPIView` handles validation, saving, and error responses automatically — you only customize behavior when needed.**

---

## 2. CreateAPIView – What It Is

### Definition

`CreateAPIView` is a **generic class-based view** used to:

* Handle `POST` requests
* Validate incoming data
* Save a new model instance
* Return the created object as JSON
* Return validation errors automatically

---

## 3. Basic CreateAPIView Example

```python
# products/views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### Why This Works

* DRF handles `POST`
* Serializer validates input
* Object is saved automatically
* Response includes created object

---

## 4. URL Configuration – Important Detail About Slashes ⚠️

### App-level URLs

```python
# products/urls.py
from django.urls import path
from .views import ProductCreateAPIView

urlpatterns = [
    path('', ProductCreateAPIView.as_view()),
]
```

### Project-level URLs

```python
# project/urls.py
path('api/products/', include('products.urls')),
```

✅ Resulting endpoint:

```
POST /api/products/
```

❌ Avoid this mistake:

```python
path('/', ProductCreateAPIView.as_view())  # creates double slashes
```

---

## 5. Testing the Create API (Python Client)

```python
import requests

url = "http://127.0.0.1:8000/api/products/"
data = {
    "title": "New Product",
    "price": 32.99
}

response = requests.post(url, json=data)
print(response.json())
```

---

## 6. Serializer Validation Happens Automatically ✅

If required fields are missing:

```json
{
  "title": ["This field is required."]
}
```

No extra code needed.

---

## 7. Customizing Object Creation with `perform_create()`

### What Is `perform_create()`?

* A hook method called **right before saving**
* Only runs for create views
* Ideal for injecting extra data

---

## 7.1 Basic `perform_create()` Example

```python
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
```

---

## 7.2 Accessing Validated Data

```python
def perform_create(self, serializer):
    print(serializer.validated_data)
    serializer.save()
```

Example output:

```python
{
  'title': 'Test Product',
  'price': Decimal('32.99')
}
```

---

## 7.3 Modifying Data Before Save (Important Pattern)

```python
def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')

    if content is None:
        content = title

    serializer.save(content=content)
```

### Why This Is Useful

* Auto-populate fields
* Apply business rules
* Avoid duplicating logic in serializers

---

## 8. Assigning the Logged-in User (Common Real-World Use Case)

```python
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
```

Used when:

* Products belong to users
* Posts have authors
* Orders belong to customers

---

## 9. Why Not Put Logic in the Model?

This tutorial correctly hints at an important design decision:

| Approach           | When to Use            |
| ------------------ | ---------------------- |
| Model logic        | Always applied         |
| `perform_create()` | API-specific logic     |
| Django signals     | Cross-cutting concerns |

**Best practice**:

* Use `perform_create()` for API-level behavior
* Use signals for side effects (emails, logs)

---

## 10. Why Not `/create/` in the URL?

REST convention:

| Action   | Method    | URL            |
| -------- | --------- | -------------- |
| Create   | POST      | `/products/`   |
| List     | GET       | `/products/`   |
| Retrieve | GET       | `/products/1/` |
| Update   | PUT/PATCH | `/products/1/` |
| Delete   | DELETE    | `/products/1/` |

👉 **HTTP method defines the action**, not the URL name.

---

## 11. Key Important Pointers (Exam / Interview Ready)

### ✔ `CreateAPIView`:

* Handles only `POST`
* Uses `serializer_class`
* Uses `queryset` mainly for permissions

### ✔ Validation:

* Handled automatically by serializer
* Errors returned as JSON

### ✔ Customization:

* Use `perform_create()`
* Access `serializer.validated_data`
* Inject user or computed fields

### ✔ Slashes:

* Avoid double slashes
* Keep RESTful URLs clean

---

## 12. Mental Model to Remember 🧠

> **CreateAPIView = POST handler + validation + save + response**

You only step in when:

* You want to add logic
* You want to modify data
* You want to attach metadata (user, timestamps, defaults)

---

## 1. High-Level Summary of Django Rest Framework ListAPIView & ListCreateAPIView

* Create a **List API view** to fetch multiple objects
* Combine **List + Create** into a single endpoint
* Use HTTP methods (`GET`, `POST`) to control behavior
* Reuse the **same URL** for multiple actions
* Leverage the **Browsable API** for testing
* Prepare for future views like update & delete
* Understand why combining views is common in REST APIs

Key idea:

> **One endpoint can serve multiple purposes — the HTTP method determines the action.**

---

## 2. ListAPIView – Fetch All Objects

### Purpose

`ListAPIView` handles:

* `GET` requests
* Returns a list of objects
* Automatically serializes queryset

---

## 2.1 Basic ListAPIView Example

```python
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### What DRF Does Automatically

* Executes the queryset
* Serializes all objects
* Returns JSON array

Example response:

```json
[
  {
    "id": 1,
    "title": "Laptop",
    "price": "799.99"
  },
  {
    "id": 2,
    "title": "Phone",
    "price": "499.99"
  }
]
```

---

## 3. Why Not Use ListAPIView Separately?

The tutorial intentionally **does NOT use this directly** because:

* You already have a **CreateAPIView**
* Both use the same endpoint (`/products/`)
* REST prefers fewer endpoints with multiple HTTP methods

---

## 4. ListCreateAPIView – Best Practice 🚀

### What It Does

`ListCreateAPIView` combines:

* `ListAPIView` → `GET`
* `CreateAPIView` → `POST`

---

## 4.1 Combined View Example

```python
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### Behavior

| HTTP Method | Action               |
| ----------- | -------------------- |
| GET         | List all products    |
| POST        | Create a new product |

Same endpoint, different behavior.

---

## 5. URL Configuration

```python
# products/urls.py
from django.urls import path
from .views import ProductListCreateAPIView

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
]
```

### Endpoint

```
/api/products/
```

---

## 6. Testing with Python Client

### List Products (GET)

```python
import requests

response = requests.get("http://127.0.0.1:8000/api/products/")
print(response.json())
```

---

### Create Product (POST)

```python
data = {
    "title": "Keyboard",
    "price": 49.99
}

response = requests.post(
    "http://127.0.0.1:8000/api/products/",
    json=data
)
print(response.json())
```

✔ Same URL
✔ Different method
✔ Different result

---

## 7. Browsable API – Huge Productivity Boost 🧠

The DRF Browsable API lets you:

* View all listed data
* Submit POST requests via HTML form
* Test validation instantly
* Inspect permissions later

No extra setup needed.

---

## 8. Why This Design Is RESTful

❌ Bad design:

```
/products/list/
/products/create/
```

✅ Good REST design:

```
GET  /products/
POST /products/
```

Action = HTTP verb
Resource = URL

---

## 9. Preparing for Update & Delete Views

Next logical views:

| View                         | Purpose                |
| ---------------------------- | ---------------------- |
| UpdateAPIView                | Modify existing object |
| DestroyAPIView               | Delete object          |
| RetrieveUpdateDestroyAPIView | Combine all            |

Example:

```python
class ProductRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

## 10. Permissions & User-Based Behavior (Preview)

Later, you can control:

* Who can list
* Who can create
* Who can update/delete

Example:

```python
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]
```

---

## 11. Important Pointers (Must Remember)

### ✔ ListAPIView

* Handles `GET`
* Returns multiple objects
* Serializer uses `many=True` automatically

### ✔ ListCreateAPIView

* Combines listing & creating
* Uses same endpoint
* REST best practice

### ✔ Browsable API

* Enabled by default
* Great for debugging
* Shows allowed methods

### ✔ Combining Views

* Reduces endpoint clutter
* Improves consistency
* Easier permission handling

---

## 12. Mental Model 🧠

> **One URL = One resource
> HTTP method = Action on that resource**

DRF generic views implement this philosophy perfectly.

Run Sqlite DB - `sqlite3 backend/db.sqlite3 "SELECT id,title,content,price FROM products_product;"`

---

## 1. High-Level Summary of Using Function Based Views For Create Retrieve or List

It demonstrates how **Create, Retrieve, and List API behavior** can be implemented using **a single Function-Based View**, instead of multiple generic class-based views.

* Use `@api_view` to enable HTTP methods in FBVs
* Branch logic based on `request.method`
* Handle **GET (list + detail)** and **POST (create)** in one function
* Use URL keyword arguments (`pk`) to distinguish list vs detail
* Manually serialize querysets and single objects
* Handle 404 errors using `get_object_or_404` or `Http404`
* Replicate `perform_create()` logic inside FBVs
* Test endpoints using the same client scripts
* Understand **why this approach becomes confusing at scale**

Key lesson:

> **Just because you *can* put everything into one FBV doesn’t mean you *should*.**

---

## 2. The Goal of This Section

The instructor is **not recommending** this approach.

Instead, the goal is to:

* Show **what DRF generic views are doing behind the scenes**
* Illustrate how HTTP methods map to actions
* Demonstrate why generic views exist

---

## 3. Single Function-Based View for CRUD (List, Retrieve, Create)

## 3.1 Required Imports

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
```

---

## 3.2 Function-Based “All-in-One” View

```python
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None):
    # CREATE
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # LIST or RETRIEVE
    if request.method == 'GET':
        if pk is not None:
            # DETAIL VIEW
            obj = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(obj)
            return Response(serializer.data)
        else:
            # LIST VIEW
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
```

---

## 4. How the Logic Works

### HTTP Method Determines Action

| Method      | Behavior             |
| ----------- | -------------------- |
| GET + no pk | List all products    |
| GET + pk    | Retrieve one product |
| POST        | Create a new product |

### URL Determines Context

```python
path('products/', product_alt_view),
path('products/<int:pk>/', product_alt_view),
```

---

## 5. Handling 404 Errors

### Option 1: `get_object_or_404` (Recommended)

```python
obj = get_object_or_404(Product, pk=pk)
```

Automatically raises a proper 404 response.

---

### Option 2: Manual 404

```python
from django.http import Http404

try:
    obj = Product.objects.get(pk=pk)
except Product.DoesNotExist:
    raise Http404
```

Both work, but `get_object_or_404` is cleaner.

---

## 6. Serializer Usage in FBVs

### List Serialization

```python
serializer = ProductSerializer(queryset, many=True)
```

### Detail Serialization

```python
serializer = ProductSerializer(obj)
```

### Create Serialization

```python
serializer = ProductSerializer(data=request.data)
```

This is exactly what generic views automate for you.

---

## 7. Replicating `perform_create()` in FBVs

```python
serializer = ProductSerializer(data=request.data)
if serializer.is_valid():
    serializer.save()
```

Custom logic example:

```python
if serializer.is_valid():
    title = serializer.validated_data.get('title')
    serializer.save(content=title)
```

---

## 8. Testing All Scenarios

| Client Script  | Expected Result   |
| -------------- | ----------------- |
| `detail.py`    | Retrieve product  |
| `list.py`      | List all products |
| `create.py`    | Create product    |
| `not_found.py` | 404 response      |

Everything works — **but readability suffers**.

---

## 9. Why This Approach Is Problematic ⚠️

### The View Becomes Confusing

```text
If method == GET
   If pk exists
      Do X
   Else
      Do Y
Else if POST
   Do Z
```

Hard to:

* Read
* Maintain
* Debug
* Extend
* Share with team members

---

## 10. Why Generic Views Are Better ✅

### Generic View Equivalent

```python
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

```python
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### Instantly Understandable

* You know what the view does by its name
* No conditional logic
* Fewer bugs
* Easier collaboration

---

## 11. FBV vs Generic CBV (Reality Check)

| Feature       | FBV                 | Generic CBV |
| ------------- | ------------------- | ----------- |
| Flexibility   | High                | High        |
| Boilerplate   | High                | Low         |
| Readability   | Low (complex views) | High        |
| Scalability   | Poor                | Excellent   |
| Best Use Case | Small logic         | CRUD APIs   |

---

## 12. When FBVs Still Make Sense

FBVs are still great for:

* Non-CRUD endpoints
* Custom logic-heavy endpoints
* One-off APIs
* Webhooks
* Integration callbacks

---

## 13. Mental Model 🧠

> **FBVs show *how* things work**
> **Generic CBVs show *what* the endpoint does**

Learn FBVs → Understand DRF
Use Generic CBVs → Build production APIs

---

## 14. Final Takeaway

* This “alt view” is educational, not recommended
* Generic views reduce confusion
* Consistent patterns scale better
* DRF’s power is in its abstractions

---

## 1️⃣ UpdateAPIView & DestroyAPIView

So far, you’ve implemented:

* **Create** → `CreateAPIView`
* **List** → `ListAPIView`
* **Retrieve (Detail)** → `RetrieveAPIView`

In this section, the tutorial covers the remaining **CRUD operations**:

* **Update** → `UpdateAPIView`
* **Delete** → `DestroyAPIView`

Once these are done, you have **full CRUD support**:

> **C**reate
> **R**etrieve
> **U**pdate
> **D**estroy

⚠️ Important note from the tutorial:

> CRUD works, but **there is no authentication or permission control yet** — meaning *anyone can update or delete anything*.
> This will be fixed later using **authentication & permissions**.

---

## 2️⃣ UpdateAPIView – Core Idea

### What does `UpdateAPIView` do?

* Updates **an existing object**
* Uses HTTP methods:

  * `PUT` → full update
  * `PATCH` → partial update
* Works almost **identically to `RetrieveAPIView`**
* Requires:

  * `queryset`
  * `serializer_class`
  * `lookup_field` (usually `id`)

---

## 3️⃣ UpdateAPIView – Key Concepts Explained

### 🔹 lookup_field

This tells DRF **how to find the object**.

```python
lookup_field = "id"
```

So this URL:

```
/api/products/5/update/
```

means:

> Update the product where `id = 5`

---

### 🔹 perform_update()

This method is **optional**, but very powerful.

It runs **after serializer validation** and **before response is returned**.

Use it when:

* You want to modify data before saving
* You want side effects (logging, auto-filling fields, etc.)

---

## 4️⃣ Basic UpdateAPIView Example

### `views.py`

```python
from rest_framework.generics import UpdateAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def perform_update(self, serializer):
        instance = serializer.save()

        # Custom logic
        if not instance.content:
            instance.content = instance.title
            # No need to call instance.save()
            # serializer.save() already saved it
```

---

### `urls.py`

```python
from django.urls import path
from .views import ProductUpdateAPIView

urlpatterns = [
    path("products/<int:id>/update/", ProductUpdateAPIView.as_view()),
]
```

---

### 🔹 How the update request works

```http
PUT /api/products/5/update/
```

```json
{
  "title": "Macbook M5 Pro",
  "content": "this is latest series in Macbook series M5 pro",
  "price": 198.65
}
```

✅ Updates only the provided fields
✅ Returns updated JSON data

---

## 5️⃣ DestroyAPIView – Core Idea

### What does `DestroyAPIView` do?

* Deletes an existing object
* Uses HTTP method:

  * `DELETE`
* Returns:

  * **HTTP 204 No Content** (no JSON body)

---

## 6️⃣ DestroyAPIView – Key Concepts Explained

### 🔹 perform_destroy()

Runs **right before deletion**.

Use it if:

* You want to log deletions
* Clean up related data
* Trigger analytics/events

---

## 7️⃣ Basic DestroyAPIView Example

### `views.py`

```python
from rest_framework.generics import DestroyAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        # Custom logic before delete
        print(f"Deleting product: {instance.title}")

        # Actually delete the object
        super().perform_destroy(instance)
```

---

### `urls.py`

```python
from django.urls import path
from .views import ProductDestroyAPIView

urlpatterns = [
    path("products/<int:id>/delete/", ProductDestroyAPIView.as_view()),
]
```

---

### 🔹 How the delete request works

```http
DELETE /api/products/10/delete/
```

**Response**

```
204 No Content
```

✔️ Object is permanently deleted
✔️ No JSON response (important!)

---

## 8️⃣ Common Mistakes Highlighted in the Tutorial

### ❌ Wrong endpoint

Using `/detail/` instead of `/update/` or `/delete/`

→ Results in:

```
PUT method not allowed
DELETE method not allowed
```

✔️ Fix: Ensure the correct URL is used

---

### ❌ Expecting JSON on DELETE

DELETE returns **204**, not JSON

✔️ Fix:

* Check status code instead of response body

---

## 9️⃣ Important Takeaways (Very Important)

### ✅ Update & Destroy views:

* Are **nearly identical to Detail views**
* Differ mainly by:

  * HTTP method
  * Behavior (save vs delete)

---

### ⚠️ Major Security Warning

At this stage:

* ❌ No authentication
* ❌ No permissions
* ❌ Anyone can update/delete anything

➡️ **Never ship this to production**

---

## 10️⃣ Mental Model (Easy to Remember)

| Action | DRF View Class    | HTTP Method |
| ------ | ----------------- | ----------- |
| List   | `ListAPIView`     | GET         |
| Create | `CreateAPIView`   | POST        |
| Detail | `RetrieveAPIView` | GET         |
| Update | `UpdateAPIView`   | PUT/PATCH   |
| Delete | `DestroyAPIView`  | DELETE      |

---

## 1️⃣ Mixins and a Generic API View

Up to now, you used **ready-made generic views** like:

* `ListAPIView`
* `CreateAPIView`
* `RetrieveAPIView`
* `UpdateAPIView`
* `DestroyAPIView`

In this section, the tutorial explains:

> **Those views are just combinations of *mixins* + `GenericAPIView`.**

So the goal is to:

* Understand **mixins**
* Understand **GenericAPIView**
* Manually recreate list / detail / create behavior
* Learn *how DRF maps HTTP methods to logic*

This gives you **deep control** and **better debugging ability** later.

---

## 2️⃣ GenericAPIView – Core Concept

### What is `GenericAPIView`?

It is:

* The **base class** for most DRF generic views
* Provides:

  * `queryset`
  * `serializer_class`
  * `lookup_field`
  * `get_queryset()`
  * `get_serializer()`

❌ By itself, it **does nothing**
✅ Mixins add actual behavior

---

### Minimal GenericAPIView

```python
from rest_framework.generics import GenericAPIView

class MyView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

👉 This alone will **not respond to GET/POST**
You must define HTTP methods (`get`, `post`, etc.)

---

## 3️⃣ What Are Mixins?

### Mixins = Reusable behavior blocks

DRF provides mixins like:

* `ListModelMixin`
* `CreateModelMixin`
* `RetrieveModelMixin`
* `UpdateModelMixin`
* `DestroyModelMixin`

Each mixin adds **one method**:

| Mixin              | Method Provided |
| ------------------ | --------------- |
| ListModelMixin     | `list()`        |
| CreateModelMixin   | `create()`      |
| RetrieveModelMixin | `retrieve()`    |
| UpdateModelMixin   | `update()`      |
| DestroyModelMixin  | `destroy()`     |

⚠️ Mixins **do not map to HTTP methods**
You must call them yourself.

---

## 4️⃣ Key Difference: Function-Based vs Class-Based Views

### Function-Based View

```python
def product_view(request):
    if request.method == "GET":
        ...
    elif request.method == "POST":
        ...
```

### Class-Based View (DRF)

```python
class ProductView(GenericAPIView):
    def get(self, request):
        ...
    
    def post(self, request):
        ...
```

✔ No `if request.method == ...`
✔ One method per HTTP verb

---

## 5️⃣ List View Using Mixins (GET)

### Step 1: Import mixins + GenericAPIView

```python
from rest_framework import generics, mixins
```

### Step 2: Create List View

```python
class ProductMixinView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
```

### What’s happening?

* `ListModelMixin` provides `.list()`
* `get()` calls that method
* DRF handles serialization automatically

---

## 6️⃣ Important Pointer: Serializer Error

❌ Wrong:

```python
serializer = ProductSerializer
```

✅ Correct:

```python
serializer_class = ProductSerializer
```

If missing:

```
AssertionError: You must define serializer_class
```

---

## 7️⃣ Mapping Any HTTP Method You Want

Because **you control the method**, you can do this:

```python
def post(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
```

⚠️ Now:

* `POST` → lists data
* `GET` → method not allowed

📌 This demonstrates how **flexible CBVs are**.

---

## 8️⃣ lookup_field – When It Matters

```python
lookup_field = "pk"
```

### Important:

* `ListModelMixin` ❌ does NOT use `lookup_field`
* `RetrieveModelMixin` ✅ DOES use it

So:

* You don’t need `lookup_field` for lists
* You do need it for detail views

---

## 9️⃣ List + Detail in One View (GET)

### Add RetrieveModelMixin

```python
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
```

### Result:

| URL            | Result |
| -------------- | ------ |
| `/products/`   | List   |
| `/products/3/` | Detail |

✔ One view
✔ Two behaviors

---

## 🔍 Why kwargs Matter

When URL is:

```python
path("products/<int:pk>/", ProductMixinView.as_view())
```

DRF passes:

```python
kwargs = {"pk": 3}
```

That’s how `retrieve()` finds the object.

---

## 10️⃣ Adding Create Support (POST)

### Add CreateModelMixin

```python
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

✔ POST now creates data
✔ No serializer logic written manually

---

## 11️⃣ perform_create Still Works!

```python
def perform_create(self, serializer):
    instance = serializer.save()
    if not instance.content:
        instance.content = "This is a single view doing cool stuff"
```

📌 Why?
Because `CreateModelMixin.create()` internally calls:

```python
self.perform_create(serializer)
```

So **hooks still apply**.

---

## 12️⃣ How Generic Views Are Built (Big Reveal)

### Example:

```python
class CreateAPIView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    pass
```

👉 That’s literally how DRF does it.

Same for:

* `ListCreateAPIView`
* `RetrieveUpdateDestroyAPIView`

---

## 13️⃣ Why You Usually Should NOT Do This in Production

The tutorial clearly says:

❌ This becomes **convoluted**
❌ Harder to read
❌ Harder to maintain

✅ Best practice:

* Use **built-in generic views**
* Use mixins only when:

  * You need custom behavior
  * You want deep control

---

## 14️⃣ Key Takeaways (Very Important)

### ✅ What You Learned

* Generic views = **Mixins + GenericAPIView**
* Mixins provide behavior
* HTTP methods decide what runs
* `perform_create`, `perform_update`, `perform_destroy` still work
* DRF generic views are **not magic**

---

### 🧠 Mental Model

```
HTTP Method → CBV Method → Mixin Method → Serializer → Response
```

- [Mixins](https://www.django-rest-framework.org/api-guide/generic-views/#mixins)

---

## 1️⃣ Big Picture: Session Authentication & Permissions

### Authentication

👉 **Who are you?**
Example: logged-in user, admin, anonymous user

### Permissions

👉 **What are you allowed to do?**
Example: read only, create, update, delete

📌 **Permissions always depend on authentication**

---

## 2️⃣ Why This Matters

Before this:

* Anyone could:

  * Create products
  * Update products
  * Delete products

❌ That’s dangerous
✅ We now **lock things down**

---

## 3️⃣ Permission Classes (First Concept)

DRF allows permissions on **generic views** very easily.

### Import

```python
from rest_framework import permissions
```

---

## 🔹 IsAuthenticated

```python
permission_classes = [permissions.IsAuthenticated]
```

### Behavior

| User      | Result      |
| --------- | ----------- |
| Logged in | ✅ Allowed   |
| Anonymous | ❌ 401 / 403 |

### Example View

```python
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### Result

* Browser (not logged in): ❌
* API client (no auth): ❌
* Logged-in admin user: ✅

---

## 🔹 IsAuthenticatedOrReadOnly (Very Common)

```python
permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

### Meaning

| HTTP Method | Allowed?    |
| ----------- | ----------- |
| GET         | ✅ Anyone    |
| POST        | ❌ Anonymous |
| PUT         | ❌ Anonymous |
| DELETE      | ❌ Anonymous |

### Why it’s useful

* Public data
* Protected writes

### Example

```python
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

### Result

* GET `/products/` → works
* POST `/products/` → ❌ unless logged in

---

## 4️⃣ Understanding Status Codes (Important Detail)

| Status Code | Meaning                 |
| ----------- | ----------------------- |
| 401 / 403   | Permission denied       |
| 405         | HTTP method not allowed |

📌 Example:

* `POST` on ListAPIView → 405 (view doesn’t support POST)
* `POST` with no auth → 403 (permission denied)

This distinction is **very important** for API clients.

---

## 5️⃣ Authentication Classes (Second Concept)

Permissions check **who is authenticated**, but authentication defines **how**.

### Import

```python
from rest_framework import authentication
```

---

## 🔹 SessionAuthentication

```python
authentication_classes = [authentication.SessionAuthentication]
```

### What it uses

* Django login session
* Cookies
* CSRF protection

### Typical Use Case

✔ Traditional Django apps
✔ Django Admin
✔ React / JS frontend served by Django

---

### Full Example View

```python
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

---

## 6️⃣ Why Browser Works but API Client Doesn’t

### Browser (Browsable API)

* You logged into `/admin`
* Django created a session
* Session cookie is sent automatically
* ✅ Authenticated

### Python API Client

* No session
* No cookies
* ❌ Anonymous

That’s why:

```
Authentication credentials were not provided
```

📌 **Nothing is wrong** — this is expected.

---

## 7️⃣ Creating a Superuser (Demo Purpose)

```bash
python manage.py createsuperuser
```

Once logged in:

* Browsable API shows:

  * Logged-in user
  * POST form enabled
* You can create objects visually

---

## 8️⃣ When SessionAuthentication Makes Sense

✅ Best for:

* Django + React
* Django + templates
* Internal admin dashboards

❌ Not ideal for:

* Mobile apps
* External APIs
* Python scripts
* Third-party consumers

📌 Why?
Because sessions require:

* Cookies
* Browser-like behavior

---

## 9️⃣ Why Your Python Client Still Fails

```python
requests.post("http://localhost:8000/api/products/")
```

❌ No session
❌ No cookies
❌ Not logged in

✔ Works only if:

* You manually handle cookies
* Or use browser automation (Selenium)

---

## 🔑 Key Insight

> **Session authentication is browser-first authentication**

For real APIs, we usually want:

* Token authentication
* JWT authentication

That’s exactly what comes next.

---

## 10️⃣ Summary of Built-In Permissions (Must Remember)

| Permission                | Use Case                   |
| ------------------------- | -------------------------- |
| AllowAny                  | Public API                 |
| IsAuthenticated           | Private API                |
| IsAdminUser               | Admin-only                 |
| IsAuthenticatedOrReadOnly | Public read, private write |
| DjangoModelPermissions    | Model-based access         |

---

## 11️⃣ Key Takeaways (Exam / Interview Ready)

✅ Permissions decide **what you can do**
✅ Authentication decides **who you are**
✅ SessionAuthentication uses Django login
✅ Browsable API auto-uses sessions
✅ API clients need token-based auth

- [Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

---

## Django User & Group Permissions with `DjangoModelPermissions` 

## 1. Big Picture: User & Group Permissions with DjangoModelPermissions

The tutorial shows:

* How **Django’s built-in model permissions** work
* How **users vs groups** affect permissions
* How **Django Admin permissions ≠ DRF API permissions**
* Why **`DjangoModelPermissions` alone is not enough**
* Why we eventually need **custom permissions**

---

## 2. Django Model Permissions (Auto-Created)

For every Django model, Django automatically creates **4 permissions**:

| Permission | Codename           |
| ---------- | ------------------ |
| Add        | `add_modelname`    |
| Change     | `change_modelname` |
| Delete     | `delete_modelname` |
| View       | `view_modelname`   |

Example for `Product` model:

```
add_product
change_product
delete_product
view_product
```

These permissions are:

* Stored in the database
* Used by **Django Admin**
* Can be assigned to **users or groups**

---

## 3. Users vs Groups (Very Important)

### Two Ways Permissions Can Be Given

1. **Directly to a User**
2. **Via a Group the User Belongs To**

Permissions are **additive**:

> User permissions + Group permissions = final permissions

### Best Practice

✅ **Use groups**
❌ Avoid assigning permissions directly to users

---

## 4. Admin Example (What the Tutorial Did)

### Step 1: Create a Staff User

* `is_staff = True`
* Not a superuser

Result:
❌ Cannot see any models in admin

---

### Step 2: Give `view_product` Permission

Admin → User → Permissions → `Can view product`

Result:
✅ User can **see products**
❌ Cannot edit / delete

Admin shows **read-only view**

---

### Step 3: Create Group: `staff_product_editor`

Permissions given to group:

* `view_product`
* `add_product`
* `change_product`

User added to this group.

Result:
✅ User can view, add, edit products
❌ Still not a superuser

---

## 5. Bringing This Into DRF (API Side)

### Initial API View

```python
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
```

🔴 Problem:

* Any authenticated user can POST
* Permissions are **not tied to Django model permissions**

---

## 6. Using `DjangoModelPermissions`

### Change Permission Class

```python
from rest_framework.permissions import DjangoModelPermissions

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]
```

### What This Does

DRF now checks permissions based on HTTP method:

| HTTP Method | Required Permission         |
| ----------- | --------------------------- |
| GET         | ❌ **No permission checked** |
| POST        | `add_product`               |
| PUT/PATCH   | `change_product`            |
| DELETE      | `delete_product`            |

---

## 7. 🔥 Critical Issue Discovered in Tutorial

### Scenario

Staff user has:
❌ NO `view_product` permission

Yet:

```http
GET /api/products/
```

👉 **Still returns all products**

### Why?

Because:

* `GET`, `HEAD`, `OPTIONS` are considered **SAFE METHODS**
* `DjangoModelPermissions` **does NOT check `view_*` permission**
* It only protects **write operations**

This is default DRF behavior.

---

## 8. Another Big Gotcha: Permissions Are Per-View

### What Went Wrong?

* List view had `DjangoModelPermissions`
* Update view **did NOT**

So user could:
❌ Edit product via API
❌ Even though admin blocked it

### Lesson

> **Permissions must be applied to EVERY view**

---

## 9. Why `view_model` Permission Is Ignored by Default

DRF assumes:

* Reading data is public unless restricted
* Model permissions exist mainly for **mutations**

So:

* `view_product` is ignored unless you explicitly enforce it

---

## 10. Why Custom Permissions Are Needed

### Problems with `DjangoModelPermissions`

1. ❌ GET requests not protected
2. ❌ `view_model` permission ignored
3. ❌ Easy to forget permissions on some views
4. ❌ API behavior doesn’t match Admin behavior

---

## 11. Custom Permission (Basic Example)

### Goal

Require:

* `view_product` for GET
* `add_product` for POST
* `change_product` for PUT/PATCH
* `delete_product` for DELETE

---

### Custom Permission Class

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS

class ProductPermissions(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return user.has_perm("products.view_product")

        if request.method == "POST":
            return user.has_perm("products.add_product")

        if request.method in ["PUT", "PATCH"]:
            return user.has_perm("products.change_product")

        if request.method == "DELETE":
            return user.has_perm("products.delete_product")

        return False
```

---

### Apply It to Views

```python
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermissions]
```

Now:

* API behavior matches admin behavior ✅
* No accidental data leaks ✅

---

## 12. Key Takeaways (Exam / Interview Ready)

### ✅ Django Model Permissions

* Auto-created per model
* Used by Admin
* Can be reused in DRF

### ✅ DjangoModelPermissions

* Protects **write operations only**
* Ignores `view_model`
* Must be applied per-view

### ❌ Common Mistakes

* Forgetting permissions on update/delete views
* Assuming admin permissions apply to API
* Relying only on `IsAuthenticated`

### ✅ Best Practice

* Use **groups**
* Create **custom permission classes**
* Apply permissions **globally or consistently**
* Explicitly protect GET if data is sensitive

- [DjangoModelPermissions](https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions)

---

## Custom Permissions in Django REST Framework

## 1. What Problem Are We Solving?

### The core issue:

* In **Django Admin**, a staff user with no permissions:

  * ❌ Cannot view products
  * ❌ Cannot edit products
* In **DRF API**, the same user:

  * ✅ Can still `GET /api/products/`
  * ❌ Might not be able to edit — but **can still see everything**

👉 **Admin permissions ≠ API permissions**

This mismatch is dangerous.

---

## 2. Why `DjangoModelPermissions` Is Not Enough

By default, `DjangoModelPermissions`:

| HTTP Method | Permission Checked |
| ----------- | ------------------ |
| GET         | ❌ none             |
| POST        | `add_model`        |
| PUT / PATCH | `change_model`     |
| DELETE      | `delete_model`     |

### Result:

* Users without `view_model` can still **read data**
* This is why your staff user could still see all products

👉 **We need to enforce `view_model` permission**

---

## 3. What Are Custom Permissions in DRF?

A **custom permission** is a class that decides:

> “Should this user be allowed to do this action?”

You implement one (or both) of these methods:

```python
has_permission(self, request, view)         # view-level
has_object_permission(self, request, view, obj)  # object-level
```

---

## 4. Examples from DRF Docs (Conceptual)

### Blocklist Permission (IP-based)

```python
class BlocklistPermission(BasePermission):
    def has_permission(self, request, view):
        return request.META["REMOTE_ADDR"] not in BLOCKED_IPS
```

### Owner-Only Editing

```python
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
```

👉 These examples show:

* **Global rules** → `has_permission`
* **Object-specific rules** → `has_object_permission`

---

## 5. Creating Our Custom Permission (Tutorial Path)

### Step 1: Create `permissions.py`

```python
# products/permissions.py
from rest_framework.permissions import DjangoModelPermissions
```

---

### Step 2: Extend `DjangoModelPermissions`

Why?

* It already knows how to check:

  * `add`
  * `change`
  * `delete`
* We just want to **add `view` permission support**

```python
class IsStaffEditorPermission(DjangoModelPermissions):
    pass
```

---

## 6. Understanding Permission Strings (Very Important)

Format:

```
app_label.action_modelname
```

Examples for `Product` model in `products` app:

```text
products.view_product
products.add_product
products.change_product
products.delete_product
```

---

## 7. The Initial (Wrong) Custom Permission Attempt

### ❌ What went wrong:

```python
if user.has_perm("products.view_product"):
    return True

if user.has_perm("products.change_product"):
    return True
```

### Why this fails:

* If **any permission** is true → everything becomes allowed
* A user with `view_product` could edit products 😬

👉 **Permissions must be tied to HTTP methods**

---

## 8. The Correct Way: Override `perms_map`

This is the **key lesson** of the tutorial.

### Default `DjangoModelPermissions` mapping (simplified):

```python
perms_map = {
    "POST": ["%(app_label)s.add_%(model_name)s"],
    "PUT": ["%(app_label)s.change_%(model_name)s"],
    "PATCH": ["%(app_label)s.change_%(model_name)s"],
    "DELETE": ["%(app_label)s.delete_%(model_name)s"],
}
```

### It does NOT include `GET`

---

## 9. Custom Permission That FIXES Everything

### ✅ Final Custom Permission Class

```python
from rest_framework.permissions import DjangoModelPermissions

class IsStaffEditorPermission(DjangoModelPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    def has_permission(self, request, view):
        # Must be staff
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
```

### What this achieves:

* GET → requires `view_product`
* POST → requires `add_product`
* PUT/PATCH → requires `change_product`
* DELETE → requires `delete_product`
* Non-staff users → ❌ denied

✅ Admin and API behavior now match

---

## 10. Applying the Permission to Views

```python
from .permissions import IsStaffEditorPermission

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffEditorPermission]
```

---

## 11. Combining Permissions (Very Important)

### Example:

```python
permission_classes = [
    permissions.IsAdminUser,
    IsStaffEditorPermission
]
```

### Rules:

* Permissions are evaluated **top to bottom**
* First failure = request denied

👉 Ordering matters!

---

## 12. Staff vs Admin (Clarified)

| Role           | Meaning                         |
| -------------- | ------------------------------- |
| `is_staff`     | Can access admin (if permitted) |
| `is_superuser` | Bypasses all permission checks  |
| `IsAdminUser`  | Checks `is_staff=True`          |

---

## 13. Why the API Client (Python `requests`) Failed

```python
client.get("/api/products/")
```

❌ Failed because:

* API now requires authentication
* No token / session provided

👉 This sets up the **next topic: Token Authentication**

---

## 14. Key Takeaways (Interview-Ready)

### ✅ Core Lessons

* Django Admin permissions do NOT protect APIs
* `DjangoModelPermissions` ignores `view_model`
* Always enforce permissions per HTTP method
* Extend built-in permissions — don’t reinvent them
* Use **least privilege** by default

### ❌ Common Mistakes

* Assuming GET is safe
* Forgetting permission ordering
* Writing `has_permission` without method checks
* Giving users direct permissions instead of groups

---

## 15. Mental Model (One Line)

> **Authentication answers “who are you?”
> Permissions answer “what are you allowed to do?”**

- What it is: owner = models.ForeignKey(User) declares a many-to-one DB relationship where each model instance references one User, and a User can own many instances.

- Note - user.is_staff is a boolean field on Django's User model that marks whether the account is allowed access to admin/staff-only areas — it is defined by Django (on AbstractUser) not by DRF.

- [Custom permissions](https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions)

---

## Token Authentication in Django REST Framework

## 1. Why Token Authentication Is Needed

### Problem recap

* **Session Authentication** works only for:

  * Browsers
  * Django Admin
  * Same-site JavaScript (React, etc.)
* ❌ Python clients (`requests`, scripts, mobile apps) **cannot reuse browser sessions**

👉 **Token Authentication** allows **any external client** to securely talk to your API.

---

## 2. What Is Token Authentication?

* Server issues a **unique token** to a user after login
* Client sends that token with every request
* Server validates token → identifies user → checks permissions

### Mental model:

```
username + password  →  token
token → access API
```

---

## 3. Enable Token Authentication in Django

### Step 1: Install app

```python
# settings.py
INSTALLED_APPS = [
    ...
    "rest_framework",
    "rest_framework.authtoken",
]
```

### Step 2: Run migrations

```bash
python manage.py migrate
```

This creates a `Token` table in the database.

---

## 4. Token Model (Important Insight)

Each token record contains:

* `key` → actual token string
* `user` → linked user
* `created` → timestamp

```python
from rest_framework.authtoken.models import Token

Token.objects.all()
```

👉 Tokens **do not expire by default**

---

## 5. Create an API Endpoint to Generate Tokens

### Add token endpoint in `urls.py`

```python
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api/auth/", obtain_auth_token),
]
```

### How it works:

* Accepts `username` + `password`
* Returns a token

Example response:

```json
{
  "token": "abc123xyz..."
}
```

---

## 6. Protect API Views with TokenAuthentication

### Update your API view

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductListCreateView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
```

Now:

* ❌ No token → access denied
* ✅ Valid token → access granted

---

## 7. Python Client: Authenticating with Token

### Step 1: Get credentials securely

```python
from getpass import getpass
import requests

username = input("Username: ")
password = getpass("Password: ")
```

---

### Step 2: Request a token

```python
auth_url = "http://localhost:8000/api/auth/"

auth_response = requests.post(auth_url, data={
    "username": username,
    "password": password
})

token = auth_response.json()["token"]
```

---

### Step 3: Send token in headers

```python
headers = {
    "Authorization": f"Token {token}"
}

response = requests.get(
    "http://localhost:8000/api/products/",
    headers=headers
)

print(response.json())
```

✅ Your Python client is now authenticated

---

## 8. Why Tokens Don’t Change Every Login

* Tokens are **persistent**
* Same user → same token (unless deleted)

### Pros

* Simple
* Fast
* Stateless

### Cons

* No automatic expiration
* Must be manually revoked

---

## 9. Revoking Tokens (Logout)

### Delete token manually

```python
Token.objects.filter(user=user).delete()
```

Effect:

* Token immediately becomes invalid
* Client must log in again

API response:

```json
{
  "detail": "Invalid token."
}
```

---

## 10. Token Expiration (Advanced Concept)

DRF tokens **do not expire by default**, but you can:

### Option 1: Cron / Celery job

```python
Token.objects.filter(
    created__lt=timezone.now() - timedelta(days=7)
).delete()
```

### Option 2: Custom Token Model

* Add `expires` field
* Validate expiration on each request

### Option 3: Third-party packages

* `djangorestframework-simplejwt`
* OAuth2 providers

---

## 11. Using `Bearer` Instead of `Token`

### Why?

Industry standard header:

```
Authorization: Bearer <token>
```

---

### Custom Token Authentication

```python
# api/authentication.py
from rest_framework.authentication import TokenAuthentication

class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"
```

---

### Use it in views

```python
from api.authentication import BearerTokenAuthentication

class ProductListCreateView(ListCreateAPIView):
    authentication_classes = [BearerTokenAuthentication]
```

---

### Python client change

```python
headers = {
    "Authorization": f"Bearer {token}"
}
```

✅ Same token, different keyword

---

## 12. How Token Authentication Fits with Permissions

Flow for **every request**:

```
1. Authentication (Who are you?)
2. Permission checks (What can you do?)
3. View logic runs
```

Example:

* Token valid → user identified
* Permission class checks:

  * `is_staff`
  * `view_product`
* Request allowed or denied

---

## 13. Security Best Practices (Important)

✅ Use HTTPS always
✅ Store tokens securely (env, vault, keychain)
✅ Rotate tokens for sensitive access
✅ Delete tokens on logout
❌ Never hardcode tokens
❌ Never log tokens

---

## 14. When to Use Which Authentication

| Use case               | Best choice           |
| ---------------------- | --------------------- |
| Django Admin / Browser | SessionAuthentication |
| Python scripts         | TokenAuthentication   |
| Mobile apps            | Token / JWT           |
| Third-party APIs       | Token / OAuth         |
| Large systems          | JWT / OAuth2          |

---

## 15. Key Takeaways (Exam / Interview Ready)

* Token Authentication enables **stateless API access**
* Tokens identify users, not sessions
* Tokens must be sent in `Authorization` header
* Tokens don’t expire by default
* Permissions still apply after authentication
* You can customize:

  * Token header keyword
  * Expiry logic
  * Storage model

---

## 16. One-Line Summary

> **Session auth is for browsers.
> Token auth is for APIs.**

---

## Default Django REST Framework Settings

*(Authentication, Permissions, Overrides, Throttling)*

## 1. Why Default DRF Settings Exist

### The problem

In many views you keep writing:

```python
authentication_classes = [...]
permission_classes = [...]
```

This leads to:

* Repetition
* Mistakes
* Inconsistent security

### The solution

👉 **Define global defaults in `settings.py`**
So every API view:

* Uses the same authentication
* Uses the same permission rules
* Can override only when needed

---

## 2. Where Defaults Are Defined

In **`settings.py`**

```python
REST_FRAMEWORK = {
    ...
}
```

This dictionary controls:

* Authentication
* Permissions
* Throttling
* Renderers
* Parsers

---

## 3. Default Authentication Classes

### What are Authentication Classes?

They answer:

> **Who is the user making this request?**

Examples:

* SessionAuthentication (browser)
* TokenAuthentication (API clients)

---

### Setting Default Authentication

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "api.authentication.TokenAuthentication",
    ],
}
```

### Important points

* You **do not import classes**
* You provide **Python paths as strings**
* These apply to **all API views automatically**

---

## 4. Default Permission Classes

### What are Permission Classes?

They answer:

> **Is this user allowed to do this action?**

---

### Common permissions

| Permission                  | Meaning                          |
| --------------------------- | -------------------------------- |
| `AllowAny`                  | Anyone can access                |
| `IsAuthenticated`           | Must be logged in                |
| `IsAuthenticatedOrReadOnly` | Read = anyone, Write = logged-in |

---

### Setting Default Permissions

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}
```

### What this means

* `GET` → public
* `POST`, `PUT`, `DELETE` → authenticated users only

---

## 5. Effect on API Views (Very Important)

### Before (repetitive)

```python
class ProductListAPIView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
```

---

### After (clean)

```python
class ProductListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
```

✅ Authentication comes from **settings.py**
✅ View only specifies **what is different**

---

## 6. View-Level Override Rule (Golden Rule)

> **View settings always override global defaults**

---

### Example: Override permissions

```python
class PublicAPIView(APIView):
    permission_classes = []
```

Result:

* No permissions
* Fully public

---

### Override authentication

```python
class TokenOnlyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
```

Result:

* Ignores SessionAuthentication
* Uses TokenAuthentication only

---

## 7. Empty Lists Are Dangerous (Important Warning ⚠️)

```python
permission_classes = []
```

Means:

* ❌ No permission checks
* ❌ Public access

Same applies to:

```python
authentication_classes = []
```

👉 Use **intentionally**, not accidentally.

---

## 8. Using DEBUG to Change Defaults

### Why?

* Easier testing
* Less friction in development

---

### Example

```python
if DEBUG:
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = [
        "api.authentication.TokenAuthentication",
    ]
```

### Best practice

* **Dev**: flexible auth
* **Production**: strict auth
* Often achieved using **separate settings files**

---

## 9. Throttling (Rate Limiting)

### What is throttling?

Limits how many requests a user can make in a time window.

Example:

* 1000 requests/day/user

---

### DRF Throttling Concept

```python
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "user": "1000/day",
    },
}
```

---

### Instructor’s advice (important)

* DRF throttling is **okay**
* But **NGINX / load balancer throttling is better**
* DRF throttling only applies to API views

---

## 10. Authentication vs Permission (Clear Difference)

| Step           | Question         |
| -------------- | ---------------- |
| Authentication | Who are you?     |
| Permission     | Are you allowed? |

Flow:

```
Request
 → Authentication
 → Permission
 → View logic
```

---

## 11. Why Defaults Are Powerful

### Benefits

✅ Centralized security
✅ Less boilerplate
✅ Easy global changes
✅ Safer APIs
✅ Cleaner views

---

## 12. Common Mistake Highlighted in Transcript

❌ Wrong key:

```python
"DEFAULT_AUTHENTICATION_CLASSES": [...]
```

❌ Typo:

```python
"DEFAULT_AUTHENTICATION"
```

✅ Correct:

```python
"DEFAULT_PERMISSION_CLASSES"
```

Small typo = **security bug**

---

## 13. When to Still Define Permissions in Views

You define permissions in views when:

* Admin-only APIs
* Staff/editor permissions
* Object-level permissions

Example:

```python
class ProductUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAdminUser]
```

---

## 14. Avoid Repetition → Use Mixins (Preview)

Instead of:

```python
permission_classes = [IsAdminUser]
```

Everywhere…

You create:

```python
class StaffPermissionMixin:
    permission_classes = [IsAdminUser]
```

And reuse it:

```python
class ProductUpdateAPIView(StaffPermissionMixin, UpdateAPIView):
    ...
```

(This is what the next tutorial covers.)

---

## 15. One-Line Mental Model

> **Defaults define the rules.
> Views override the exceptions.**

---

## 16. Interview-Ready Summary

* `REST_FRAMEWORK` controls global API behavior
* Authentication & permission defaults reduce duplication
* View-level settings override global ones
* Empty permission/auth lists disable security
* Throttling limits request rates
* Defaults make APIs safer and easier to maintain

- [Settings](https://www.django-rest-framework.org/api-guide/settings/)

---

## Using Mixins for Permissions (DRF)

## 1. Why Use Mixins for Permissions?

### The problem

You keep writing this in many views:

```python
permission_classes = [IsAdminUser, StaffEditorPermission]
```

Issues:

* Repetition
* Hard to change later
* Risk of inconsistency
* Messy views

---

### The solution

👉 **Create a Permission Mixin**

A mixin:

* Holds shared logic/configuration
* Is reusable across views
* Keeps views clean

---

## 2. Moving Permissions to a Central Place

### What the instructor does

* Moves `permissions.py` from `products` app → `api` app
* Reason: permissions are **cross-cutting concerns**
* Used by multiple apps

✔️ Good architecture practice

---

### Folder structure (after refactor)

```
api/
├── permissions.py
├── mixins.py
products/
├── views.py
```

---

## 3. Custom Permission (Recap)

Example: **StaffEditorPermission**

```python
# api/permissions.py
from rest_framework.permissions import BasePermission

class StaffEditorPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and
            user.is_staff
        )
```

📌 This answers:

> “Is the user allowed to access this view?”

---

## 4. Creating the Permission Mixin

### Mixin definition

```python
# api/mixins.py
from rest_framework import permissions
from .permissions import StaffEditorPermission

class StaffEditorPermissionMixin:
    permission_classes = [
        permissions.IsAdminUser,
        StaffEditorPermission,
    ]
```

### What this does

Any view that **inherits this mixin**:

* Automatically gets these permission classes
* No need to declare them again

---

## 5. Using the Mixin in Views

### Before (repetitive & noisy)

```python
class ProductUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAdminUser, StaffEditorPermission]
```

---

### After (clean & expressive)

```python
from api.mixins import StaffEditorPermissionMixin

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    UpdateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

📌 Just reading the class name tells you:

> “This endpoint is restricted to staff editors.”

---

## 6. Important Rule: Mixin Order Matters

Always place mixins **before** DRF generic views:

```python
class MyView(MyMixin, ListAPIView):
    ...
```

Why?

* Python’s MRO (Method Resolution Order)
* DRF reads attributes top-down

---

## 7. Removing Redundant Imports

After using mixins, you can safely delete:

* `permission_classes` from views
* Permission-related imports

Result:

* Cleaner files
* Less cognitive load
* Easier maintenance

---

## 8. Testing the Permission Mixin

### Scenario

* User logged in ❌
* But not staff ❌

➡️ Access denied

---

### Fix

* Add user to `staff` or editor group
* Refresh API
* Access granted ✅

This confirms:
✔️ Mixin works
✔️ Permission is enforced everywhere it’s used

---

## 9. Power of Mixins (Very Important Insight)

### One change → affects all views

Example:

```python
class StaffEditorPermissionMixin:
    permission_classes = [
        permissions.AllowAny,  # ⚠️ dangerous
    ]
```

❌ All views become public
✔️ Centralized control
⚠️ Centralized risk

---

## 10. Why Mixins Are Worth It

### Benefits

✅ DRY (Don’t Repeat Yourself)
✅ Central permission logic
✅ Easy refactors
✅ Clean views
✅ Expressive class names

---

## 11. Mixins Are Not Only for Permissions

You can create mixins for:

### Querysets

```python
class UserQuerysetMixin:
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
```

---

### Serializers

```python
class ProductSerializerMixin:
    serializer_class = ProductSerializer
```

---

### Combined Mixins (Advanced)

```python
class StaffEditorView(
    StaffEditorPermissionMixin,
    UserQuerysetMixin,
    ListAPIView
):
    ...
```

---

## 12. When NOT to Use Mixins

Avoid mixins when:

* Used only once
* Logic is too specific
* Over-abstracting simple code

---

## 13. One-Line Mental Model

> **Mixins let you reuse behavior, not copy code.**

---

## 14. Interview-Ready Summary

* Mixins reduce permission duplication
* They centralize access control
* They improve readability and maintainability
* One change affects many views
* Must be used carefully to avoid security issues

---

## 15. What Comes Next (Context)

Next topics usually cover:

* Object-level permissions
* Token authentication
* JWT authentication
* Combining mixins + authentication

---

## ViewSets & Routers — DRF Explained Clearly

## 1. What Problem Do ViewSets Solve?

### Before (what you already did)

You manually created:

* List view
* Detail view
* Create view
* Update view
* Delete view
* URLs for each one

This gives **maximum control**, but:

* Lots of boilerplate
* Many URLs to maintain

---

### ViewSets goal

👉 **Bundle related CRUD logic into ONE class**
👉 **Auto-generate URLs using Routers**

Less code, faster setup.

---

## 2. Creating a ViewSet

### Example: `ModelViewSet` (Full CRUD)

```python
# products/viewsets.py
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
```

### What you get automatically

| HTTP Method | Action         | Equivalent Generic View |
| ----------- | -------------- | ----------------------- |
| GET         | list           | ListAPIView             |
| GET         | retrieve       | RetrieveAPIView         |
| POST        | create         | CreateAPIView           |
| PUT         | update         | UpdateAPIView           |
| PATCH       | partial_update | UpdateAPIView           |
| DELETE      | destroy        | DestroyAPIView          |

All from **just 2 lines**:

```python
queryset
serializer_class
```

---

## 3. Routers: Auto-Generating URLs

Instead of manually defining URLs, **routers inspect the ViewSet and build URLs**.

### Router setup

```python
# cfehome/routers.py
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register("products-abc", ProductViewSet, basename="products")

urlpatterns = router.urls
```

---

### Hook router into main `urls.py`

```python
# cfehome/urls.py
from django.urls import path, include

urlpatterns = [
    path("api/v2/", include("cfehome.routers")),
]
```

---

## 4. Resulting URLs (Auto-Generated)

Visiting `/api/v2/` shows:

```
/api/v2/products-abc/
```

Behind the scenes, DRF created:

```
GET     /products-abc/
POST    /products-abc/
GET     /products-abc/{id}/
PUT     /products-abc/{id}/
PATCH   /products-abc/{id}/
DELETE  /products-abc/{id}/
```

📌 These URLs are **not explicitly visible in code**, which is an important trade-off.

---

## 5. Why Routers Feel “Magical” (and Confusing)

### Good

* Less code
* Faster CRUD APIs
* Consistent REST patterns

### Not so good

* URLs are implicit
* Harder to reason about routing
* Less granular control

This is **why the instructor prefers GenericAPIView** in many real projects.

---

## 6. Limiting Features with `GenericViewSet`

Instead of full CRUD, you may want **only list + retrieve**.

### GenericViewSet + Mixins

```python
from rest_framework import viewsets, mixins

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### What this supports now

| HTTP Method  | Allowed |
| ------------ | ------- |
| GET (list)   | ✅       |
| GET (detail) | ✅       |
| POST         | ❌       |
| PUT          | ❌       |
| DELETE       | ❌       |

Router will now generate **only two endpoints**.

---

## 7. Why This Can Be Confusing

Without printing `router.urls`, it’s hard to know:

* Which endpoints exist
* Which methods are allowed

This is one of the biggest criticisms of ViewSets.

---

## 8. Turning ViewSets into Explicit Views (Advanced)

You can convert ViewSet actions into explicit views:

```python
product_list_view = ProductGenericViewSet.as_view({
    "get": "list"
})

product_detail_view = ProductGenericViewSet.as_view({
    "get": "retrieve"
})
```

Then use them like normal views in `urls.py`.

This defeats the router abstraction—but gives **clarity**.

---

## 9. Why the Instructor Rarely Uses ViewSets

### Personal preference (very common in real projects):

* Wants **full visibility** of URLs
* Likes **explicit routing**
* Easier debugging
* Better long-term maintainability

ViewSets are great **when you know the pattern well**.

---

## 10. ViewSets vs GenericAPIView (Comparison)

| Feature        | ViewSets | GenericAPIView |
| -------------- | -------- | -------------- |
| Boilerplate    | Very low | Medium         |
| URL clarity    | Low      | High           |
| Control        | Medium   | High           |
| Learning curve | Steeper  | Easier         |
| Debugging      | Harder   | Easier         |

---

## 11. Important Insight About Serializers

When using ViewSets:

* List & detail responses come from the **same serializer**
* Often you’ll need:

  * Different serializers for list vs detail
  * Hyperlinked fields (`url` field)

This is why **serializer customization becomes important next**.

---

## 12. Mental Model (One-Line)

> **ViewSets + Routers trade explicit control for convention and speed.**

---

## 13. When Should YOU Use ViewSets?

Use ViewSets when:

* CRUD-heavy APIs
* Consistent REST patterns
* Internal APIs
* Rapid development

Avoid when:

* Public APIs
* Complex permissions
* Custom URL structures
* Need clarity over magic

### Why to use ViewSets & Routers?

- Reduce boilerplate: A ViewSet groups related actions (list/create/retrieve/update/destroy) into one class instead of five separate views.
- Automatic URL wiring: A Router (e.g., DefaultRouter) generates RESTful URL patterns for all standard actions, so you don't hand-write each route.
- Consistency & discoverability: Routers produce predictable endpoints and names, and integrate with DRF's browsable API and viewset action names.
- Extensibility: Easy to add custom actions (@action) and use nested routers or viewset mixins.

### When to use ViewSet vs APIView?

- Use ViewSet + Router when endpoints follow standard CRUD patterns — fastest and cleanest.
- Use APIView or generic views when:
  - An endpoint has highly custom behavior that doesn't fit standard actions.
  - You need very fine-grained control over request/response handling or separate permission logic per method.

---

## URLs, Reverse & Serializers (DRF) — Complete Notes

## Big Picture (What this lesson is about)

You’re learning **how to include URLs inside serialized API responses**, so that:

* A product list can link to its **detail / edit view**
* URLs stay **maintainable** when API versions or routes change
* Your API becomes **self-descriptive (RESTful)**

This is a *core Django REST Framework concept*.

---

## ❌ The Naive / Wrong Way (Hardcoding URLs)

### What was done

```python
class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return f"/api/products/{obj.pk}/"
```

### Why this is bad

* ❌ Hardcoded paths
* ❌ Breaks if:

  * API version changes (`/api/v2/`)
  * URL structure changes
  * App is reused elsewhere
* ❌ Doesn’t generate **absolute URLs**

**Key lesson**: Never hardcode API URLs inside serializers.

---

## ✅ Better Way: `reverse()` from DRF

### Concept: `reverse()`

`reverse()` looks up URLs **by name**, not by path.

So instead of saying:

```
/api/products/5/
```

You say:

```
"Whatever URL is named product-detail with pk=5"
```

---

### Correct import (important!)

```python
from rest_framework.reverse import reverse
```

⚠️ Not Django’s `django.urls.reverse`
DRF’s version supports **absolute URLs** using `request`.

---

### Serializer using `reverse()`

```python
class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None

        return reverse(
            "product-detail",
            kwargs={"pk": obj.pk},
            request=request
        )

    class Meta:
        model = Product
        fields = ["id", "title", "price", "url"]
```

---

### Why `self.context.get("request")`?

* Serializers **don’t always** have access to request
* Generic views **automatically pass it**
* Manual serializer usage does not

So we safely do:

```python
request = self.context.get("request")
```

---

### URL config (must match `reverse()`)

```python
# urls.py
path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail")
```

🔑 `kwargs={"pk": obj.pk}` must match `<int:pk>`

---

## Result

API response becomes:

```json
{
  "id": 1,
  "title": "Laptop",
  "price": 50000,
  "url": "http://127.0.0.1:8000/api/products/1/"
}
```

✔ Absolute
✔ Maintainable
✔ Version-safe

---

## Multiple URLs (Detail, Edit, etc.)

You can add more links:

```python
edit_url = serializers.SerializerMethodField()

def get_edit_url(self, obj):
    request = self.context.get("request")
    if request is None:
        return None
    return reverse(
        "product-edit",
        kwargs={"pk": obj.pk},
        request=request
    )
```

And URL pattern:

```python
path("products/<int:pk>/edit/", ProductEditView.as_view(), name="product-edit")
```

---

## ✅ BEST / PREFERRED WAY: `HyperlinkedIdentityField`

This is the **cleanest** and **most DRF-native** approach.

---

### Concept: `HyperlinkedIdentityField`

* Auto-generates URL
* No custom method needed
* Requires `ModelSerializer`
* Uses `view_name` + `lookup_field`

---

### Serializer example

```python
class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field="pk"
    )

    class Meta:
        model = Product
        fields = ["id", "title", "price", "url"]
```

✔ Cleaner
✔ Less code
✔ Easier to maintain

---

### Requirement

Your view **must** receive request context (generic views do this automatically):

```python
class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

## SerializerMethodField vs HyperlinkedIdentityField

| Feature            | SerializerMethodField | HyperlinkedIdentityField |
| ------------------ | --------------------- | ------------------------ |
| Flexibility        | ⭐⭐⭐⭐                  | ⭐⭐                       |
| Simplicity         | ⭐⭐                    | ⭐⭐⭐⭐                     |
| Custom logic       | Yes                   | No                       |
| Preferred for URLs | ❌                     | ✅                        |

**Rule of thumb**

* Use `HyperlinkedIdentityField` for standard links
* Use `SerializerMethodField` for complex logic

---

## Multiple Serializers for Different Views

### Why?

* List view → less data
* Detail view → more data
* Sometimes you don’t want URLs everywhere

---

### Example

```python
class ProductListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail"
    )

    class Meta:
        model = Product
        fields = ["id", "title", "url"]
```

```python
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
```

```python
class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
```

✔ Cleaner APIs
✔ Better control
✔ Industry standard

---

## Important Creation Insight (POST requests)

Even though `url` is in the serializer:

* It is **read-only**
* You **don’t need to send it** when creating objects

```json
POST /api/products/
{
  "title": "Phone",
  "price": 30000
}
```

✔ No errors
✔ URL is auto-generated in response

---

## Final Key Takeaways (Very Important)

### ✅ Best Practices

* ❌ Never hardcode URLs
* ✅ Use `reverse()` or `HyperlinkedIdentityField`
* ✅ Always name your URL patterns
* ✅ Use multiple serializers for different views
* ✅ Let serializers describe navigation

### 🔥 Interview-worthy line

- “DRF serializers should expose navigable URLs using `reverse` or `HyperlinkedIdentityField` to keep APIs decoupled from URL structure.”

---

## **DRF `reverse` — Useful & Important Pointers**

- **What it is:** `rest_framework.reverse.reverse` builds a URL from a view name and kwargs. Unlike Django's `reverse`, it accepts a `request` and `format` argument so it can return absolute URLs (including scheme and host) useful for APIs.

- **Why use it in serializers:** Serializers often expose links (self/detail URLs or related resource URLs). Using DRF's `reverse` inside a serializer (usually in a `SerializerMethodField`) produces correct, fully-qualified links when the serializer receives `context={'request': request}` from a view.

- **Common pattern (SerializerMethodField):**

  ```python
  from rest_framework import serializers
  from rest_framework.reverse import reverse

  class ProductSerializer(serializers.ModelSerializer):
      url = serializers.SerializerMethodField()

      class Meta:
          model = Product
          fields = ['id', 'name', 'url']

      def get_url(self, obj):
          request = self.context.get('request')
          return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
  ```

- **Simpler alternative — hyperlinked fields:** Use `HyperlinkedModelSerializer` or `HyperlinkedIdentityField` for standard self-links to avoid manual `reverse` calls:

  ```python
  class ProductHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Product
          fields = ['url', 'id', 'name']
          extra_kwargs = {'url': {'view_name': 'product-detail'}}
  # or
  url = serializers.HyperlinkedIdentityField(view_name='product-detail')
  ```

- **Important: view names and routers** — When using `DefaultRouter` and `router.register('products', ProductViewSet)`, DRF creates named routes like `product-list` and `product-detail`. Use those names with `reverse` or hyperlinked fields.

- **DRF `reverse` vs Django `reverse`:** DRF's `reverse(..., request=request)` can return absolute URLs; Django's `django.urls.reverse` returns a path only (use `request.build_absolute_uri()` to make it absolute).

- **Best practices:**
  - Prefer hyperlinked serializers for simple self-links.
  - Use `SerializerMethodField` + `reverse` for custom or conditional links.
  - Ensure your view passes the `request` in serializer context (generic views and viewsets do this automatically).

---

## ModelSerializer: `create()` & `update()` — Complete Notes

## Big Idea

This lesson explains:

* How **ModelSerializer actually creates and updates models**
* How to add **extra fields not present in the model**
* How to use **write-only fields**
* When and why to **override `create()` and `update()`**
* How this relates to `serializer.save()` and `perform_create()`

---

## 1️⃣ Adding a Field That Is NOT in the Model

### Scenario

You want to send an email **when a product is created**, but:

* `email` is **not a Product model field**
* You still want it accepted in POST requests

---

### ❌ Problem: Normal Field Causes Error

```python
email = serializers.EmailField()
```

If you add this to `fields`, DRF tries to do:

```python
Product.objects.create(email="abc@gmail.com")
```

❌ Boom → **field does not exist on Product**

---

## 2️⃣ Solution: `write_only=True`

### Concept: `write_only`

* Field is accepted in input (POST / PUT)
* Field is NOT returned in API response
* Field is NOT expected on the model

---

### Correct Example

```python
class ProductSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = ["id", "title", "price", "email"]
```

### What happens now?

* ✅ Email shows up in browsable API form
* ❌ Email not shown in response
* ❌ Still causes error unless handled in `create()`

---

## 3️⃣ Why Error Still Happens

Even with `write_only=True`:

```python
serializer.save()
```

Internally does:

```python
Product.objects.create(**validated_data)
```

But `validated_data` still contains:

```python
{"title": "...", "price": 100, "email": "..."}
```

❌ Product model doesn’t accept `email`

---

## 4️⃣ Overriding `create()` (Core Concept)

### Default DRF behavior (simplified)

```python
def create(self, validated_data):
    return Product.objects.create(**validated_data)
```

So we **override it**.

---

### Custom `create()` with extra field

```python
class ProductSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = ["id", "title", "price", "email"]

    def create(self, validated_data):
        email = validated_data.pop("email")  # remove extra field

        product = Product.objects.create(**validated_data)

        # example side effect
        print("Send email to:", email)

        return product
```

---

### Why `pop()` is important

* Removes non-model fields
* Prevents DB errors
* Lets you use data for side-effects (email, logging, analytics)

---

## 5️⃣ `validated_data` — Very Important

### What is it?

* Cleaned + validated input data
* Only exists **after validation**
* Used by `create()` and `update()`

Example:

```python
validated_data = {
    "title": "Laptop",
    "price": 50000,
    "email": "abc@gmail.com"
}
```

---

## 6️⃣ Where Does `create()` Get Called From?

### Key Insight

```python
serializer.save()
```

DRF decides:

| Condition       | Method Called                      |
| --------------- | ---------------------------------- |
| No instance     | `create(validated_data)`           |
| Instance exists | `update(instance, validated_data)` |

You **never call `create()` manually**.

---

## 7️⃣ Doing the Same Logic in the View (`perform_create`)

### Alternative approach

```python
class ProductListCreateView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data.pop("email")
        product = serializer.save()
        print("Send email to:", email)
```

### Why this works

* `validated_data` is available **before** save
* `serializer.save()` triggers `create()`

---

### Which is better?

✅ **Serializer** (recommended)

* Reusable
* Works everywhere
* Cleaner architecture

❌ View

* Tied to one endpoint

---

## 8️⃣ `update()` Method Explained

### Default behavior (simplified)

```python
def update(self, instance, validated_data):
    instance.title = validated_data.get("title", instance.title)
    instance.price = validated_data.get("price", instance.price)
    instance.save()
    return instance
```

---

### Custom `update()` with extra field

```python
def update(self, instance, validated_data):
    email = validated_data.pop("email", None)

    instance = super().update(instance, validated_data)

    if email:
        print("Send update email to:", email)

    return instance
```

---

### Key Points

* `instance.save()` is handled automatically
* You don’t need to save again
* `super().update()` is safest

---

## Where is `serializer.save()` called **in two places**?

## 1️⃣ **In the Generic API View (View Layer)**

This is the **explicit call you usually see**.

Example (ListCreateAPIView):

```python
class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
```

### What’s happening here?

* DRF’s `create()` method on the view:

  * validates data
  * then calls `perform_create()`
* `perform_create()` calls:

```python
serializer.save()
```

✅ **First place `serializer.save()` is called**

---

## 2️⃣ **Inside `serializer.save()` itself (Serializer Layer)**

This is the **second place**, and it’s easy to miss.

### Internally, `serializer.save()` does this:

```python
if self.instance is None:
    return self.create(self.validated_data)
else:
    return self.update(self.instance, self.validated_data)
```

So:

| Case            | What gets called                   |
| --------------- | ---------------------------------- |
| Creating object | `create(validated_data)`           |
| Updating object | `update(instance, validated_data)` |

> “serializer.save if there isn’t an instance will run the create method
> if there *is* an instance it’s going to run another method called update”

✅ **Second place `serializer.save()` effectively triggers logic**

---

## Putting It Together (Mental Model)

### Request Flow for POST (Create)

```
HTTP POST
  ↓
View.create()
  ↓
perform_create()
  ↓
serializer.save()        ← (1st place)
  ↓
serializer.create()      ← (2nd place, internal)
  ↓
Model.objects.create()
```

---

### Request Flow for PUT / PATCH (Update)

```
HTTP PUT/PATCH
  ↓
View.update()
  ↓
serializer.save()        ← (1st place)
  ↓
serializer.update()      ← (2nd place, internal)
  ↓
instance.save()
```

---

## ✅ Final Answer (Short & Precise)

**`serializer.save()` is involved in two places:**

1. **Explicitly in the view**, usually inside `perform_create()` or `perform_update()`
2. **Internally inside the serializer**, where it automatically calls:

   * `create(validated_data)` when creating
   * `update(instance, validated_data)` when updating

That’s the full picture — and once you see it, DRF suddenly feels much less “magical.”

---

## 9️⃣ `serializer.save()` vs `model.save()`

| Method              | Purpose                        |
| ------------------- | ------------------------------ |
| `serializer.save()` | Calls `create()` or `update()` |
| `model.save()`      | Saves an existing instance     |

**Serializer = business logic layer**

---

## 🔟 Adding Arbitrary Fields — Summary

### You can add fields that:

* ❌ Don’t exist in model
* ✅ Are used for:

  * Emails
  * Flags
  * Tracking
  * Temporary metadata

### Rules

✔ Must be `write_only=True`
✔ Must be removed from `validated_data`
✔ Best handled in serializer

---

## Final Takeaways (Exam / Interview Ready)

### 🔑 Core Truths

* `ModelSerializer.create()` → object creation
* `ModelSerializer.update()` → object modification
* `serializer.save()` chooses which one to call
* `validated_data` is the clean input
* Non-model fields must be popped

### ⭐ Best Practice

> “Side effects like emails, logging, or analytics should live in the serializer’s create/update methods, not the view.”

---

## Custom Validation with DRF Serializers — Complete Notes

## Big Picture

**Validation in DRF happens before `create()` or `update()`**
It runs when:

* `serializer.is_valid()` is called
* Only applies to **write operations** (POST / PUT / PATCH)
* Never affects read-only responses

DRF gives you **multiple layers** to validate data:

1. Field-level validation (inline)
2. External reusable validators
3. Built-in validators (`UniqueValidator`)
4. Context-aware validation (request / user)
5. Field overriding (`CharField`, `EmailField`, etc.)
6. Renaming fields using `source`

---

## 1️⃣ Field-Level Validation (`validate_<fieldname>`)

### What it is

A method inside the serializer that validates **one specific field**.

### When it runs

* On create
* On update
* Only for incoming data

### Syntax

```python
def validate_<field_name>(self, value):
    return value
```

### Example: Ensure Product Title is Unique (Case-Insensitive)

```python
class ProductSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                f"{value} is already a product name"
            )
        return value
```

### Key Points

* `value` = submitted value
* Use `iexact` instead of `exact` to avoid case issues
* Best for **simple, serializer-specific logic**

---

## 2️⃣ External Validators (Reusable)

### Why use them?

* Cleaner serializers
* Reusable across serializers, models, forms
* Better organization for large projects

### Create a `validators.py`

```python
# validators.py
from rest_framework import serializers
from .models import Product

def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(
            f"{value} is already a product name"
        )
    return value
```

### Use it in Serializer

```python
from .validators import validate_title

class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = "__all__"
```

### When to use

* Shared validation logic
* Cleaner codebase
* Validation used in multiple serializers

---

## 3️⃣ Built-in `UniqueValidator` (Preferred for Uniqueness)

### Why this is important

DRF already solves uniqueness validation — don’t reinvent the wheel.

### Example

```python
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        validators=[
            UniqueValidator(queryset=Product.objects.all())
        ]
    )

    class Meta:
        model = Product
        fields = "__all__"
```

### Advantages

* Clean
* Optimized
* DRF-standard
* Supports update operations properly

✅ **Best choice for uniqueness validation**

---

## 4️⃣ Combining Multiple Validators

You can stack validators easily.

### Example:

* Title must be unique
* Title must NOT contain the word `"hello"`

```python
def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("hello is not allowed")
    return value
```

```python
class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        validators=[
            UniqueValidator(queryset=Product.objects.all()),
            validate_title_no_hello
        ]
    )

    class Meta:
        model = Product
        fields = "__all__"
```

### Result

Both validations run automatically.

---

## 5️⃣ Context-Aware Validation (`self.context`)

### Why this matters

Sometimes validation depends on:

* Logged-in user
* Request
* Permissions
* Ownership

### Access request inside serializer

```python
request = self.context.get("request")
user = request.user
```

### Example

```python
def validate_title(self, value):
    request = self.context.get("request")
    user = request.user

    if Product.objects.filter(title=value, owner=user).exists():
        raise serializers.ValidationError(
            "You already used this title"
        )
    return value
```

### When needed

* Multi-user systems
* Ownership-based rules
* Per-user uniqueness

---

## 6️⃣ Overriding Field Types (Extra Validation for Free)

DRF fields perform **automatic validation**.

### Example: Changing Field Type

```python
title = serializers.EmailField()
```

Now DRF validates:

* Proper email format
* No extra code required

📌 Even though `title` is a model `CharField`, the serializer controls validation.

---

## 7️⃣ Renaming Fields with `source`

### Why useful

* Better API naming
* Backward compatibility
* Cleaner frontend contracts

### Example

```python
class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source="title",
        read_only=True
    )

    class Meta:
        model = Product
        fields = ["id", "title", "name"]
```

### Output

```json
{
  "id": 1,
  "title": "Laptop",
  "name": "Laptop"
}
```

### Key Points

* `source` maps serializer field → model field
* Works with foreign keys too:

```python
email = serializers.EmailField(source="user.email")
```

---

## 8️⃣ Where Validation Fits in Request Flow

```
POST / PUT / PATCH
   ↓
serializer = Serializer(data=request.data)
   ↓
serializer.is_valid()   ← VALIDATION HAPPENS HERE
   ↓
serializer.save()
   ↓
create() / update()
```

❗ If validation fails → `create()` and `update()` NEVER run

---

## Best Practices (Real-World Advice)

✔ Put **data integrity rules** on the **model**
✔ Put **request/user-specific rules** in **serializer**
✔ Prefer **UniqueValidator** over manual queries
✔ Use external validators for shared logic
✔ Keep validation simple and readable

---

## Final Takeaway

Custom validation in DRF is **layered and flexible**:

| Method              | Use Case                       |
| ------------------- | ------------------------------ |
| `validate_<field>`  | Simple, serializer-only checks |
| External validators | Reusable logic                 |
| `UniqueValidator`   | Uniqueness (best practice)     |
| `self.context`      | User / request-aware rules     |
| Field override      | Format-level validation        |
| `source`            | Field remapping                |

- [Serializer fields](https://www.django-rest-framework.org/api-guide/fields/)

---

## 📌 Request User Data & Customizing QuerySets in DRF

It focuses on **associating data with users**, **restricting data visibility**, and **automatically assigning ownership** in Django REST Framework.

---

## 1️⃣ Attaching a User to a Model (ForeignKey)

### Key Points

* Each product belongs to a user
* Use `settings.AUTH_USER_MODEL` instead of `auth.User`
* Supports future customization of the User model
* Avoid cascading deletes when a user is removed

### Example

```python
# models.py
from django.conf import settings
from django.db import models

class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        default=1   # assumes a default user exists
    )
    title = models.CharField(max_length=255, unique=True)
```

✅ **Why use `settings.AUTH_USER_MODEL`?**

* Django-recommended
* Safer if you ever customize the User model

---

## 2️⃣ Running Migrations After Model Changes

Whenever models change:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 3️⃣ Exposing User Field in the Serializer (Temporarily)

Used for debugging and validation.

```python
# serializers.py
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['user', 'title']
```

⚠️ **Later removed** because:

* Users should not control ownership manually
* Ownership should come from `request.user`

---

## 4️⃣ Accessing `request.user` in Views

### Important Distinction

| Location   | How to Access                      |
| ---------- | ---------------------------------- |
| View       | `self.request.user`                |
| Serializer | `self.context.get("request").user` |

### Example

```python
def get_queryset(self):
    print(self.request.user)
    return super().get_queryset()
```

---

## 5️⃣ Filtering QuerySet by Logged-In User

### Goal

Only return objects owned by the logged-in user.

```python
def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
        return Product.objects.filter(user=user)
    return Product.objects.none()
```

✅ Ensures:

* Users see only their own products
* Unauthorized users see nothing

---

## 6️⃣ Automatically Assigning User on Create

### Problem

User field removed from serializer → who sets it?

### Solution: `perform_create`

```python
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
```

✔ Prevents:

* User spoofing
* Manual ownership assignment

---

## 7️⃣ Why Remove `user` From Serializer?

* Ownership should be **implicit**
* Logged-in user = owner
* Cleaner API design

```python
# serializers.py
fields = ['title']
```

---

## 8️⃣ Unique Validator Issue (Cross-User Conflict)

### Problem

Two different users could not create products with the same title.

### Why?

Default unique validator checks **globally**, not per user.

### Fix

Use `iexact` lookup or scoped validation.

```python
validators = [
    UniqueValidator(
        queryset=Product.objects.all(),
        lookup='iexact'
    )
]
```

✔ Ensures case-insensitive uniqueness

---

## 9️⃣ Creating a Reusable User QuerySet Mixin

### Why?

* Avoid repeating `get_queryset`
* Clean and reusable
* Centralized ownership filtering

### Mixin Implementation

```python
class UserQuerySetMixin:
    user_field = 'user'
    allow_staff_view = False

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.is_staff and self.allow_staff_view:
            return qs

        lookup = {self.user_field: user}
        return qs.filter(**lookup)
```

---

## 🔁 Dynamic Field Filtering Explained

```python
lookup = {self.user_field: user}
qs.filter(**lookup)
```

Equivalent to:

```python
qs.filter(user=request.user)
```

🔑 Useful when field name changes (e.g., `owner`, `created_by`)

---

## 🔟 Using the Mixin in Views

```python
class ProductListCreateView(
    UserQuerySetMixin,
    generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

## 1️⃣1️⃣ Allowing Staff/Admin to See Everything

```python
allow_staff_view = True
```

✔ Staff → all records
✔ Normal users → own records only

---

## 1️⃣2️⃣ Why Permissions Alone Are Not Enough

### Problem

Permissions allow access, but **querysets define visibility**

### Correct Approach

✔ Combine:

* **Permissions** → can access?
* **QuerySets** → what data?

---

## 1️⃣3️⃣ Security Best Practice Highlight

> **Least Privilege Principle**

* Default → restrictive
* Explicitly allow broader access
* Prevent accidental data leaks

---

## 1️⃣4️⃣ Key Takeaways

### ✔ What You Learned

* How to associate models with users
* How to access `request.user`
* How to auto-assign ownership
* How to restrict querysets per user
* How to create reusable mixins
* Why permissions ≠ data access
* Why serializers should not expose ownership fields

---

## 🔜 What’s Next (Mentioned in Tutorial)

➡ **Foreign key / related field serialization**

* Display user info safely
* Nested serializers
* Read-only relationships

---

## 📌 Related Fields & Foreign Key Serialization (DRF)

This section explains **how to serialize related data** (ForeignKey & reverse relationships) in Django REST Framework, **why some approaches are bad**, and **which ones are preferred in production**.

---

## 1️⃣ Foreign Key & Reverse Relationship (Core Concept)

### Model Relationship

```python
class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
```

### What This Gives You

| Direction                 | Access                   |
| ------------------------- | ------------------------ |
| Product → User            | `product.user`           |
| User → Products (reverse) | `user.product_set.all()` |

This **reverse relationship** exists automatically unless `related_name` is specified.

---

## 2️⃣ Default ForeignKey Serialization (ID Only)

```python
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'title']
```

### Output

```json
{
  "id": 1,
  "user": 3,
  "title": "Product ABC"
}
```

✔ DRF defaults to **primary key representation**
❌ Not human-friendly

---

## 3️⃣ SerializerMethodField (Works but NOT Recommended)

### Example

```python
class ProductSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField(read_only=True)

    def get_user_data(self, obj):
        return {
            "username": obj.user.username
        }
```

### Why This Is ❌ Not Ideal

* Manual
* Hard to reuse
* No validation
* Logic-heavy serializers

✅ Use only for **computed fields**, not relationships

---

## 4️⃣ Preferred Approach: Nested Serializer (Best Practice)

### Step 1: Create a Public User Serializer

```python
class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
```

✔ No model dependency
✔ Safe for public exposure
✔ Simple and reusable

---

### Step 2: Use It in Product Serializer

```python
class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'user']
```

### Output

```json
{
  "id": 1,
  "title": "Product ABC",
  "user": {
    "id": 3,
    "username": "staff"
  }
}
```

✅ Clean
✅ Scalable
✅ Recommended

---

## 5️⃣ Renaming Fields Using `source`

### Example: Show `owner` Instead of `user`

```python
class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'owner']
```

✔ Model unchanged
✔ API response customized

---

## 6️⃣ Adding Extra User Fields Safely

```python
class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
```

🚫 Avoid exposing:

* email
* phone
* permissions

✔ Public serializer = **minimal data**

---

## 7️⃣ Reverse Relationship Serialization (User → Products)

### Accessing Related Objects

```python
user.product_set.all()
```

---

## 8️⃣ Why Importing ProductSerializer Inside UserSerializer Is BAD

### Problem

* Circular imports
* Infinite nesting
* Performance issues
* Tight coupling

🚫 **Never do this**

```python
# BAD IDEA
from products.serializers import ProductSerializer
```

---

## 9️⃣ Solution: Inline / Lightweight Serializer

### Inline Product Serializer

```python
class UserProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
```

---

## 🔁 Using Inline Serializer via SerializerMethodField

```python
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    other_products = serializers.SerializerMethodField()

    def get_other_products(self, obj):
        qs = obj.product_set.all()[:5]
        return UserProductInlineSerializer(qs, many=True).data
```

### Output

```json
{
  "username": "staff",
  "other_products": [
    {"title": "Product A"},
    {"title": "Product B"}
  ]
}
```

⚠ **Demo-only pattern** (not ideal for large datasets)

---

## 1️⃣0️⃣ Passing Context to Nested Serializers

Needed for fields like `HyperlinkedIdentityField`.

```python
UserProductInlineSerializer(
    qs,
    many=True,
    context=self.context
)
```

✔ Ensures `request` is available

---

## 1️⃣1️⃣ Using `source` for Reverse Relations

```python
class ProductSerializer(serializers.ModelSerializer):
    related_products = UserProductInlineSerializer(
        source='user.product_set',
        many=True,
        read_only=True
    )
```

✔ No method needed
❌ No filtering or limits

---

## 1️⃣2️⃣ Why This Can Be Dangerous

### Problem

* Returns ALL related products
* Grows unbounded
* Performance nightmare

🚨 **Avoid this in production**

---

## 1️⃣3️⃣ Serializer vs ModelSerializer

| Serializer     | ModelSerializer |
| -------------- | --------------- |
| Public data    | CRUD support    |
| Lightweight    | Validation      |
| Read-only      | Create / Update |
| No DB coupling | Model-aware     |

### Rule of Thumb

✔ **Public / nested → Serializer**
✔ **CRUD → ModelSerializer**

---

## 1️⃣4️⃣ Missing Fields Don’t Error (Serializer)

```python
class TestSerializer(serializers.Serializer):
    fake = serializers.CharField(read_only=True)
```

✔ Field silently ignored if missing
❌ Can hide bugs

---

## 1️⃣5️⃣ When Errors DO Happen

Errors appear when:

* Writing data
* Using ModelSerializer
* Validation runs

---

## 1️⃣6️⃣ Final Best Practices Summary

### ✅ DO

* Use **nested serializers** for FK
* Use **public serializers** for users
* Use `source` for renaming
* Limit related data
* Pass context properly

### ❌ DON’T

* Nest serializers infinitely
* Serialize large reverse querysets
* Expose private user fields
* Import serializers circularly

---

## 🔑 Key Takeaway

> **Foreign key serialization is about clarity, security, and performance—not convenience.**

Nested serializers should:

* Be intentional
* Be minimal
* Be bounded

---

## 🔜 What You Should Learn Next

* `select_related` vs `prefetch_related`
* Pagination for nested data
* Dedicated endpoints for related data
* ViewSets + serializers composition


summaries this tutorial transcript in markdown form also make note of all important pointers