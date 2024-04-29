import requests
import json

BACKEND_URL = "http://127.0.0.1:8000/upper"
payload = {"msg": "abcdefㅇㅇg"}

response = requests.post(BACKEND_URL, data=json.dumps(payload))
print(requests.status_codes)
print(response.json()["result"])
print(response.content.decode("utf-8"))
print(response.content)

if response.ok:
    print("성공!")
