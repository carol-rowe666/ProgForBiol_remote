import sqlite3 as dbapi
import pandas as pd

con = dbapi.connect('portal_mammals.sqlite')
cur = con.cursor()
cur.execute('DROP TABLE Field_Notes')
cur.execute('DROP TABLE PortalMammals_species_code')
cur.execute("CREATE TABLE Field_Notes('yr' int, 'mo' int, 'dy' int, 'Notes' varchar(5000))")
cur.execute("INSERT INTO Field_Notes VALUES(1963, 04, 01, 'Just completed the April 1963 census of the site. The region is teeming with Dipodomys spectabilis. Using the time machine to conduct trapping prior to the start of the study is working out great!')")
cur.execute("INSERT INTO Field_Notes VALUES(2013, 10, 1, 'Vegetation seems to have returned to normal for this time of year. The landscape isn''t exactly green, but there is a decent amount of plant activity and there should be enough food for the rodents to the winter')")
cur.execute("UPDATE Field_Notes SET yr=2012 WHERE mo=10 AND dy=1")

#Starting question 12. Fixing oldcode column in PortalMammals_species table to contain a single entry.
#Had to change name to PortalMammals_speices_old after I created the new PortalMammals_species table without the oldcode column.
cur.execute("CREATE TABLE PortalMammals_species_code (new_code TEXT, old_code TEXT)")
cur.execute("SELECT new_code, oldcode FROM PortalMammals_species_old")
temptable = cur.fetchall()
for n_code, o_code in temptable:
    #print new_code, oldcode
    if o_code is None:
        o_code = n_code
    oldcodes = o_code.split(",")
    for code in oldcodes:
        # the strip removes any whitespace
        code = code.strip()
        # ? represents the parameter
        cur.execute("INSERT INTO PortalMammals_species_code VALUES (?, ?)",(n_code, code))
        #print n_code, code
#recreating the PortalMammals_species table without the oldcode column. Once I do this, I need to edit it out, or DROP TABLE at start.
#cur.execute("ALTER TABLE PortalMammals_species RENAME TO PortalMammals_species_old")
#cur.execute('''CREATE TABLE PortalMammals_species AS SELECT new_code, scientificname, taxa, commonname, 
#            unknown, rodent, shrubland_affiliated FROM PortalMammals_species_old''')
con.commit()
con.close()