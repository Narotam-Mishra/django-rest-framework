
import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "IPhone17 pro",
    "content": "IPhone 17 pro from Apple",
    "price": 123.11,
}

get_res = requests.post(endpoint, json=data)

# print json response
print("Create Response data:",get_res.json())

# print("Status Code:",get_res.status_code)

