import sqlite3

from Config.config import TestData

connie = sqlite3.connect(TestData.DB_LOCALE)
c = connie.cursor()

c.execute("""
INSERT INTO contact_details 
(name, dob, gender, identifier) VALUES 
('gewf', '1940-12-01', 'male', 'OK'),
('gedr', '1940-12-01', 'female', 'yes'),
('rwetrg', '1940-12-01', 'Male', 'HI')
""")

connie.commit()
connie.close()
