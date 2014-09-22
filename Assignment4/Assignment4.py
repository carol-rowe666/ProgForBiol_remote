import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

col_names = ['Continent', 'Status', 'Order', 'Family', 'Genus', 'Species', 'Log_mass', 'Combined_mass', 'Reference']
data = pd.read_table('http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt', keep_default_na =False, names = col_names)
data = data.replace('Af', 'AF')
#print data['Continent'].unique()
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
print "The largest combined mass is:", tubby[['Genus', 'Species', 'Combined_mass']].set_index(['Genus'])

noneg_skinny = data[(data['Combined_mass'] >= 0 )]
skinny = noneg_skinny[(noneg_skinny['Combined_mass'] == min(noneg_skinny['Combined_mass']))]
print skinny[['Genus', 'Species', 'Combined_mass']]

#"The average mass of extant species is X and the average mass of extinct species is Y." 
avg_mass = data.groupby('Status')
#print avg_mass['Combined_mass'].mean()
print "The average mass of extant species is %.2f and the average mass of extinct species is %.2f." % (extant['Combined_mass'].mean(), extant['Combined_mass'].mean())

#Queston2
# 'extant' and 'extinct' already created above. Use those data subsets now with groupby Continent
by_cont_alive = extant.groupby(['Continent'])
by_cont_dead = extinct.groupby(['Continent'])
#now get the mass. But noticed my DataFrame was messed-up. Re-assign DataFrame and new index.
avg_mass_alive = pd.DataFrame(by_cont_alive['Combined_mass'].mean()).reset_index()
avg_mass_dead = pd.DataFrame(by_cont_dead['Combined_mass'].mean()).reset_index()
#how tells how to merge. 'outer' merges them from all variables in both files based on='Continent'. Lovely!
continent_mass_differences = pd.merge(avg_mass_alive, avg_mass_dead, on='Continent', how='inner', suffixes=('_avg_extant', '_avg_extinct'))
continent_mass_differences['diff_masses'] = abs(continent_mass_differences['Combined_mass_avg_extant'] - continent_mass_differences['Combined_mass_avg_extinct'])
continent_mass_differences['ratio'] = continent_mass_differences['Combined_mass_avg_extinct'] / continent_mass_differences['Combined_mass_avg_extant']
#print continent_mass_differences
continent_mass_differences.to_csv('continent_mass_differences.csv')

#Question3
pos_logExtant = extant[(extant['Log_mass'] >= 0)]
pos_logExtinct = extinct[(extinct['Log_mass'] >= 0)]
#logmass_Extant = pos_logExtant[['Continent' , 'Log_mass']]
pos_logExtant['Log_mass'].hist(by=pos_logExtant['Continent'], color='red', alpha=0.5)
pos_logExtinct['Log_mass'].hist(by=pos_logExtinct['Continent'], color='blue', alpha=0.3)
plt.title('Log_Mass_Histogram', fontsize=20)
plt.xlabel('Log_mass', fontsize=15)
plt.ylabel('Frequency', fontsize=10)

plt.show()
#plt.savefig('Log_mass_Continent_Fig.pdf', format='pdf', dpi=1000)

"""
# df = pd.merge(position, region, on='chromosome', how='inner')
#>>> idx = (df['BP'] < df['start']) | (df['end'] < df['BP'])  # violating rows

genspstat = np.unique(bygenus['Status'])
print genspstat

#print len(data[unique_names['Status'] == "extant"])
#Find out how many genera are present in the dataset
gen_data = np.unique(data['Genus'].values)
print "There are %d genera in the dataset." % len(gen_data)
"""