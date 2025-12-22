
import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Macbook M5 Pro",
    "content": "this is latest series in Macbook series M5 pro",
    "price": 198.65
}


get_res = requests.put(endpoint, json=data)

# print json response
print("Update Response data:",get_res.json())

# print("Status Code:",get_res.status_code)

