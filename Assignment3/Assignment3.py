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

def get_data_from_web(url):
    data = pd.read_csv(url)
    return data

