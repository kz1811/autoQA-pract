from framework.api.client_api import ClientApi
from framework.constants.http_status_codes import OK, CREATED


class JsonPlaceholderApi:

    def get_user_data_by_id(self, user_id, expected_code=OK):
        endpoint = f'/users/{user_id}'
        return ClientApi().send_get_request(endpoint=endpoint, expected_code=expected_code)

    def get_all_users_data(self, expected_code=OK):
        endpoint = '/users'
        return ClientApi().send_get_request(endpoint=endpoint, expected_code=expected_code)

    def get_post_by_id(self, post_id, expected_code=OK):
        endpoint = f'/posts/{post_id}'
        return ClientApi().send_get_request(endpoint=endpoint, expected_code=expected_code)

    def get_all_posts(self, expected_code=OK):
        endpoint = '/posts'
        return ClientApi().send_get_request(endpoint=endpoint, expected_code=expected_code)

    def create_post(self, json, expected_code=CREATED):
        endpoint = '/posts'
        return ClientApi().send_post_request(endpoint=endpoint, json=json, expected_code=expected_code)

