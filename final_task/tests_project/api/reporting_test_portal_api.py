from framework.api.client_api import ClientApi
from tests_project.files.test_data import *
from framework.constants.http_status_codes import *


class ReportingTestPortalApi:

    def get_token(self, variant=VARIANT_NUMBER, expected_code=OK):
        endpoint = "/token/get"
        return ClientApi().send_post_request(endpoint=endpoint, data={"variant": variant}, expected_code=expected_code).text
