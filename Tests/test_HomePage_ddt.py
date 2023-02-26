import time

import pytest

from Config.config import TestData
from Pages.DetailPage import DetailPage
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class Test_HomePage_DDT(BaseTest):

    @pytest.mark.ui
    @pytest.mark.third
    def test_homepage_id_ddt(self):

        self.home_page = HomePage(self.driver)
        time.sleep(1)
        self.detail_page = DetailPage(self.driver)

        failed_messages = []
        for the_id, dic in TestData.ID_DATA.items():
            identifier = dic['identifier']
            valid = dic['valid']
            name = dic['name']
            dob = dic['dob']
            gender = dic['gender']
            self.home_page.enter_identifier(identifier)
            time.sleep(1)
            self.home_page.click_find_patient_button()
            time.sleep(1)
            actual_title = self.detail_page.get_result_title()
            actual_detail = self.detail_page.get_result_detail()
            if valid == 'yes':
                expected_name = 'Name: ' + name
                expected_dob = 'DOB: ' + dob
                expected_gender = 'Gender: ' + gender
                if TestData.DEFAULT_PATIENT_FOUND_TITLE == actual_title:
                    print("Patient found! That's good!")
                    if expected_name in actual_detail:
                        print("Patient name matched! That's good!")
                        if expected_dob in actual_detail:
                            print("Patient dob matched! That's good!")
                            if expected_gender in actual_detail:
                                print("Patient gender matched! That's good!")
                                print('Pass: ' + the_id + ' is good!')
                            else:
                                fail_message = 'Fail: ' + the_id + "'s expected gender " + expected_gender + ' is not found in the patient detail ' + actual_detail
                                print(fail_message)
                                failed_messages.append(fail_message)
                        else:
                            fail_message = 'Fail: ' + the_id + "'s expected dob " + expected_dob + ' is not found in the patient detail ' + actual_detail
                            print(fail_message)
                            failed_messages.append(fail_message)
                    else:
                        fail_message = 'Fail: ' + the_id + "'s expected name " + expected_name + ' is not found in the patient detail ' + actual_detail
                        print(fail_message)
                        failed_messages.append(fail_message)
                else:
                    fail_message = 'Fail: ' + the_id + "'s expected title is " + TestData.DEFAULT_PATIENT_FOUND_TITLE + '. However, actual title is ' + actual_title
                    print(fail_message)
                    failed_messages.append(fail_message)
            # No patient matches the identifier
            else:
                expected_detail = identifier
                if TestData.DEFAULT_PATIENT_NOT_FOUND_TITLE == actual_title:
                    print("Patient NOT found! That's good for " + identifier + "!")
                    if expected_detail == actual_detail:
                        print("Patient identifier " + expected_detail + "is shown on the detail page! That's good!")
                    else:
                        fail_message = 'Fail: ' + the_id + "'s expected identifier " + expected_detail + ' is not found in the patient detail ' + actual_detail
                        print(fail_message)
                        failed_messages.append(fail_message)
                else:
                    fail_message = 'Fail: ' + the_id + "'s expected title is " + TestData.DEFAULT_PATIENT_NOT_FOUND_TITLE + '. However, actual title is ' + actual_title
                    print(fail_message)
                    failed_messages.append(fail_message)
            self.detail_page.click_back_link()
            time.sleep(1)
        if failed_messages:
            print('Fail: test_homepage_id_ddt.')
            print('Failure reasons are ' + str(failed_messages))
            assert False
        else:
            print('Pass: test_homepage_id_ddt.')
            assert True
