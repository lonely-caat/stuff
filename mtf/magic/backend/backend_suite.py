import pytest
import requests
from http.cookiejar import Cookie

class BackendSuite(pytest):
    def __init__(self, url, **kwargs):
        self.kwargs = kwargs
        self.cookies = []
        self.host = 'https://api.shodan.io'
        self.api_key = 'cn1GFeeca71RwAH2ShOxWm96yz43Hspg'


    def request_api(self, method_name, path, **kwargs):
        request = getattr(requests,method_name)
        url = self.host+'/'+path

        # Fill content-type if we are missing one:
        headers = {}.setdefault('headers', {})
        if (method_name.lower() in ('post', 'put', 'trace', 'patch') and
                    'content-type' not in (h.lower() for h in headers)):
            headers['Content-Type'] = 'application/json'

        headers['x-requested-with'] = 'XMLHttpRequest'
        if self.cookies:
            headers['Cookie'] = '; '.join(self.cookies)

        request(url,headers)


    def add_cookie(self, data):
        """Add cookie string to the cookies"""
        self.cookies.append(data)

    def add_cookies_from_headers(self, data):
        c = Cookie(data)
        for x in c.value():
            self.add_cookie('%s=%s' % (x.key, x.coded_value))

    def login(self, username, password):
        """The wrapper around login call that would set cookies for the farther usage"""
        token_resp = self.get_auth_token()
        assert token_resp.status_code == 200
        login_resp = self.post_auth_login(json={'csrf_token': token_resp.text,
                                                'email': username,
                                                'password': password,
                                                'rememberMe': True})
        if login_resp.status_code == 200:
            self.add_cookies_from_headers(login_resp.headers['Set-Cookie'])
        return login_resp
