import requests

pk = input("Product id to update: ").strip()
if not pk.isdigit():
    raise SystemExit("Invalid id")

endpoint = f"http://localhost:8000/api/products/{pk}/update/"

print("Leave a field empty to skip updating it.")
title = input("New Title: ").strip()
content = input("New Content: ").strip()
price_raw = input("New Price (e.g. 29.99): ").strip()

payload = {}
if title:
    payload["title"] = title
if content:
    payload["content"] = content
if price_raw:
    try:
        payload["price"] = float(price_raw)
    except ValueError:
        print("Invalid price input — skipping price")

if not payload:
    print("Nothing to update; exiting.")
    raise SystemExit

res = requests.patch(endpoint, json=payload)
print("Update Response data:", res.json())