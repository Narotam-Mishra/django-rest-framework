
import requests

endpoint = "http://localhost:8000/api/products/"

get_res = requests.get(endpoint)

# print json response
print("List Response data:",get_res.json())

# print("Status Code:",get_res.status_code)

