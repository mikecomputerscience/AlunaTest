# AlunaTest

Aluna Automation Test

## Steps to run the tests:

1. Make sure you are at the project root folder
2. Create the virtual environment: <code>python3 -m venv venv</code>
2. Activate the virtual environment: <code>source venv/bin/activate</code>
3. Install the packages: <code>pip install -r requirements.txt</code>
4. Run following .py files to create & verify local database: <code>python3 db-create.py</code>, <code>python3
   db-populate.py</code>, <code>python3 db-query.py</code>
5. Run the backend service: <code>python3 app.py</code>

## First exercise

1. Write a function that given the input above returns the desired identifier. ==> The function can be found at <code>
   ./Utilities/ApiHelper</code> where the function name is get_identifier
2. Given the following API spec write automated tests to guarantee that the api works.
   ==> <code>pytest -s -v -m "first"</code>

## Second exercise

Run all tests for the second exercise: <code>pytest -s -v -m "second"</code>

## Third exercise

Run all tests for the third exercise: <code>pytest -s -v -m "third"</code>

## All commands

Run all tests: <code>pytest -s -v</code>

Run all UI tests: <code>pytest -s -v -m "ui"</code>

Run all API tests: <code>pytest -s -v -m "api"</code>

Run all tests for the first exercise: <code>pytest -s -v -m "first"</code>

Run all tests for the second exercise: <code>pytest -s -v -m "second"</code>

Run all tests for the third exercise: <code>pytest -s -v -m "third"</code>
