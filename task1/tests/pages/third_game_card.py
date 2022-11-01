from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ThirdGameCard(BasePage):

    BASE_ELEMENT = (By.CLASS_NAME, "personal-details")

    def __init__(self, search_condition=BASE_ELEMENT[0], locator=BASE_ELEMENT[1], page_name='Third Card Form'):
        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition
