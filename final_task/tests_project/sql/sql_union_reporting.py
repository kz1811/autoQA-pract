from datetime import datetime
from framework.utils.file_util import File
from framework.utils.random_util import RandomUtils
from framework.utils.config_parser import ConfigParser
from tests_project.models.union_test import UnionTest
from tests_project.files.queries import *
from tests_project.files.test_data import *


class SqlUnionReporting:

    def __init__(self, mysql_client):
        self.client = mysql_client

    def get_tests(self):
        return self.client.execute_query(GET_TESTS_DATA, True)

    def get_project_id_by_project_name(self, project_name):
        return self.client.execute_query(GET_PROJECT_DATA_BY_NAME_QUERY.format(project_name), True)[0][0]

    def get_project_name_by_project_id(self, project_id):
        return self.client.execute_query(GET_PROJECT_NAME_BY_ID.format(project_id), True)[0]

    def get_tests_from_project(self, project_name):
        project_id = self.get_project_id_by_project_name(project_name)
        return self.client.execute_query(GET_TESTS_BY_PROJECT_ID_QUERY.format(project_id, LIMIT_TESTS_ON_PAGE), True)

    def get_test_data_by_name_and_start_time(self, name, start_time):
        return self.client.execute_query(GET_TEST_DATA_BY_NAME_AND_START_TIME.format(name, start_time), True)

    def create_test(self, test_name, method_name, start_time, project_id, status_id, session_id, env, browser):
        self.client.execute_query(CREATE_TEST_QUERY.format(test_name, method_name, start_time, project_id,
                                                           status_id, session_id, env, browser))

    def get_test_id_by_test_data(self, test_name, method_name, status_id, start_time, session_id, browser, env):
        return self.client.execute_query(GET_TEST_ID_BY_TEST_DATA.format(test_name, method_name, status_id,
                                                                         start_time, session_id,
                                                                         browser, env), fetch=True)[0]

    def attach_logs(self, test_id, logs_string):
        self.client.execute_query(ATTACH_LOG, args=(logs_string, test_id))

    def attach_screenshot(self, test_id, screenshot_path):
        screenshot_string = File().convert_file_to_binary(screenshot_path)
        self.client.execute_query(ATTACH_SCREENSHOT, args=(screenshot_string, test_id))

    def add_test(self, project_name, test_name=RandomUtils().get_random_word(),
                 method_name=RandomUtils().get_random_word(),
                 start_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), screenshot=None,
                 logs=RandomUtils().get_random_word()):
        project_id = self.get_project_id_by_project_name(project_name)

        status_id = TEST_STATUS_ID
        session_id = SESSION_ID
        env = RandomUtils().get_random_word()
        browser = ConfigParser().get_config()['browser']

        self.create_test(test_name, method_name, start_time, project_id, status_id, session_id, env, browser)

        test_id = self.get_test_id_by_test_data(test_name, method_name, status_id, start_time, session_id, browser, env)

        self.attach_screenshot(test_id, screenshot)

        logs_string = File().read_from_file(logs)
        self.attach_logs(test_id, logs_string)

        test_model = UnionTest()
        test_dict = {'test_name': test_name, 'method_name': method_name,
                     'status': TEST_CODE_STATUSES_DICT[status_id], 'start_time': start_time}

        test_model.get_test_data_from_dict(test_dict)

        return test_model
