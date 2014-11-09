import re
import pandas as pd
import sqlite3 as dbapi

inputfile = open('list_of_rodents.txt', 'r')

def get_family(inputstring):
    family_re = re.compile("Family\s\\[\\[([A-Z][a-z]+)")
    family_search = re.search(family_re, inputstring)
    if family_search:
        return family_search.group(1)

def get_name(inputstring):
    species_re = re.compile("\\[\\[([A-Z][a-z]+)\s([a-z]+)")
    species_search = re.search(species_re, inputstring)
    if species_search:
        return species_search.group(1,2)

"""Got this from StackOverflow"""
class myDict(dict):
    def __init__(self):
        self = dict()
        
    def add(self, key, value):
        self[key] = value


""" I pirated the def df2sqlite from the internet: 
http://yznotes.com/write-pandas-dataframe-to-sqlite/"""
def df2sqlite(dataframe, db_name = "Gen_sp_output.sqlite", tbl_name = "Gen_sp_output"):
    import sqlite3
    conn=sqlite3.connect(db_name)
    cur = conn.cursor()                                 
 
    wildcards = ','.join(['?'] * len(dataframe.columns))              
    data = [tuple(x) for x in dataframe.values]
 
    cur.execute("drop table if exists %s" % tbl_name)
 
    col_str = '"' + '","'.join(dataframe.columns) + '"'
    cur.execute("create table %s (%s)" % (tbl_name, col_str))
 
    cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)
 
    conn.commit()
    conn.close()
    
  
no_match = []
Gen_sp_output = pd.DataFrame()
genus_species = myDict()

for line in inputfile:
    family = get_family(line)
    genus = get_name(line)    
    if family:
        genus_species.add('Family', family)
    if genus:
        genus_species.add('Genus', genus[0])
        genus_species.add('species', genus[1])
        Gen_sp_output = Gen_sp_output.append(genus_species, ignore_index = True)
    else:
        no_match.append(line)

#I need to delete the last row in the table.

#Gen_sp_output.to_excel('Fam_Genus_sp.xls')
df2sqlite(Gen_sp_output)