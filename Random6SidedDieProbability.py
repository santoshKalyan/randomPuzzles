"""
Create a random number generator for a 6-sided die based on a given probability distribution
The function should return a die value based on uneven probability
Number : 1,2,3,4,5,6
Probability : 0.05, 0.1, 0.15, 0.20, 0.15, 0.35
"""

import random
unevenDist = (0.05, 0.1, 0.15, 0.20, 0.15, 0.35)

# astotale total of bias is 1
def roll_uneven_die(Dist):
    first = random.random()
    total = 0
    result = 1
    for i in Dist:
        total += i
        if first < total:
            return result
        result+=1

print roll_uneven_die(unevenDist)
