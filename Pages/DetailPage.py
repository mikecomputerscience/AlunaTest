import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DetailPage(BasePage):
    # By locators - Object Repository
    back_link = (By.LINK_TEXT, 'Back')
    result_title = (By.ID, 'result_title')
    result_detail = (By.ID, 'result_detail')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.WEB_BASE_URL)

    def is_back_link_visible(self):
        return self.is_visible(self.back_link)

    def click_back_link(self):
        self.driver.back()
        # self.do_click(self.back_link)

    def get_result_title(self):
        self.get_element_text(self.result_title)
        time.sleep(1)

    def get_result_detail(self):
        self.get_element_text(self.result_detail)
        time.sleep(1)
