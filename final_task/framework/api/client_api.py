from framework.utils.config_parser import ConfigParser
import requests
from framework.constants.http_status_codes import OK, CREATED


class ClientApi:
    host = ConfigParser().get_config()['url_api']

    def send_get_request(self, host=host, endpoint='', json=None, expected_code=CREATED):

        url = host + endpoint

        if json is None:
            json = {}

        answer = requests.get(url, json=json)

        assert answer.status_code == expected_code, f"Status code is wrong. Expected: {expected_code} Received: {answer.status_code}"
        return answer

    def send_post_request(self, host=host, endpoint='', json=None, data=None, expected_code=CREATED):

        url = host + endpoint

        if json is None:
            json = {}

        if data is None:
            data = {}

        answer = requests.post(url, json=json, data=data)

        assert answer.status_code == expected_code, f"Status code is wrong. Expected: {expected_code} Received: {answer.status_code}"
        return answer
