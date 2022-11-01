from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from tests_project.files import credentials


class PasswPage(BasePage):

    PASSWORD_FIELD_LOCATOR = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")

    def __init__(self, page_name='Password Page'):
        self.locator = self.PASSWORD_FIELD_LOCATOR[1]
        self.page_name = page_name
        self.search_condition = self.PASSWORD_FIELD_LOCATOR[0]

    def send_password(self):
        password_field = TextBox(self.PASSWORD_FIELD_LOCATOR[0], self.PASSWORD_FIELD_LOCATOR[1], 'password')
        password_field.send_keys(credentials.PASSWORD)
        submit_button = Button(self.SUBMIT_BUTTON_LOCATOR[0], self.SUBMIT_BUTTON_LOCATOR[1], 'submit password')
        submit_button.click()
