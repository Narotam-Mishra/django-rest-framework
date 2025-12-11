
- [Django Rest Framework](https://www.django-rest-framework.org/)

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

# 📌 **Final Notes From the Tutorial**

### ✔ REST API = Web API

### ✔ Uses HTTP requests (GET, POST, PUT, DELETE)

### ✔ Endpoints = different paths of the API

### ✔ Use Python `requests` library to interact with APIs

### ✔ JSON is the standard data format

### ✔ httpbin.org is great for testing

### ✔ Status codes are important for debugging

### ✔ REST APIs allow many clients to consume the same service

---

