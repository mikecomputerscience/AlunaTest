import pytest

from Config.config import TestData
from Utilities.ApiHelper import ApiHelper


class Test_First_Exercise():

    @pytest.mark.api
    @pytest.mark.first
    def test_get_identifier_valid_id_0(self):
        actual_identifier = ApiHelper.get_identifier(TestData.VALID_ID_0_NAME, TestData.VALID_ID_0_DOB,
                                                     TestData.VALID_ID_0_GENDER)
        if TestData.VALID_ID_0.upper() == actual_identifier:
            assert True
            print("Identifier " + actual_identifier + " matched! That's good!")
            print('Pass: test_get_identifier_valid_id_0')
        else:
            print('Expected identifier is ' + TestData.VALID_ID_0)
            print('However, actual identifier is ' + actual_identifier)
            print('Fail: test_get_identifier_valid_id_0. Reason: identifier mismatch.')
            assert False

    @pytest.mark.api
    @pytest.mark.first
    def test_get_identifier_name_missing(self):
        actual_identifier = ApiHelper.get_identifier('', TestData.VALID_ID_0_DOB,
                                                     TestData.VALID_ID_0_GENDER)
        if TestData.VALID_ID_0.upper() == actual_identifier:
            print("Identifier" + actual_identifier + " matched! That's not good since name is missing!")
            print(
                'Fail: test_get_identifier_name_missing. Reason: an identifier should not be returned when name is missing.')
            assert False
        else:
            assert True
            print('Pass: test_get_identifier_name_missing')
