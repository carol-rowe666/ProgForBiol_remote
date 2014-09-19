import pandas as pd
import numpy as np
import matplotlib as plt

col_names = ['Continent', 'Status', 'Order', 'Family', 'Genus', 'Species', 'Log_mass', 'Combined_mass', 'Reference']
data = pd.read_table('http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt', names = col_names)

#Use groupby to get unique names
bygenus = data.groupby(['Genus', 'Species'])
print "Number of unique species in the list:", len(bygenus)

#Find out how many of the unique species are extinct and how many are extant, print the result to the screen
#extant = bygen[(bygen['Status'] == 'extant')]
extant = (data[data['Status'] == 'extant'])
extinct = (data[data['Status'] == 'extinct'])
print "Number of extant species:", len(extant.groupby(['Genus', 'Species']))
print "Number of extinct species:", len(extinct.groupby(['Genus', 'Species']))

#Find out how many families are present in the dataset.
families = data.groupby(['Family'])
print "Number of families in the dataset:", len(families)

#Now print the genus name, the species name, and the mass of the largest and smallest 
#species (note, it is not possible for a mammal to have negative mass
tubby = data[(data['Combined_mass'] == max(data['Combined_mass']))]
print tubby[['Genus', 'Species', 'Combined_mass']].set_index(['Genus'])




"""
genspstat = np.unique(bygenus['Status'])
print genspstat

#print len(data[unique_names['Status'] == "extant"])
#Find out how many genera are present in the dataset
gen_data = np.unique(data['Genus'].values)
print "There are %d genera in the dataset." % len(gen_data)
"""