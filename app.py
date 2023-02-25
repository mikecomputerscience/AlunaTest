import sqlite3

from flask import *

from Config.config import TestData
from Utilities.ApiHelper import ApiHelper

app = Flask(__name__)


@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home_page():
    patient_data = ApiHelper.query_contact_details()
    return jsonify(patient_data), 200


# The first api in document
# 'GET /patients/identifier?name=< name >&dob=< dob >&gender=< gender >'
@app.route('/patients/identifier', methods=['GET'])
def request_id():
    name = str(request.args.get('name'))
    dob = str(request.args.get('dob'))
    gender = str(request.args.get('gender'))
    identifier = ApiHelper.get_identifier(name, dob, gender)
    res = {'identifier': identifier}
    return jsonify(res), 200


# The second api in document
# POST /identity
@app.route('/identity', methods=['POST'])
def post_identity():
    existing_identifiers = [row[4] for row in ApiHelper.query_contact_details()]
    data = request.form  # a multidict containing POST data
    identifier = data['identifier']

    if identifier in existing_identifiers:
        res = {'error': 'The record already exists'}
        return jsonify(res), 409
    else:
        try:
            connie = sqlite3.connect(TestData.DB_LOCALE)
            c = connie.cursor()
            sql = """INSERT INTO contact_details (name, dob, gender, identifier) VALUES (?, ?, ?, ?)"""
            c.execute(sql, ('', '', '', identifier))
            connie.commit()
            return jsonify({}), 200
        except Exception as e:
            res = {'error': e}
            return jsonify(res), 500


# The third api in document
# GET /identity
# http://127.0.0.1:7777/identity?identifier=JUGO1940M
@app.route('/identity', methods=['GET'])
def get_identity():
    identifier = str(request.args.get('identifier'))
    connie = sqlite3.connect(TestData.DB_LOCALE)
    c = connie.cursor()
    c.execute("SELECT * FROM contact_details WHERE identifier=?", (identifier,))
    patient_data = c.fetchall()
    infos = [
        dict(name=row[1], dob=row[2], gender=row[3])
        for row in patient_data
    ]
    if len(infos) > 0:
        res = infos[0]
        return jsonify(res), 200
    else:
        res = {'error': 'The record is not found'}
        return jsonify(res), 404


# This api can be used to post name, dob and gender to database. It's very useful.
# POST /patient
@app.route('/patient', methods=['POST'])
def post_patient():
    data = request.form  # a multidict containing POST data
    name = data['name']
    dob = data['dob']
    gender = data['gender']
    identifier = ApiHelper.get_identifier(name, dob, gender)

    connie = sqlite3.connect(TestData.DB_LOCALE)
    c = connie.cursor()
    sql = """INSERT INTO contact_details (name, dob, gender, identifier) VALUES (?, ?, ?, ?)"""
    c.execute(sql, (name, dob, gender, identifier))
    connie.commit()
    res = {'name': name, 'dob': dob, 'gender': gender, 'identifier': identifier}
    return jsonify(res), 201


if __name__ == '__main__':
    app.run(port=7777, debug=False)
