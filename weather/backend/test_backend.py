from .backend_client import BackendClient
import inspect

# class TestBackend(BackendClient):
#     def __init__(self,base_url, key):
#         super().__init__(base_url, key)
#         config = self.read_config()
# client = BackendClient(config['backend']['host'], config['backend']['key'])



class TestBackend2(BackendClient):
    def test_weather_by_city(self):


        response = self.client.make_request('weather', {"q":"London"})

        assert response['body']['cod'] == 200, "Expected Status 200"


