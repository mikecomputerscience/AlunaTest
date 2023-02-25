import pytest
import requests

from Config.config import TestData


class Test_Identifier_Api_DDT():

    @pytest.mark.api
    @pytest.mark.first
    def test_get_identifier_api_ddt(self):
        failed_messages = []
        for the_id, dic in TestData.ID_DATA.items():
            identifier = dic['identifier']
            valid = dic['valid']
            name = dic['name']
            dob = dic['dob']
            gender = dic['gender']
            if valid == 'yes':
                get_payload = {'name': name, 'dob': dob, 'gender': gender}
                response = requests.get(TestData.API_BASE_URL + TestData.PATIENTS_IDENTIFIER, params=get_payload)
                assert response.status_code == 200
                actual_identifier = response.json()['identifier']
                if identifier.upper() == actual_identifier:
                    print("Identifier " + actual_identifier + " matched! That's good!")
                else:
                    fail_message = 'Fail: ' + the_id + "'s expected identifier is " + identifier + '. However, actual identifier is ' + actual_identifier
                    print(fail_message)
                    failed_messages.append(fail_message)
            # No patient matches the identifier
            else:
                print('Negative tests are skipped for get_identifier verification.')
        if failed_messages:
            print('Fail: test_get_identifier_api_ddt.')
            print('Failure reasons are ' + str(failed_messages))
            assert False
        else:
            print('Pass: test_get_identifier_api_ddt.')
            assert True
