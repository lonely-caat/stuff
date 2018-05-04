from properties import host,username,password,api_host,api_key,m3_api_host
from base_request import BaseRequest


class Auth(BaseRequest):
    def __init__(self):
        self.host = host
        self.username = username
        self.password = password
        self.api = api_host
        self.api_key = api_key
        self.m3_api_host = m3_api_host

    def get_auth_token(self):
        cli = BaseRequest(self.api)
        res= cli.make_request(path='api_jsonrpc.php', data={ "jsonrpc": "2.0", "method": "user.login", "params": { "user": self.username, "password": self.password }, "id": 1 })
        return res[0]


if __name__ == '__main__':
    a = Auth()
    print a.get_auth_token()