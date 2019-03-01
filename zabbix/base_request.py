import requests
import logging as logger
from properties import host,username,password,api_host,api_key,m3_api_host
import json


class BaseRequest(object):
    def __init__(self, host):
        self.base = host
        self.logger = logger.getLogger()

    def make_request(self, method='POST', path='', data=None):
        if method=='GET':
            resp = requests.get(self.base+'/'+path,headers={"Content-type": "application/json"})
        if method=='POST' or data:
            resp = requests.post(self.base+'/'+path,json.dumps(data),headers={"Content-type": "application/json"})

        self.logger.debug("Getting response with URL: %s\n"
                          "Code: %s\nHeaders: %s\ndata: %s" % (resp.url, resp.status_code,
                                                               resp.headers, resp.text))
        print(resp.status_code, 'base_request')
        print(resp.request, 'base_request')
        print(resp.url, 'base_request')
        print(resp.text, 'base_request')

        return json.loads(resp.text),\
                             # resp.status_code, resp.url

