from properties import host,username,password,api_host,api_key,m3_api_host
from zabbixcl import ZabbixClient

class Auth(ZabbixClient):
    def __init__(self):
        self.host = host
        self.username = username
        self.password = password
        self.api = api_host
        self.api_key = api_key
        self.m3_api_host = m3_api_host

    @staticmethod
    def get_auth_token():
        cl = ZabbixClient('http://zabbix-command01.dev.phx7.llnw.net')
        resp = cl.make_request(path='api_jsonrpc.php', body={
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "zabbix-api-limon-qa",
                "password": "YuN0cH4nGem3%"
            },
            "id": 1,
        })
        return resp[0]['result']

if __name__ == '__main__':
    a = Auth()
    print a.get_auth_token()