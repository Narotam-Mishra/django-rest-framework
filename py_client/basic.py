
import requests
import os
from dotenv import load_dotenv

# load env file
load_dotenv()

# fetch api key from dotenv file
api_key = os.getenv("api_key")

# endpoint = "https://reqres.in/api/users"
# endpoint = "https://jsonplaceholder.typicode.com/users"

endpoint = "http://localhost:8000/api/"

# making api call
# get_res = requests.get(endpoint)
# print(get_res.text)

headers = {
    "x-api-key": api_key
}

# get_res = requests.get(endpoint, headers=headers)

get_res = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello Django"})

# print raw text response
# print(get_res.text)

# print status code
# print(get_res.status_code)

print("Response data:",get_res.json())

# print("Status Code:",get_res.status_code)

