import pytest
import requests

from Config.config import TestData
from Utilities.ApiHelper import ApiHelper


class Test_Second_Exercise():
    # test GET /patients/identifier?name=< name >&dob=< dob >&gender=< gender >
    @pytest.mark.api
    @pytest.mark.first
    def test_get_patients_identifier_valid_id_0(self):
        get_payload = {'name': TestData.VALID_ID_0_NAME, 'dob': TestData.VALID_ID_0_DOB,
                       'gender': TestData.VALID_ID_0_GENDER}
        response = requests.get(TestData.API_BASE_URL + TestData.PATIENTS_IDENTIFIER, params=get_payload)
        assert response.status_code == 200
        actual_identifier = response.json()['identifier']
        if TestData.VALID_ID_0.upper() == actual_identifier:
            assert True
            print("Identifier " + actual_identifier + " matched! That's good!")
            print('Pass: test_get_patients_identifier_valid_id_0')
        else:
            print('Expected identifier is ' + TestData.VALID_ID_0)
            print('However, actual identifier is ' + actual_identifier)
            print('Fail: test_get_patients_identifier_valid_id_0. Reason: identifier mismatch.')
            assert False

    @pytest.mark.api
    @pytest.mark.first
    def test_get_identifier_name_missing(self):
        get_payload = {'name': '', 'dob': TestData.VALID_ID_0_DOB, 'gender': TestData.VALID_ID_0_GENDER}
        response = requests.get(TestData.API_BASE_URL + TestData.PATIENTS_IDENTIFIER, params=get_payload)
        assert response.status_code == 200
        actual_identifier = response.json()['identifier']
        if TestData.VALID_ID_0.upper() == actual_identifier:
            print("Identifier" + actual_identifier + " matched! That's not good since name is missing!")
            print(
                'Fail: test_get_identifier_name_missing. Reason: an identifier should not be returned when name is missing.')
            assert False
        else:
            assert True
            print('Pass: test_get_identifier_name_missing')

    # test POST /identity
    @pytest.mark.api
    @pytest.mark.second
    def test_post_identity_200(self):
        EXPECTED_STATUS_CODE = 200
        random_identifier = ApiHelper.get_random_string(9)
        payload = {"identifier": random_identifier}
        response = requests.post(TestData.API_BASE_URL + '/identity', data=payload)
        actual_status_code = response.status_code
        failed_messages = []
        if actual_status_code == EXPECTED_STATUS_CODE:
            actual_response = response.json()
            if actual_response == {}:
                print("Response is empty! That's good!")
            else:
                fail_message = 'Fail: expected response is empty. However, actual response is ' + str(actual_response)
                print(fail_message)
                failed_messages.append(fail_message)
        else:
            fail_message = 'Fail: expected status code is' + str(
                EXPECTED_STATUS_CODE) + '. However, actual status code is ' + str(actual_status_code)
            print(fail_message)
            failed_messages.append(fail_message)
        if failed_messages:
            print('Fail: test_post_identity_200.')
            print('Failure reasons are ' + str(failed_messages))
            assert False
        else:
            print('Pass: test_post_identity_200.')
            assert True

    # test POST /identity
    @pytest.mark.api
    @pytest.mark.second
    def test_post_identity_409(self):
        EXPECTED_STATUS_CODE = 409
        EXPECTED_ERROR = 'The record already exists'
        random_identifier = ApiHelper.get_random_string(9)
        payload = {"identifier": random_identifier}
        requests.post(TestData.API_BASE_URL + TestData.IDENTITY, data=payload)
        # post the same identifier again
        response = requests.post(TestData.API_BASE_URL + TestData.IDENTITY, data=payload)
        actual_status_code = response.status_code
        actual_error = response.json()['error']
        failed_messages = []
        if EXPECTED_STATUS_CODE == actual_status_code:
            print("Status code matched! That's good!")
            if EXPECTED_ERROR == actual_error:
                print("Response is empty! That's good!")
            else:
                fail_message = 'Fail: expected error is ' + EXPECTED_ERROR + '. However, actual error is ' + actual_error
                print(fail_message)
                failed_messages.append(fail_message)
        else:
            fail_message = 'Fail: expected status code is' + str(
                EXPECTED_STATUS_CODE) + '. However, actual status code is ' + str(actual_status_code)
            print(fail_message)
            failed_messages.append(fail_message)
        if failed_messages:
            print('Fail: test_post_identity_409.')
            print('Failure reasons are ' + str(failed_messages))
            assert False
        else:
            print('Pass: test_post_identity_409.')
            assert True

    # test GET /identity
    @pytest.mark.api
    @pytest.mark.second
    def test_get_identity_valid_id_0(self):
        EXPECTED_STATUS_CODE = 200
        name = ApiHelper.get_random_fullname()
        dob = ApiHelper.get_random_dob()
        gender = ApiHelper.get_random_gender()
        identifier = ApiHelper.get_identifier(name, dob, gender)
        post_payload = {'name': name, 'dob': dob, 'gender': gender}
        response = requests.post(TestData.API_BASE_URL + TestData.PATIENT, data=post_payload)
        assert response.status_code == 201

        payload = {'identifier': identifier}
        response = requests.get(TestData.API_BASE_URL + TestData.IDENTITY, params=payload)
        actual_status_code = response.status_code
        response_json = response.json()
        actual_name = response_json['name']
        actual_dob = response_json['dob']
        actual_gender = response_json['gender']
        failed_messages = []
        if EXPECTED_STATUS_CODE == actual_status_code:
            print("Status code matched! That's good!")
            if name == actual_name:
                print("Name matched! That's good!")
                if dob == actual_dob:
                    print("DOB matched! That's good!")
                    if gender == actual_gender:
                        print("Name matched! That's good!")
                    else:
                        fail_message = 'Fail: expected gender is ' + gender + '. However, actual gender is ' + actual_gender
                        print(fail_message)
                        failed_messages.append(fail_message)
                else:
                    fail_message = 'Fail: expected dob is ' + dob + '. However, actual dob is ' + actual_dob
                    print(fail_message)
                    failed_messages.append(fail_message)
            else:
                fail_message = 'Fail: expected name is ' + name + '. However, actual name is ' + actual_name
                print(fail_message)
                failed_messages.append(fail_message)
        else:
            fail_message = 'Fail: expected status code is' + str(
                EXPECTED_STATUS_CODE) + '. However, actual status code is ' + str(actual_status_code)
            print(fail_message)
            failed_messages.append(fail_message)
        if failed_messages:
            print('Fail: test_get_identity_valid_id_0.')
            print('Failure reasons are ' + str(failed_messages))
            assert False
        else:
            print('Pass: test_get_identity_valid_id_0.')
            assert True
