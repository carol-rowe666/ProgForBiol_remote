
#Assignment3 Question1
import math

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
        ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
        ['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
        ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
        ['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
        ['D5', 98], ['D6', 32]]
print "There are %d sites." % len(data)
print "There are %d birds at the 7th site." % data[6][1]
print "There are %d birds at the last site." % data[-1][1]
total_birds = 0
for i in data:
    total_birds += i[1]
print "The total number of birds across all sites is %d." % total_birds
avg_birds = float(total_birds)/len(data)               
print "The average number of birds seen on a site is %.2f." % avg_birds
C_avg_birds = 0
for i in data:
    if "C" in i[0]:
        C_avg_birds += i[1]
print "The total number of birds counted on sites with codes \n\tbegining with 'C' is %d." % C_avg_birds


#Assignment3 Question2
import pandas as pd
import numpy as np

def get_data_from_web(url):
    data = pd.read_csv(url)
    return data

data = get_data_from_web('http://www.programmingforbiologists.org/data/houseelf_earlength_dna_data.csv')

#determine the earisize as large or small
earnum = 0
data['earsize'] = 'ambiguous'
for earsize in data['earlength']:
    if earsize > 10.0:
        data['earsize'][earnum] = 'large'
    else:
        data['earsize'][earnum] = 'small'
    earnum = earnum + 1


#determine %GC content
count = -1
data['GCcontent'] = 0
for seq in data['dnaseq']:
    GCcont = 0
    length = len(seq)
    count = count + 1
    for letter in seq:
        if (letter == 'G') or (letter == 'C'):
            GCcont = GCcont + 1
    data['GCcontent'][count] = GCcont
    data['%GCcontent'] = 100.0 * data['GCcontent'] / length

#Alternative to %GCcontent
count = 0
data['alt_%GCcontent'] = 0
for seq in data['dnaseq']:
    length = len(data['dnaseq'][count])
    data['alt_%GCcontent'][count] = 100.0 * (data['dnaseq'][count].count('G') + data['dnaseq'][count].count('C')) / length
    count = count + 1


#Create new table for columns of interest
grangers_analysis = data[['id', 'earsize', '%GCcontent']]
grangers_analysis.to_csv('grangers_analysis.csv')

#determine average GC content of small-eared elves
small_ears = grangers_analysis[grangers_analysis['earsize'] == 'small']
print "The mean GC content of small-eared elves is %.2f percent." % small_ears.mean(0)

#determine average GC content of large-eared elves
large_ears = grangers_analysis[grangers_analysis['earsize'] == 'large']
print "The mean GC content of large-eared elves is %.2f percent." % large_ears.mean(0)

#Alternative method for GC content of small- and large-eared elves, using GROUPING
eared_data = data.groupby('earsize') #grouping by earsize
for earsize, subgroup_data in eared_data: #creates variables 'earsize' for the ordered group, and 'subgroup_data' for the subset of data based on earsize
    avg_GC_by_ears = np.mean(subgroup_data['%GCcontent'])
    print "The mean GC content of {}-eared elves is {}%" .format(earsize, avg_GC_by_ears)
    
#testing
earless_data = data.groupby(data['earlength'] > 10.0)
for earsized, subgrouped in earless_data:
    avged_GC_by_ears = np.mean(subgrouped['%GCcontent'])
    print "The mean GC content of {}-eared elves is {}%" .format(earsized, avged_GC_by_ears)
