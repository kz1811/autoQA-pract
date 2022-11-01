from framework.utils.image_utils import ImageUtils
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text import Text
from tests_project.files.test_data import *
from framework.utils.config_parser import ConfigParser
from framework.elements.link import Link
from framework.utils.file_util import File
from tests_project.models.union_test import UnionTest


class TestPage(BasePage):
    PARTIAL_TEST_NAME_LOCATOR = "//ol[@class='breadcrumb']/li[contains(text(), '{}')]"
    PROJECT_NAME_LOCATOR = (By.XPATH, "//h4[text()='Project name']/../p[@class='list-group-item-text']")
    TEST_NAME_LOCATOR = (By.XPATH, "//h4[text()='Test name']/../p[@class='list-group-item-text']")
    TEST_METHOD_NAME_LOCATOR = (By.XPATH, "//h4[text()='Test method name']/../p[@class='list-group-item-text']")
    TEST_STATUS_LOCATOR = (By.XPATH, "//h4[text()='Status']/../p[@class='list-group-item-text']")
    BROWSER_LOCATOR = (By.XPATH, "//h4[text()='Browser']/../p[@class='list-group-item-text']")
    ENV_LOCATOR = (By.XPATH, "//h4[text()='Environment']/../p[@class='list-group-item-text']")
    TEST_START_TIME_LOCATOR = (By.XPATH, "//h4[text()='Time info']/../p[@class='list-group-item-text']")
    TEST_END_TIME_LOCATOR = (By.XPATH, "//h4[text()='Time info']/../p[@class='list-group-item-text'][2]")
    TEST_SCREENSHOT_LOCATOR = (By.XPATH, "//img[@class='thumbnail']/..")
    LOGS_LOCATOR = (By.XPATH, "//div[text()='Logs']/../table")

    def __init__(self, test_name):
        self.locator = self.PARTIAL_TEST_NAME_LOCATOR.format(test_name[:30])
        self.page_name = f'{test_name}'
        self.search_condition = By.XPATH

    def get_test_data_dict(self, client):

        test_ui_data = {}
        test_ui_data['project_name'] = Text(self.PROJECT_NAME_LOCATOR[0], self.PROJECT_NAME_LOCATOR[1],
                                            'project name').get_text()
        test_ui_data['project_id'] = client.get_project_id_by_project_name(test_ui_data['project_name'])
        test_ui_data['test_name'] = Text(self.TEST_NAME_LOCATOR[0], self.TEST_NAME_LOCATOR[1], "test name").get_text()
        test_ui_data['method_name'] = Text(self.TEST_METHOD_NAME_LOCATOR[0], self.TEST_METHOD_NAME_LOCATOR[1],
                                           'test method name').get_text()
        test_ui_data['status'] = Text(self.TEST_STATUS_LOCATOR[0], self.TEST_STATUS_LOCATOR[1],
                                      "test status").get_text()
        test_ui_data['environment'] = Text(self.ENV_LOCATOR[0], self.ENV_LOCATOR[1], "test environment").get_text()
        test_ui_data['browser'] = Text(self.BROWSER_LOCATOR[0], self.BROWSER_LOCATOR[1], "test browser").get_text()

        start_time = Text(self.PROJECT_NAME_LOCATOR[0], self.TEST_START_TIME_LOCATOR[1], "test start time")
        test_ui_data['start_time'] = start_time.get_text().split('Start time: ')[1][:-2]

        end_time_elem = Text(self.PROJECT_NAME_LOCATOR[0], self.TEST_END_TIME_LOCATOR[1], "test end time")
        end_time = end_time_elem.get_text()

        if len(end_time.split('End time: ')) == 1:
            test_ui_data['end_time'] = None
        else:
            test_ui_data['end_time'] = end_time.split('End time: ')[1][:-2]
        return test_ui_data

    def is_fields_of_test_valid(self, client, test):
        test_data = client.get_test_data_by_name_and_start_time(test.test_name, test.start_time)

        test_db = UnionTest()
        test_db.get_test_data_from_db(test_data[0], compare_to_ui=True)
        test_db.project_name = client.get_project_name_by_project_id(test_db.project_id)

        test_ui = UnionTest()
        test_data_ui = self.get_test_data_dict(client)
        test_ui.get_test_data_from_dict(test_data_ui)

        return test_db == test_ui

    def is_test_screenshot_valid(self, screenshot_path):
        photo_link = Link(self.TEST_SCREENSHOT_LOCATOR[0], self.TEST_SCREENSHOT_LOCATOR[1], "photo").get_href()
        File().write_file_from_base64(file_path=SAVE_SCREENSHOT_PATH, source=photo_link)
        return ImageUtils().compare_images(screenshot_path, SAVE_SCREENSHOT_PATH)
