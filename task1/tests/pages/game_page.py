from framework.elements.checkbox import CheckBox
from framework.elements.dropdown import Dropdown
from framework.elements.link import Link
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.button import Button
from framework.elements.text import Text
from framework.elements.form import Form
from framework.utils import random_util
from tests.pages.first_game_card import FirstGameCard
from tests.pages.second_game_card import SecondGameCard
from tests.pages.third_game_card import ThirdGameCard


class GamePage(BasePage):

    TIMER_LOCATOR = (By.CLASS_NAME, "timer")

    HIDE_FORM_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'help-form__send-to-bottom-button')]")
    HELP_FORM_TEXT_BOX_LOCATOR = (By.CLASS_NAME, "help-form__title")
    COOKIES_HEADER_LOCATOR = (By.CLASS_NAME, "cookies")
    ACCEPT_COOKIES_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'really')]")

    def __init__(self, search_condition=TIMER_LOCATOR[0], locator=TIMER_LOCATOR[1], page_name='Game Page'):
        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition

    def hide_help_form(self):
        hide_form_button = Button(self.HIDE_FORM_BUTTON_LOCATOR[0], self.HIDE_FORM_BUTTON_LOCATOR[1], 'hide form')
        hide_form_button.click()

        help_form_title = Text(self.HELP_FORM_TEXT_BOX_LOCATOR[0], self.HELP_FORM_TEXT_BOX_LOCATOR[1], 'help form')
        help_form_title.wait_for_invisibility()

        return not help_form_title.is_displayed()

    def accept_cookies(self):

        accept_cookie_button = Button(self.ACCEPT_COOKIES_BUTTON_LOCATOR[0], self.ACCEPT_COOKIES_BUTTON_LOCATOR[1], 'accept cookie')
        accept_cookie_button.click()

        cookies_header = Form(self.COOKIES_HEADER_LOCATOR[0], self.COOKIES_HEADER_LOCATOR[1], 'cookies header')
        cookies_header.wait_for_is_absent()

        return not cookies_header.is_displayed()

    def get_timer(self):
        timer = Text(self.TIMER_LOCATOR[0], self.TIMER_LOCATOR[1], 'timer')
        return timer.get_text()

    @property
    def first_card(self):
        return FirstGameCard()

    @property
    def second_card(self):
        return SecondGameCard()

    @property
    def third_card(self):
        return ThirdGameCard()
