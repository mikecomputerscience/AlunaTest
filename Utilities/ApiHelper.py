import random
import sqlite3
import time

from Config.config import TestData


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


class ApiHelper:
    @staticmethod
    def get_identifier(name, dob, gender):
        try:
            names = name.split(' ')
            first_name = names[0].upper()
            last_name = names[1].upper()
            year = dob[:4]
            gender_initial = gender[0].upper()
            return first_name[:2] + last_name[:2] + year + gender_initial
        except Exception as e:
            return str(e)

    @staticmethod
    def query_contact_details():
        connie = sqlite3.connect(TestData.DB_LOCALE)
        c = connie.cursor()
        c.execute("""
        SELECT * FROM contact_details
        """)
        patient_data = c.fetchall()
        return patient_data

    @staticmethod
    def query_identifiers():
        connie = sqlite3.connect(TestData.DB_LOCALE)
        c = connie.cursor()
        c.execute("""
        SELECT identifier FROM contact_details
        """)
        patient_data = c.fetchall()
        return patient_data

    @staticmethod
    def query_contact_by_identifier():
        connie = sqlite3.connect(TestData.DB_LOCALE)
        c = connie.cursor()
        c.execute("""
            SELECT * FROM contact_details
            """)
        patient_data = c.fetchall()
        return patient_data

    @staticmethod
    def get_random_string(length):
        letters = []
        for i in range(65, 91):
            letters.append(chr(i))
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def get_random_name():
        length = random.randint(3, 7)
        return ApiHelper.get_random_string(length)

    @staticmethod
    def get_random_fullname():
        firstname = ApiHelper.get_random_name()
        lastname = ApiHelper.get_random_name()
        return firstname + ' ' + lastname

    @staticmethod
    def get_random_dob():
        # 1940-12-01
        return random_date("1900-01-01", "2023-02-24", random.random())

    @staticmethod
    def get_random_gender():
        genders = ['male', 'Male', 'female', 'Femail']
        return random.choice(genders)
