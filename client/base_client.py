import json

import requests


class BaseClient:
    def extract_response(self, response):
        if 'application/json' in response.headers['Content-Type']:
            return response.json(), response.status_code
        else:
            return response.text, response.status_code

    def get(self, url, params=None, headers=None):
        response = requests.get(url=url, params=params, headers=headers)
        return self.extract_response(response)

    def post(self, url, body=None, headers=None):
        if headers is None:
            headers = {}
        headers.update({"Content-Type": "application/json"})

        response = requests.post(url=url, data=json.dumps(body), headers=headers)
        return self.extract_response(response)

    def patch(self, url, body=None, headers=None):
        if headers is None:
            headers = {}
        headers.update({"Content-Type": "application/json"})

        response = requests.patch(url=url, data=json.dumps(body), headers=headers)
        return self.extract_response(response)

    def delete(self, url, params=None, headers=None):
        response = requests.delete(url=url, params=params, headers=headers)
        return self.extract_response(response)

