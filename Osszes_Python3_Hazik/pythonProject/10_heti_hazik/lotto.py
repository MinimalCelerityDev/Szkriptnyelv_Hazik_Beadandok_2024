from itertools import combinations

from math import prod

def talalas():

    for kombo in combinations(range(1, 46), 6):


        if sum(kombo) == 90 and prod(kombo) == 996300:

            return kombo

nyerok = talalas()
print("A nyerőszámok:", nyerok)
