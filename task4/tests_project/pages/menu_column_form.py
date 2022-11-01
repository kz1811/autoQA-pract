from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.link import Link


class MenuForm(BasePage):

    MY_PAGE_LOCATOR = (By.ID, "l_pr")

    def __init__(self, page_name='Main Form'):
        self.locator = self.MY_PAGE_LOCATOR[1]
        self.page_name = page_name
        self.search_condition = self.MY_PAGE_LOCATOR[0]

    def click_to_my_page_item(self):
        my_page_item = Link(self.MY_PAGE_LOCATOR[0], self.MY_PAGE_LOCATOR[1], 'my page')
        my_page_item.click()
