"""Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70  22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk  Pj| is minimised; what is the value of D?
"""
import random
random.seed()
pentagonal = lambda n: n*(3*n-1)/2

def pfind(x,y): 
    
    #if(abs(x-y) in P and abs(x+y) in P): 
    w = (((24*abs(x-y)+1)**0.5 +1 ) )/6 
    k =  (((24*abs(x+y)+1)**0.5 +1 ) )/6
    if( (w%1==0) and (k%1==0)):
    #if (((24*abs(x-y)+1)**0.5 +1 ) %1 == 0) and (((24*abs(x-y)+1)**0.5 +1 ) %1 == 0):
        print x,y,w,k
        return True
    else:
        return False
    
P = []
P = map(pentagonal,range(1,10000))

#print P,4 in P
#Pd = reduce(pfind, P)
print random.choice(P),pfind(67,5), 5%1 == 0,3.22 %1 == 0.22
count = 0
found = 0
D = 0
Pd = []
#Pd = [[][]]
while (count < 1000000) :
    x = random.choice(P)
    y = random.choice(P)
    if( (x <> y) and pfind(x,y)):
        Pd.append([x,y])
        found += 1
    count +=1

print Pd
        


