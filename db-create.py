import sqlite3

from Config.config import TestData

connie = sqlite3.connect(TestData.DB_LOCALE)
c = connie.cursor()

c.execute("""
CREATE TABLE contact_details
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
dob TEXT,
gender TEXT,
identifier TEXT
)
""")

connie.commit()
connie.close()
