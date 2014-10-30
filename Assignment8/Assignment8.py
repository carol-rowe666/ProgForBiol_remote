#Assignment8
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
        self.eggs_per_season = self.eggs_per_season + [more_eggs]
        return self.eggs_per_season
    
perry = Platypus("perry", [3, 2, 4, 1, 2])
print perry.total_fecundity()
print perry.breeding_seasons()
#print perry.lay_eggs(perry.total_fecundity()) Oops, this isn't what you were asking!
print perry.lay_eggs(2)
print perry.total_fecundity()
