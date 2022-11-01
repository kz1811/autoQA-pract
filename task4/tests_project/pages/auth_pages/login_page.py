from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.button import Button
from tests_project.files import credentials


class LoginPage(BasePage):

    LOGIN_FIELD_LOCATOR = (By.ID, 'index_email')
    SIGN_IN_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "signInButton")]')

    def __init__(self, page_name=' Auth Login Page'):
        self.locator = self.LOGIN_FIELD_LOCATOR[1]
        self.page_name = page_name
        self.search_condition = self.LOGIN_FIELD_LOCATOR[0]

    def send_login(self):

        login_field = TextBox(self.LOGIN_FIELD_LOCATOR[0], self.LOGIN_FIELD_LOCATOR[1], 'login')
        login_field.send_keys(credentials.LOGIN)
        sign_in_button = Button(self.SIGN_IN_BUTTON_LOCATOR[0], self.SIGN_IN_BUTTON_LOCATOR[1], "sign in")
        sign_in_button.click()

