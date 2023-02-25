import time

import pytest

from Config.config import TestData
from Pages.DetailPage import DetailPage
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class Test_DetailPage(BaseTest):

    @pytest.mark.ui
    @pytest.mark.third
    def test_detail_page_title(self):
        self.home_page = HomePage(self.driver)
        time.sleep(1)
        self.home_page.enter_identifier(TestData.VALID_ID_0)
        time.sleep(1)
        self.home_page.click_find_patient_button()
        time.sleep(1)
        self.detail_page = DetailPage(self.driver)
        time.sleep(1)
        actual_detail_page_title = self.detail_page.get_title()
        if TestData.DETAIL_PAGE_TITLE == actual_detail_page_title:
            print("Detail page title is correct! That's good!")
            assert True
            print('Pass: test_detail_page_title')
        else:
            print('Expected detail page title is ' + TestData.DETAIL_PAGE_TITLE)
            print('However, actual title is ' + actual_detail_page_title)
            print('Fail: test_detail_page_title. Reason: detail page title mismatch.')
            assert False

    @pytest.mark.ui
    @pytest.mark.third
    def test_back_link(self):
        self.home_page = HomePage(self.driver)
        time.sleep(1)
        self.home_page.enter_identifier(TestData.VALID_ID_0)
        time.sleep(1)
        self.home_page.click_find_patient_button()
        time.sleep(1)
        self.detail_page = DetailPage(self.driver)
        if self.detail_page.is_back_link_visible():
            print("Back link found! That's good!")
            self.detail_page.click_back_link()
            actual_home_page_title = self.home_page.get_title()
            if TestData.HOME_PAGE_TITLE == actual_home_page_title:
                print("Home page title is correct! That's good!")
                assert True
                print('Pass: test_back_link')
            else:
                print('Expected home page title is ' + TestData.HOME_PAGE_TITLE)
                print('However, actual title is ' + actual_home_page_title)
                print('Fail: test_back_link. Reason: home page title mismatch.')
                assert False
        else:
            print('Fail: test_back_link. Reason: back link not visible.')
            assert False
