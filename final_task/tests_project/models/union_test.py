from framework.elements.text import Text
from selenium.webdriver.common.by import By
from tests_project.files.test_data import *


class UnionTest:

    def __init__(self):
        self.test_name = None
        self.method_name = None
        self.status = None
        self.start_time = None
        self.end_time = None
        self.environment = None
        self.project_name = None

    def __eq__(self, other):
        if isinstance(other, UnionTest):
            return (self.test_name == other.test_name and
                    self.method_name == other.method_name and
                    self.status == other.status and
                    self.start_time == other.start_time and
                    self.end_time == other.end_time and
                    self.environment == other.environment)

        return NotImplemented

    def get_test_data_from_db(self, test, compare_to_ui=True):
        self.test_name = test[1]
        self.method_name = test[3]
        self.project_id = test[4]
        self.start_time = str(test[6])
        self.environment = test[8]
        self.browser = test[9]

        if compare_to_ui:
            self.status = TEST_CODE_STATUSES_DICT[test[2]]
        else:
            self.status = test[2]

        if test[7] is None:
            self.end_time = None
        else:
            self.end_time = str(test[7])

    def get_test_data_from_dict(self, test):
        self.test_name = test['test_name']
        self.method_name = test['method_name']
        self.status = test['status']
        self.start_time = test['start_time']
        self.project_id = test.get('project_id')
        self.environment = test.get('environment')
        self.browser = test.get('browser')

        if test.get('project_name') is not None:
            self.project_name = test['project_name']

        if test.get('end_time') is None:
            self.end_time = None
        else:
            self.end_time = str(test['end_time'])

