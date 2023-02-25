import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    # By locators - Object Repository
    identifier_textbox = (By.ID, 'identifier')
    find_patient_button = (By.ID, 'submit')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.WEB_BASE_URL)

    def get_home(self):
        self.driver.get(TestData.WEB_BASE_URL)

    def enter_identifier(self, identifier):
        self.do_clear_textbox(self.identifier_textbox)
        time.sleep(1)
        self.do_send_key(self.identifier_textbox, identifier)

    def click_find_patient_button(self):
        self.do_click(self.find_patient_button)
