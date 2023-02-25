from Utilities import ExcelHelper
from Utilities.utils import get_project_root


class TestData:
    # Common configs
    WEB_BASE_URL = 'https://mikecomputerscience.github.io/Aluna/'
    API_BASE_URL = 'http://127.0.0.1:7777'
    DB_LOCALE = 'patients.db'
    PROJECT_ROOT = get_project_root()
    ID_DATA_PATH = PROJECT_ROOT + '/TestData/IdData.xlsx'
    ID_DATA = ExcelHelper.get_dic(ID_DATA_PATH, 'Sheet1')

    # Home page
    HOME_PAGE_TITLE = 'Aluna | Take Control of Your Lung Health - FDA Cleared Spirometer'
    # Valid identifiers
    VALID_ID_0 = 'JUGO1940M'
    VALID_ID_0_NAME = 'Juan Gomez'
    VALID_ID_0_DOB = '1940-12-01'
    VALID_ID_0_GENDER = 'Male'

    VALID_ID_1 = 'jugo1940m'
    VALID_ID_1_NAME = 'Juan Gomez'
    VALID_ID_1_DOB = '1940-12-01'
    VALID_ID_1_GENDER = 'Male'

    VALID_ID_2 = 'EMGR2000F'
    VALID_ID_2_NAME = 'Emily Green'
    VALID_ID_2_DOB = '2000-06-30'
    VALID_ID_2_GENDER = 'Female'

    # Invalid identifiers
    INVALID_ID_0 = ''
    INVALID_ID_1 = 'JUGO1940'
    INVALID_ID_2 = 'JUGOM'
    INVALID_ID_3 = 'JU1940M'
    INVALID_ID_4 = 'GO1940M'
    INVALID_ID_5 = 'EMGR2000FE'
    INVALID_ID_6 = 'JG1940M'
    INVALID_ID_7 = 'JUGO1940F'

    # Detail page
    DETAIL_PAGE_TITLE = 'Aluna | Patient Detail'
    DEFAULT_PATIENT_FOUND_TITLE = 'Patient found'
    DEFAULT_PATIENT_NOT_FOUND_TITLE = 'No patient matches the identifier'

    # API
    PATIENTS_IDENTIFIER = '/patients/identifier'
    PATIENT = '/patient'
    IDENTITY = '/identity'
