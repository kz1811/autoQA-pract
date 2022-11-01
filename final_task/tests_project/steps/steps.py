from selenium.webdriver.common.by import By
from framework.utils.config_parser import ConfigParser
from tests_project.files.test_data import *
from framework.elements.text import Text


class Steps:
    def get_authorize_url(self):
        url = ConfigParser().get_config()['url']
        url_parts = url.split(r'://')
        login = ConfigParser().get_config()['app_auth_creds']['auth_login']
        password = ConfigParser().get_config()['app_auth_creds']['auth_password']
        return url_parts[0] + r'://' + login + ":" + password + "@" + url_parts[1]

    def is_tests_sorted_by_datetime(self, tests):
        date_list = []
        for test in tests:
            date_list.append(test[6])

        if date_list.sort(reverse=True) is None:
            return True
        else:
            return False

    def get_tests_by_project_name(self, builder, project_name):
        tests = builder.get_tests_from_project(project_name)
        test_data = ()
        for test in tests:
            test_data += builder.get_test_data_by_name_and_start_time(test[0], test[1])

        return test_data

    def get_test_data_from_all_tests_page(self, locator):

        test_dict = {}

        test_dict['method_name'] = Text(By.XPATH, locator + '//td[2]', 'Test Method').get_text()
        test_dict['test_name'] = Text(By.XPATH, locator + '//td[1]', 'Test Name').get_text()

        result = Text(By.XPATH, locator + '//td[3]', 'Test Result').get_text()

        test_dict['status'] = result
        test_dict['start_time'] = Text(By.XPATH, locator + '//td[4]', 'Test Start Time').get_text()[:-2]

        test_dict['end_time'] = Text(By.XPATH, locator + '//td[5]', 'Test End Time').get_text()[:-2]
        if test_dict['end_time'] == '':
            test_dict['end_time'] = None

        return test_dict
