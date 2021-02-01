import random
from itertools import islice
population = []
weightlimit = 200
while len(population) < 7:
    population.append(random.randint(40, weightlimit/2))
seats = 2
trips = 0
population.sort()
population.reverse()
currentperson =