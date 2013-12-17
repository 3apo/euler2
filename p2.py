""" even value fib numbers less than half a million """
import math

sqrt5 = math.sqrt(5)
phi = ( 1 + sqrt5 ) / 2
ratio = (1 + math.sqrt(5)) / 2
fiB = lambda n: n if n <2 else fiB(n-1) + fiB(n-2)

def fib2(n): 
    return round( pow( phi, n ) / sqrt5 ) 

def fib3(nr):
    return int(ratio ** nr / math.sqrt(5) + 0.5)

def p2Answer():
    total = 0
    x, y = 0, 1
    while y < 4000000:
        x, y = y, x + y
        if x % 2:
            continue
        total += x

    print total

def sumOfEvenFib(n):
    if n < 2 : return 1
    sumFib = 0
    sumFibp = 0
    fib = 0
    fibp = 1
    fibpp = 0

    for i in range(2,n,2):
        fib = fibp + fibpp
        if i %2 ==0: 
            sumFib = fib + sumFibp
            sumFibp = sumFib
            #print 'sumFib', sumFib
        fibpp = fibp
        fibp = fib
   
        #print '[' , i, ']',fib,'--',fiB(i)
    return sumFib


def sum(x,y): return x +y


print fiB(6), fiB(8)

sfib = lambda n: n if  (n % 2 != 0) or n < 2 else fiB(n) + sfib(n-2)
#print sfib(1), sfib(2)
print [sfib(k) for k in range(10)]
print p2Answer()
#print  sumOfEvenFib(400000)

