
import requests

endpoint = "http://localhost:8000/api/products/1"


get_res = requests.get(endpoint)

# print json response
print("Response data:",get_res.json())

# print("Status Code:",get_res.status_code)

