__author__ = ''

""" Devisor routine of 100 numeral precision """
def divisor(num,denom, precision):
    m,r = divmod(num,denom)
    p = [m,'.']
    len = 0
    while ( len < precision):
        r = r *10
        m,r = divmod(r,denom)
        p.append(m);
        len = len + 1
        if r == 0: break
    return p

""" get min recurring cycles in strings """
def maxRecurringCycle(str):
    k = [ l for l in range(len(str)/2) if str[0:l] == str[l:2*l] and len(set(str[0:l])) > 2 ]
    if k : return min(k)

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

