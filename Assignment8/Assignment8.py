#Assignment8
import random
import pandas as pd



class Platypus(object):
    def __init__(self, name, eggs_per_season):
        self.name = name
        self.eggs_per_season = eggs_per_season

    def total_fecundity(self):
        return sum(self.eggs_per_season)
    
    def breeding_seasons(self):
        return reduce(lambda x,y: x + (1 if y >= 1 else 0), self.eggs_per_season, 0)
        # reduce(function, iterable, initializer)
        # the left value, x, is the accumulated value which is initialized to 0, and 
        # the right argument, y, is the update value from the iterable
        # the iterable is the list of self.eggs_per_season
        
    def lay_eggs(self, more_eggs):
        #total_eggs = self.total_fecundity()
        #return self.eggs_per_season + [total_eggs] not what you were asking
        #self.eggs_per_season = self.eggs_per_season.extend(more_eggs)
        self.eggs_per_season = self.eggs_per_season + more_eggs
        return self.eggs_per_season

#data simulation
data = [Platypus('Curly', [3]), Platypus('Larry', [2]), Platypus('Moe', [0])]
for entry in data:
    eggs=[random.randint(0,3) for p in range(0,9)]
    entry.lay_eggs(eggs)
    print "{} laid a total of {} in {} successful breeding seasons.".format(entry.name, entry.total_fecundity(), entry.breeding_seasons())
    print entry.name, entry.eggs_per_season #printing this to make sure results are correct
#Below is how I initially solved the above simulation:
"""
data = [['Curly', [3]], ['Larry', [2]], ['Moe', [0]]]
count = 0
for item in data:
    #creating a random number of eggs (0 to 3) for 9 times
    eggs=[random.randint(0,3) for p in range(0,9)]
    #add the 9 new egg values to the list for each platypus
    data[count][1].extend(eggs)
    count += 1
    name = Platypus(item[0], item[1])
    #print name.lay_eggs(eggs)
    print "{} laid a total of {} in {} successful breeding seasons.".format(item[0],name.total_fecundity(), name.breeding_seasons())
print data
"""

perry = Platypus("perry", [3, 2, 4, 1, 2])
print perry.total_fecundity()
print perry.breeding_seasons()
#print perry.lay_eggs(perry.total_fecundity()) #Oops, this isn't what you were asking!
les_oefs = [2, 3, 0] #making sure the multiple eggs will be added to the list in the lay_eggs function
print perry.lay_eggs(les_oefs)
#print perry.eggs_per_season
print perry.total_fecundity()

platy_data = [Platypus("perry", [3,2,4,1,2]),
Platypus("quacker", [100,1,3,1,2]),
Platypus("fishface", [0,1,3,1,2,1]),
Platypus("duckhead", [3,1,3,6,3]),
Platypus("waddles", [3,1,2,0,8,3]),
Platypus("professor quackington", [2,1,4,5,7]),
Platypus("bartholomew beavertail", [0,1,3,1,0,0,2]),
Platypus("syd", [3,1,3,1,3,5,5,2,1,3]),
Platypus("ovide", [2,0,10,0,0,0,0,0,0]),
Platypus("hexley", [3,1,2,3,1,0,0,1,1]),
Platypus("supafly", [19,1,2,1,0,0,0,1])]
"""
for platy in platy_data:
    if float(platy.total_fecundity())/platy.breeding_seasons() > 3:
        print platy.name
"""    
names = [platy.name for platy in platy_data if float(platy.total_fecundity())/platy.breeding_seasons() > 3]  
print '\n'.join(names)
