import requests
import json

BACKEND_URL = "http://127.0.0.1:8000/sesac/upper"

payload = {"msg": "hdsafghkjhsfld"}

response = requests.post(BACKEND_URL, data=json.dumps(payload))

print(response.status_code)
print(response.content)
print("keys :", list(response.json().keys()))
print("values :", list(response.json().values()))
