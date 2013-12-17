import numpy
from itertools import permutation
print 'Euler Problem #66'

# Minimal Solution Diophentine Equation x^2 - Dy^2 = 1
def eu66():

    i = range(1,100)
    t = itertools.combinations(i,3)
    
    
    m = map(dio,i,i,i)
    print len(m),m

def dio(x,y,D):
    return x*x - D*y*y == 1

    
eu66()
