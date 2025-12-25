
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

summaries this tutorial transcript in markdown form also make note of all important pointers