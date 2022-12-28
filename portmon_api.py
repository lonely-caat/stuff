import requests
from json import decoder


def make_request(path, method='get', parameters = None):
    url = 'http://localhost:8012/'+path
    request = getattr(requests, method.lower())

    if parameters is None:
        parameters = {}

    try:
        return request(url,params=parameters).json()
    except decoder.JSONDecodeError:
        print(request(url, params=parameters).status_code),print(request(url, params=parameters).text)



make_request('/port/rules','get')
make_request('/port/1/rules', 'post')
make_request('/port/rules', 'post')

##GETS:
"""
status
/port/rules	

"""