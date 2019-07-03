import requests
import logging as logger
from properties import host,username,password,api_host,api_key,m3_api_host
import json


class ZabbixClient(object):
    def __init__(self, host, ):
        self.base = host
        self.logger = logger.getLogger()

    def make_request(self, method='POST', path='', params=None,data=None):
        if method=='GET':
            resp = requests.get(self.base+'/'+path,params,headers={"Content-type": "application/json"})
        if method=='POST':
            resp = requests.post(self.base+'/'+path,data , headers={"Content-type": "application/json"},)

        self.logger.debug("Getting response with URL: %s\n"
                          "Code: %s\nHeaders: %s\ndata: %s" % (resp.url, resp.status_code,
                                                               resp.headers, resp.text))
        print(resp.status_code)
        print(resp.url)
        print(resp.text)
        print(resp.json())
        # return json.loads(resp.text), resp.status_code, resp.url, json.dumps(data)


if __name__ == '__main__':
    # cl = ZabbixClient('http://zabbix-command01.dev.phx7.llnw.net')

    # cl = ZabbixClient('http://nautilus.ua.llnw.net')
    cl = ZabbixClient('http://zabbix-command01.dev.phx7.llnw.net')


    # cl.make_request(method='POST', path='llnw/ack.php',data={"key":"","method":"get.ack","eventids":"47229345"})
    # cl.make_request(method='POST', path='llnw/api_jsonrpc.php',data=json.dumps({"key":"sjE4i","method":"get.squelch","active":1}))

    cl.make_request(method='POST', path='api_jsonrpc.php',data=json.dumps({"key":"","jsonrpc":"2.0","method":"event.get","params":{"output":"json","hostname":["salt-epos-410-gphelps.saltdev.llnw.net"],"username":"mbilichenko","reason":"False Positive","comment":"","start":"2017-12-11 07:11:29 America\/Phoenix","end":"2017-12-11 08:11:29 America\/Phoenix"}}))
    cl.make_request(method='POST', path='api_jsonrpc.php',data=json.dumps({"key":"","jsonrpc":"2.0","method":"event.get","params":{"output":"json"}}))

    # cl.make_request(path='zabbix/api_jsonrpc.php',data=json.dumps({
    # "jsonrpc": "2.0",
    # "method": "host.get",
    # "params": {
    #     "output": "extend",
    #     "filter": {
    #         "groupids": [
    #             "12"
    #         ]
    #     }
    # },
    # "auth": "ff9b9ee55d1b0853172942af45c1a023",
    # "id": 1}))

#     cl.make_request(path='zabbix/api_jsonrpc.php',data=json.dumps({
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "mbilichenko",
#         "password": "qwerty"
#     },
#     "id": 1,
#     "auth": None
#
# } ))
