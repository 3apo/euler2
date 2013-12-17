import math
import decimal

def patternLength(s):
    pl = [ l for l in range(1,len(s)/2+1) if s[0:l] == s[l:2*l] and len(set(s[0:l])) > 2 ]
    if pl : return max(pl)

    
print patternLength('1666666')
print patternLength('142857142857')
print patternLength('aabaab')
        
pl = []
for l in range(1,10000):
    w = repr(float(1.0/l))
    if len(w) > 4:
        w = w[2:-1]
        pl.append(patternLength(w))
    else:
        pl.append(2)
    #print l, patternLength(w),w
mpl = pl.index(max(pl)) + 1
print ' max string length is :' , mpl, ' -> ', 1.0/mpl , '  length = ', max(pl) 
