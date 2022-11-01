import time

from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests_project.files.test_data import *
from framework.elements.text import Text
from framework.elements.link import Link
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.elements.form import Form
from framework.utils.random_util import *
from framework.browser.browser import Browser
from framework.scripts.scripts_js import CLOSE_POP_UP
from tests_project.files.test_data import *


class MainPage(BasePage):
    HEADER_LOCATOR = (By.XPATH, "//ol[@class='breadcrumb']")
    FOOTER_TEXT_LOCATOR = (By.XPATH, "//p[contains(@class, 'footer-text')]/span")
    ADD_PROJECT_BUTTON = (By.XPATH, "//button[@data-target='#addProject']")
    PROJECT_LOCATOR = (By.XPATH, "//a[contains(@href, 'allTests?projectId=')][text()='{}']")

    # Add Project Form
    PROJECT_FORM_LOCATOR = (By.XPATH, "//form[@id='addProjectForm']")
    PROJECT_NAME_INPUT_LOCATOR = (By.XPATH, "//input[@id='projectName']")
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    ALERT_MESSAGE_TEXT_LOCATOR = "//div[contains(@class, 'alert-success')][contains(text(), '{}')]"
    CLOSE_ADD_PROJECT_FORM_LOCATOR = (By.XPATH, "//form[@id='addProjectForm']/button[@type='button']")

    def __init__(self):
        self.locator = self.HEADER_LOCATOR[1]
        self.page_name = 'Main Wrapper'
        self.search_condition = self.HEADER_LOCATOR[0]

    def is_right_number_in_the_footer(self):
        version_text = Text(self.FOOTER_TEXT_LOCATOR[0], self.FOOTER_TEXT_LOCATOR[1], 'Footer Version').get_text()
        version_number = int(version_text.split(' ')[-1])
        return VARIANT_NUMBER == version_number

    def click_project_link(self, name=PROJECT_NAME):
        Link(self.PROJECT_LOCATOR[0], self.PROJECT_LOCATOR[1].format(name), f"{name} project").click()

    def click_add_button(self):
        Button(self.ADD_PROJECT_BUTTON[0], self.ADD_PROJECT_BUTTON[1], 'Add Project').click()

    def input_and_save_project_data(self, name=RandomUtils().get_random_word()):

        Browser().switch_to_frame_by_name('info')
        project_name_form = TextBox(self.PROJECT_NAME_INPUT_LOCATOR[0], self.PROJECT_NAME_INPUT_LOCATOR[1], "Project Name")
        project_name_form.wait_for_clickable()
        project_name_form.send_text(name)

        submit_button = Button(self.SUBMIT_BUTTON_LOCATOR[0], self.SUBMIT_BUTTON_LOCATOR[1], "Submit Project Creating")
        submit_button.click()

        return name

    def is_success_alert_message_presented(self, name):
        alert_message_locator = self.ALERT_MESSAGE_TEXT_LOCATOR.format(name)
        alert_message = Text(By.XPATH, alert_message_locator, "Alert Message")
        return alert_message.is_exist()

    def close_add_project_window(self):
        Browser().switch_to_default_content()
        Browser().get_driver().execute_script(CLOSE_POP_UP)

    def is_add_project_window_closed(self):
        project_form = Form(self.PROJECT_FORM_LOCATOR[0], self.PROJECT_FORM_LOCATOR[1], "Add Project")
        project_form.wait_for_is_absent()
        return not project_form.is_exist()

    def is_project_on_page(self, name):
        project_locator = self.PROJECT_LOCATOR[1].format(name)
        project_link = Link(self.PROJECT_LOCATOR[0], project_locator, f"{name} project")
        return project_link.is_exist()
