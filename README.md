
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

summaries this tutorial transcript in markdown form also make note of all important pointers