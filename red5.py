import requests
import json

url = "http://rts-sm-2.iad.qa.dev.llnw.net/streammanager/api/3.1/admin/event/meta/limelightlive/mmdstg001/t23?accessToken=v5qcb2yzl0thv2c"
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