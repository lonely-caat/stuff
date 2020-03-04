import requests
from pprint import pprint
import json

resp = requests.get('/config-mgmt-api/v2/configs/optionSet')
results = (resp.json()['results'])
print results
print [x for x in results]
print [x for x in x.values(),x.keys() ]
