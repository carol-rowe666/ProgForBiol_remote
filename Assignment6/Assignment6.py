import sqlite3 as dbapi
import pandas as pd

con = dbapi.connect('portal_mammals.sqlite')
cur = con.cursor()
cur.execute('DROP TABLE Field_Notes')

cur.execute("CREATE TABLE Field_Notes('yr' int, 'mo' int, 'dy' int, 'Notes' varchar(5000))")
cur.execute("INSERT INTO Field_Notes VALUES(1963, 04, 01, 'Just completed the April 1963 census of the site. The region is teeming with Dipodomys spectabilis. Using the time machine to conduct trapping prior to the start of the study is working out great!')")
cur.execute("INSERT INTO Field_Notes VALUES(2013, 10, 1, 'Vegetation seems to have returned to normal for this time of year. The landscape isn''t exactly green, but there is a decent amount of plant activity and there should be enough food for the rodents to the winter')")
cur.execute("UPDATE Field_Notes SET yr=2012 WHERE mo=10 AND dy=1")
con.commit()
con.close()