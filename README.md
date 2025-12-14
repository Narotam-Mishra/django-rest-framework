
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

Below is a **clean, structured Markdown summary** of the tutorial transcript, with **all important concepts and pointers highlighted**. I’ve organized it so you can quickly revisit this later as reference notes while building Django APIs.

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


summaries this tutorial transcript in markdown form also make note of all important pointers