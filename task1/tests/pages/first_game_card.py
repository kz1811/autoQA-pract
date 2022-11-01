from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.utils import random_util
from framework.elements.text_box import TextBox
from framework.elements.dropdown import Dropdown
from framework.elements.link import Link
from framework.elements.checkbox import CheckBox


class FirstGameCard(BasePage):

    BASE_ELEMENT = (By.CLASS_NAME, "login-form__container")
    PASSWORD_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Password')]")
    EMAIL_FIELD = (By.XPATH, "//input[contains(@placeholder, 'email')]")
    DOMAIN_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Domain')]")
    DOMAIN_DROPDOWN_HEADER = (By.XPATH, "//div[@class ='dropdown__field'][contains(text(), 'other')]")
    DROPDOWN_ELEMENT = (By.XPATH, "//div[contains(@class, 'dropdown__list-item')][contains(text(), 'org')]")
    NEXT_LINK = (By.XPATH, "//a[@class='button--secondary'][contains(text(), 'Next')]")
    TERMS_CHECKBOX = (By.CLASS_NAME, "checkbox")

    def __init__(self, search_condition=BASE_ELEMENT[0], locator=BASE_ELEMENT[1], page_name='First Card Form'):
        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition

    def fill_and_submit_the_card(self):
        random_data = random_util.get_random_password_and_email()

        pass_field = TextBox(self.PASSWORD_FIELD[0], self.PASSWORD_FIELD[1], 'password')
        pass_field.clear_field()
        pass_field.send_keys(random_data[0])

        email_field = TextBox(self.EMAIL_FIELD[0], self.EMAIL_FIELD[1], 'email')
        email_field.clear_field()
        email_field.send_keys(random_data[1])

        domain_field = TextBox(self.DOMAIN_FIELD[0], self.DOMAIN_FIELD[1], 'domain')
        domain_field.clear_field()
        domain_field.send_keys(random_data[2])

        domain_dropdown = Dropdown(self.DOMAIN_DROPDOWN_HEADER[0], self.DOMAIN_DROPDOWN_HEADER[1], 'domain')
        domain_dropdown.click()

        domain_dropdown_elements = Dropdown(self.DROPDOWN_ELEMENT[0], self.DROPDOWN_ELEMENT[1], 'domain element')
        domain_dropdown_elements.click()

        terms_checkbox = CheckBox(self.TERMS_CHECKBOX[0], self.TERMS_CHECKBOX[1], 'terms&conditions')
        terms_checkbox.click()

        button = Link(self.NEXT_LINK[0], self.NEXT_LINK[1], 'Next')
        button.click()
