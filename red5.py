import requests
import json

payload=json.dumps({
  "meta": {
    "stream": [
    {
        "name": "t23_200",
        "bandwidth": 200000,
        "level": 0}
    ],
    "georules": {
      "regions": [],
      "restricted": False
    },
    "qos": 3,
    "publish_validation": False,
    "subscribe_validation": False
  }
})


resp = requests.post(url,json=payload)

print(resp.text)
print(resp.request.url)
