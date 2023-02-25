import sqlite3

from Config.config import TestData

connie = sqlite3.connect(TestData.DB_LOCALE)
c = connie.cursor()

c.execute("""
SELECT * FROM contact_details
""")
patient_info = c.fetchall()
for patient in patient_info:
    print(patient)
connie.commit()
connie.close()
