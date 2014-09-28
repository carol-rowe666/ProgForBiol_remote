import pandas as pd
import sys
import numpy as np
import itertools as it

data = pd.read_csv('TGPP_pres.csv')

#print data['plot'].unique()
#print len(data['plot'].unique())
#print len(data)
"""
grouped_data = data.groupby(['year', 'plot'])
sp_data = grouped_data['spcode'].unique()
print type(sp_data)
print sp_data.head()
"""

species_data = data.groupby(['year', 'plot'])['spcode'].unique()
species_table = pd.DataFrame(species_data)
year_set = (data['year'].unique())
#print year_set

for num in year_set:
    new_table = species_table.ix[num]
    for pos1, pos2 in it.combinations(new_table['spcode'],2):
        pos1 = set(pos1)
        pos2 = set(pos2)
        num_inter = len(pos1.intersection(pos2))
        num_union = len(pos1.union(pos2))
        Jaccard = num_inter/float(num_union)
        print num, Jaccard
        #new_table['Jaccard'] = new_tabe.append(Jaccard)
#print new_table.head()
"""
sp_data_table = species_data.values
for line in species_data.values:
    new_line = set(line)
    print new_line

print species_data.ix[2008]
print len(species_data.ix[2008, 317])
grumpy = species_data.ix[2008, 317]
grump = set(grumpy)
"""
#print species_data.values[:5]
#table = set([species_data.values])
#print table
