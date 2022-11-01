from selenium.webdriver.common.by import By
from tests_project.models.union_test import UnionTest
from framework.pages.base_page import BasePage
from framework.elements.link import Link
from tests_project.steps.steps import Steps


class ProjectPage(BasePage):

    TEST_TABLE_LOCATOR = (By.XPATH, "//table[@class='table']//th[text()='Test name']")
    TEST_LINK_LOCATOR = "//a[contains(@href, 'testInfo?testId')][text()='{}']"
    ADD_TEST_BUTTON_LOCATOR = (By.XPATH, "//button[@data-target='#addTest']")
    TABLE_TEST_RECORD_LOCATOR = "//table[@class='table']//tr[{}]"

    def __init__(self, page_name):
        self.locator = self.TEST_TABLE_LOCATOR[1]
        self.page_name = page_name
        self.search_condition = self.TEST_TABLE_LOCATOR[0]

    def is_test_on_page(self, test):
        test_from_ui = UnionTest()
        test_ui_dict = Steps().get_test_data_from_all_tests_page(self.TABLE_TEST_RECORD_LOCATOR.format(2))
        test_from_ui.get_test_data_from_dict(test_ui_dict, )

        return test == test_from_ui

    def is_tests_same(self, tests):
        for i in range(len(tests)):
            test_from_db = UnionTest()
            test_from_db.get_test_data_from_db(tests[i])
            test_from_db.browser, test_from_db.project_id, test_from_db.environment = None, None, None

            test_from_ui = UnionTest()
            test_ui_dict = Steps().get_test_data_from_all_tests_page(self.TABLE_TEST_RECORD_LOCATOR.format(i+2))
            test_from_ui.get_test_data_from_dict(test_ui_dict, )

            if test_from_db != test_from_ui:
                return False
        return True

    def click_to_test_link(self, test):
        test_link_locator = self.TEST_LINK_LOCATOR.format(test.test_name)
        Link(By.XPATH, test_link_locator, 'test').click()
