
""" some doc """
from numpy import *

from decimal import * 

print " Proj Euler - 26"

def f3(seq): 
    # Not order preserving 
    keys = {} 
    for e in seq: 
        keys[e] = 1 
    return keys.keys()

def maxSeq(s):
    keys = {}
    pattern = ''
    foundmax = False
    for i in range(0,len(s)):
        for k in range((len(s)/2 +1),1,-1):
            t = s[i:i+k]
            if t in keys :
                keys[t] = keys[t] + 1
                if not foundmax:
                    # print 'in :', s , ' found maximal pattern:',  t
                    pattern = t
                    foundmax = True
            else:
                keys[t] = 1
            
        # for e in t:
        #     if e in keys :
        #         keys[e] = keys[e] + 1
        #     else:
        #         keys[e] = 1

    v = keys.values()
    vin = keys.keys()
    index = v.index(max(v))
    #print ' max repeating string:', vin[index], keys 
    return pattern


def maxSeq2(s):
    pattern = ''
    foundmax = False
    minPatternLength = 4

    for k in range((len(s)/2),minPatternLength,-1):
            t = s[0:k]
            p = s[k:k*2]
            if t == p:
                 if not foundmax:
                    # print 'in :', s , ' found maximal pattern:',  t
                    pattern = t
                    foundmax = True
  
    return pattern, foundmax
   
getcontext().prec = 400

for i in range(999,10,-1):
#for i in range(1,10):
    s=  str(int(Decimal(pow(10,400))/Decimal(i)))
    
#    p,f = maxSeq2(s)
#     if(f and (len(p) > 24)):
#         p1,f1 = maxSeq2(p)
#         if f1 and (len(p1) > 20):
#             print ' d:', i, '1/d:', s , ' pattern: ', p1 , len(p1)

    p1 = ''
    p,f = maxSeq2(s)
    while(f):
        p1 = p
        p,f = maxSeq2(p1)
    if len(p1) > 144:
        print ' d:', i, '1/d:', s , ' pattern: ', p1 , len(p1)
    #if((len(p) > 5)):
    #    print ' d:', i, '1/d:', s , ' pattern: ', p1 , len(p1)


