
import requests

product_id = input("What is the product id you want to delete?\n")
try:
    product_id = int(product_id)
except Exception:
    product_id = None
    print('Not a valid product id')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    res = requests.delete(endpoint)

    # Print status first
    print("Status Code:", res.status_code)

    # Safe handling: many DELETE endpoints return 204 No Content (empty body)
    if res.status_code == 204 or not res.text:
        print("No content returned. Resource likely deleted.")
    else:
        # Try to decode JSON, fall back to raw text
        try:
            print("Delete Response data:", res.json())
        except Exception:
            print("Delete Response text:", res.text)

