import requests

headers = {
    'Authorization': 'Bearer d6585204773c390c5e56cae2563c5e27f2c150ff'
}

endpoint = "http://localhost:8000/api/products/"

# http://localhost:8000/admin/
# session -> post data
# selenium

title = input("Title: ").strip()
price_raw = input("Price (e.g. 19.99): ").strip()
content = input("Content (optional, press Enter to use title): ").strip()

try:
    price = float(price_raw) if price_raw else None
except ValueError:
    print("Invalid price; using null")
    price = None

payload = {"title": title}
if price is not None:
    payload["price"] = price
if content:
    payload["content"] = content
else:
    payload["content"] = title

res = requests.post(endpoint, json=payload, headers=headers)
print("Create Response data:", res.json())