from framework.utils.config_parser import ConfigParser
from framework.constants.http_status_codes import OK
from urllib.parse import urljoin
import requests


class ClientApi:
    host = ConfigParser().get_config()['url_api']

    def send_get_request(self, host=host, json=None, endpoint='', expected_code=OK):

        url = urljoin(host, endpoint)

        if json is None:
            json = {}

        answer = requests.get(url, json=json, files=files, data=data)

        assert answer.status_code == expected_code, f"Status code is wrong. Expected: {expected_code} Received: {answer.status_code}"
        return answer

    def send_post_request(self, host=host, endpoint='', json=None, files=None, data=None, expected_code=OK):

        url = urljoin(host, endpoint)

        if files is None:
            files = {}

        if json is None:
            json = {}

        if data is None:
            data = {}

        answer = requests.post(url, json=json, files=files, data=data)

        assert answer.status_code == expected_code, f"Status code is wrong. Expected: {expected_code} Received: {answer.status_code}"
        return answer

