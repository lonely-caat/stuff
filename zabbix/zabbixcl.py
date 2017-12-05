import requests
import logging as logger
from properties import host,username,password,api_host,api_key,m3_api_host
import json


class ZabbixClient(object):
    def __init__(self, host, ):
        self.base = host
        self.logger = logger.getLogger()

    def make_request(self, method='POST', path='', body=None):
        if method=='GET':
            resp = requests.get(self.base+'/'+path,headers={"Content-type": "application/json"})
        if method=='POST':
            resp = requests.post(self.base+'/'+path,json.dumps(body),headers={"Content-type": "application/json"})

        self.logger.debug("Getting response with URL: %s\n"
                          "Code: %s\nHeaders: %s\nBody: %s" % (resp.url, resp.status_code,
                                                               resp.headers, resp.text))
        print resp.status_code
        print resp.url
        print resp.text
        return json.loads(resp.text), resp.status_code, resp.url, json.dumps(body)


if __name__ == '__main__':
    cl = ZabbixClient('http://zabbix.llnw.com')
    cl.make_request(method='POST', path='llnw/api_jsonrpc.php', body=
    {"key": "sjE4i", "jsonrpc": "2.0", "method": "ack.get", "id": 1,
     "params":{"eventid":"100100727239590"}
})

