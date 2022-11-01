import os

from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.link import Link
from framework.elements.button import Button
from framework.elements.checkbox import CheckBox
from framework.utils.autoit_utils import AutoItUtils


class SecondGameCard(BasePage):

    BASE_ELEMENT = (By.CLASS_NAME, "avatar-and-interests")
    UPLOAD_LINK = (By.CLASS_NAME, "avatar-and-interests__upload-button")
    DOWNLOAD_BUTTON = (By.XPATH, "//button[contains(@class, 'upload-button')]")
    UNSELECT_ALL_CHECKBOX = (By.XPATH, "//label[contains(@for, 'unselectall')]")
    PONIES_CHECKBOX = (By.XPATH, "//label[contains(@for, 'ponies')]")
    POLO_CHECKBOX = (By.XPATH, "//label[contains(@for, 'polo')]")
    DOUGH_CHECKBOX = (By.XPATH, "//label[contains(@for, 'dough')]")
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'Next')]")

    def __init__(self, search_condition=BASE_ELEMENT[0], locator=BASE_ELEMENT[1], page_name='Second Card Form'):
        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition

    def download_and_upload_image(self):
        upload_link = Link(self.UPLOAD_LINK[0], self.UPLOAD_LINK[1], 'upload')
        upload_link.click()

        AutoItUtils().upload_image('Open', os.getcwd()+"\\files\\avatar.png")

    def pick_three_interests(self):
        unselect_all_checkbox = CheckBox(self.UNSELECT_ALL_CHECKBOX[0], self.UNSELECT_ALL_CHECKBOX[1], "unselect-all")
        unselect_all_checkbox.scroll_by_script()
        unselect_all_checkbox.click()

        ponies_checkbox = CheckBox(self.PONIES_CHECKBOX[0], self.PONIES_CHECKBOX[1], "ponies")
        ponies_checkbox.click()

        polo_checkbox = CheckBox(self.POLO_CHECKBOX[0], self.POLO_CHECKBOX[1], "polo")
        polo_checkbox.click()

        dough_checkbox = CheckBox(self.DOUGH_CHECKBOX[0], self.DOUGH_CHECKBOX[1], "dough")
        dough_checkbox.click()

    def click_next_button(self):
        next_button = Button(self.NEXT_BUTTON_LOCATOR[0], self.NEXT_BUTTON_LOCATOR[1], 'next')
        next_button.click()
