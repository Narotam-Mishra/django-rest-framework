
import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password?\n")

auth_res = requests.post(auth_endpoint, json={'username': username, 'password':password })

# print json response
print("Auth Response data:",auth_res.json())

if auth_res.status_code == 200:
    token = auth_res.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_res = requests.get(endpoint, headers=headers)

    # print json response
    # print("List Response data:",get_res.json())
    data = get_res.json()
    next_url = data['next']
    results = data['results']
    print("Next URL:",next_url)
    print("Results:",results)
    if next_url is not None:
        get_res = requests.get(next_url, headers=headers)

# print("Status Code:",get_res.status_code)

