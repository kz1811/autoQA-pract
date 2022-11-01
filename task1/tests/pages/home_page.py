from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.link import Link


class HomePage(BasePage):
    GO_TO_GAME_PAGE_LINK_LOCATOR = (By.CLASS_NAME, "start__link")

    def __init__(self, search_condition=GO_TO_GAME_PAGE_LINK_LOCATOR[0], locator=GO_TO_GAME_PAGE_LINK_LOCATOR[1],
                 page_name='Home Page'):

        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition

    def click_here_link(self):
        link = Link(self.GO_TO_GAME_PAGE_LINK_LOCATOR[0], self.GO_TO_GAME_PAGE_LINK_LOCATOR[1], 'Here')
        link.click()
