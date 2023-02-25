import time

import pytest

from Config.config import TestData
from Pages.DetailPage import DetailPage
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class Test_HomePage(BaseTest):

    @pytest.mark.ui
    @pytest.mark.third
    def test_home_page_title(self):
        self.home_page = HomePage(self.driver)
        time.sleep(1)
        actual_home_page_title = self.home_page.get_title()
        if TestData.HOME_PAGE_TITLE == actual_home_page_title:
            print("Home page title is correct! That's good!")
            assert True
            print('Pass: test_home_page_title')
        else:
            print('Expected home page title is ' + TestData.HOME_PAGE_TITLE)
            print('However, actual title is ' + actual_home_page_title)
            print('Fail: test_home_page_title. Reason: home page title mismatch.')
            assert False

    @pytest.mark.ui
    @pytest.mark.third
    def test_homepage_valid_id_0(self):
        self.home_page = HomePage(self.driver)
        time.sleep(1)
        self.home_page.enter_identifier(TestData.VALID_ID_0)
        time.sleep(1)
        self.home_page.click_find_patient_button()
        time.sleep(1)
        self.detail_page = DetailPage(self.driver)
        actual_title = self.detail_page.get_result_title()
        actual_detail = self.detail_page.get_result_detail()
        expected_name = 'Name: ' + TestData.VALID_ID_0_NAME
        expected_dob = 'DOB: ' + TestData.VALID_ID_0_DOB
        expected_gender = 'Gender: ' + TestData.VALID_ID_0_GENDER
        if TestData.DEFAULT_PATIENT_FOUND_TITLE == actual_title:
            print("Patient found! That's good!")
            if expected_name in actual_detail:
                print("Patient name matched! That's good!")
                if expected_dob in actual_detail:
                    print("Patient dob matched! That's good!")
                    if expected_gender in actual_detail:
                        print("Patient gender matched! That's good!")
                        assert True
                        print('Pass: test_homepage_valid_id_0')
                    else:
                        print(expected_gender + ' is not found in the patient detail ' + actual_detail)
                        print('Fail: test_homepage_valid_id_0. Reason: gender mismatch.')
                        assert False
                else:
                    print(expected_dob + ' is not found in the patient detail ' + actual_detail)
                    print('Fail: test_homepage_valid_id_0. Reason: dob mismatch.')
                    assert False
            else:
                print(expected_name + ' is not found in the patient detail ' + actual_detail)
                print('Fail: test_homepage_valid_id_0. Reason: name mismatch.')
                assert False

        else:
            print('Expected title is ' + TestData.DEFAULT_PATIENT_FOUND_TITLE)
            print('However, actual title is ' + actual_title)
            print('Fail: test_homepage_valid_id_0. Reason: title mismatch.')
            assert False

    @pytest.mark.ui
    @pytest.mark.third
    def test_homepage_invalid_id_0(self):
        self.home_page = HomePage(self.driver)
        time.sleep(1)
        self.home_page.enter_identifier(TestData.INVALID_ID_0)
        time.sleep(1)
        self.home_page.click_find_patient_button()
        time.sleep(1)
        self.detail_page = DetailPage(self.driver)
        actual_title = self.detail_page.get_result_title()
        actual_detail = self.detail_page.get_result_detail()
        expected_detail = TestData.INVALID_ID_0
        if TestData.DEFAULT_PATIENT_NOT_FOUND_TITLE == actual_title:
            print("Patient NOT found! That's good for " + TestData.INVALID_ID_0 + "!")
            if expected_detail == actual_detail:
                print("Patient identifier " + expected_detail + "is shown on the detail page! That's good!")
                assert True
                print('Pass: test_homepage_invalid_id_0')
            else:
                print('Expected detail is ' + expected_detail)
                print('However, actual detail is ' + actual_detail)
                print('Fail: test_homepage_invalid_id_0. Reason: detail mismatch.')
                assert False
        else:
            print('Expected title is ' + TestData.DEFAULT_PATIENT_NOT_FOUND_TITLE)
            print('However, actual title is ' + actual_title)
            print('Fail: test_homepage_invalid_id_0. Reason: title mismatch.')
            assert False
