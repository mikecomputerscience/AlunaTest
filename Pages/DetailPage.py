import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DetailPage(BasePage):
    # By locators - Object Repository
    back_link = (By.LINK_TEXT, '< Back')
    result_title = (By.ID, 'title')
    result_detail = (By.ID, 'detail')

    def __init__(self, driver):
        super().__init__(driver)

    def is_back_link_visible(self):
        return self.is_visible(self.back_link)

    def click_back_link(self):
        self.do_click(self.back_link)

    def get_result_title(self):
        time.sleep(1)
        try:
            return self.get_element_text(self.result_title)
        except Exception as e:
            return ''

    def get_result_detail(self):
        time.sleep(1)
        try:
            return self.get_element_text(self.result_detail)
        except Exception as e:
            return ''
