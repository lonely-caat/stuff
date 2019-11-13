import requests

class BackendClient:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.params = {"APPID":self.key}


    def make_request(self, path, parameters=None):

        if parameters:
            self.params.update(parameters)
        url = self.url + '/' + path
        response = requests.get(url=url, params=self.params)

        try:
            return{"code":response.status_code, "body":response.json()}
        except ValueError:
            return [response.status_code, response.text]

