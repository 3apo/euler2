"""If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers."""
#s = reduce(lambda x,y: x+str(y), numList, '')
#num = int(s)
"""
def palindrom(n):
    l = list(str(n))
    r = list(l)
    r.reverse()
    return r == l

def lychrel(n):
    found = False
    x = n
    k = 0
    while not found and k < 50:
        #Print N,x,k
        if(palindrom(x)):
            found = True
            #print "found",n,x,k
            return True
            break
        else:
            w = str(x)
            w.replace('L','')
            r = list(w)
            r.reverse()
            s = map(str,r)
            x = x +  long(''.join(s) )#reverse n
            #print " new x:",x
            k = k+1
    #print n
    return False
            
nL = (repr(3692222222))
print nL.replace('L','')
nL.replace("L","")
#print nL,type(nL)
nI = long(''.join(nL))
#print nI, type(nI)
#num = int(''.join(map(str,nL)))

#print palindrom(67)
print lychrel(10677) 
count = 0
for t in range(1,10001):
    if(not lychrel(t)):
        print t
        count = count + 1


print "found num", count """
lychrel = 0
for i in xrange(10000):
    for k in xrange(50):
        r = int(str(i)[::-1])
        if i == r and k != 0: break
        else: i += r
    else: lychrel += 1
print lychrel


t = (repr(2**1000).replace('L',''))

#t.replace('L','')
#print t
#k += int(t[::-1])
k = 0
print int(str(t[1:2]))
for i in range(0,len(t)): k += int(str(t[i]))
print k
