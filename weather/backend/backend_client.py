import json
import requests
import inspect


class BackendClient:
    def __init__(self, base_url, key):
        self.base_url = base_url
        self.key = key
        self.params = {"APPID":self.key}

    @classmethod
    def setUpClass(cls):
        cls.client = BackendClient("http://api.openweathermap.org", "09fba9e487af0fd5558b8e6ac9da0b56")



    def make_request(self, path, parameters=None):
        if parameters:
            self.params.update(parameters)
        url = self.base_url + '/data/2.5/' + path

        response = requests.get(url, params=self.params)
        return {"body": response.json(), "status_code": response.status_code}

    @staticmethod
    def read_config():
        import configparser
        import sys
        config = configparser.ConfigParser()
        import pdb;pdb.set_trace()
        if not config.read("config.conf") and not config.read(sys.path[0] + "/" + "config.conf"):

                config.read(sys.path[0] + "/weather/backend/" + "config.conf")
        return config

