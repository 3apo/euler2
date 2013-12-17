__author__ = ''
import itertools
from utils import *


""" solves p26 """
def p26():
    k = []
    precision = 2000
    for i in range(1,1000):
        s = divisor(1,i,precision)
        if len(s) > 4 :
            k.append(maxRecurringCycle(s[2:-1]))
        else :
            k.append(3)
    #print k
    m = k.index(max(k)) + 1
    sm = divisor(1,m,precision)
    print ' Max recurring cycle is : 1.0/ ', m, ' cycle' ,max(k) #, ' -> ' , sm


""" p27 Quadratic Primes """

def numPrime(p,pSet):
    a,b = p
    qp = lambda n : n*n + a*n + b
    n = 1
    qp2 = b
    while (qp2 in pSet):
        n = n + 1
        qp2 = n*n + n*a + b
    if n > 39 : print p, n
    return n

def p27():
    searchRange = 1000
    maxN = 50*50 + searchRange*50 + searchRange
    pSet = primes(maxN)
    ar = range(-searchRange,0)
    br = [ k for k in range(searchRange) if k in pSet]
    k = []
    k.append( [ [p,numPrime(p,pSet)] for p in itertools.product(ar,br)])
    #print k

""" solves p28 """
def nextTransition(currentDirection):
    if 'right' in currentDirection:
        return 'down'
    elif 'down' in currentDirection:
        return 'left'
    elif 'left' in currentDirection:
        return 'up'
    elif 'up' in currentDirection:
        return 'right'
    else: return 'right'

def checkBounds(p,gridSize):
    x,y = p
    return x > -1 and x < gridSize and y > -1 and y < gridSize

def movePt(p,transition):
    x,y = p
    if 'up' in transition:
        return (x-1,y)
    elif 'down' in transition:
        return (x+1,y)
    elif 'left' in transition:
        return (x, y-1)
    else:
        return (x,y+1)
def printyPrintGrid(grid,gridSize):
    for r in range(gridSize):
        for c in range(gridSize):
            print grid[(r,c)] ,
        print '\n'

def nextMove(q,direction, visited, gridSize):
    # if next transition possible, then transition

    nextDirection = nextTransition(direction)
    p = movePt(q,nextDirection)
    if checkBounds(p,gridSize) and not (p in visited):
        visited[p] = visited[q] + 1
        #print 'from:', q, ':', visited[q], 'moved to :', p, ':', visited[p], ' in direction', nextDirection
        return p,nextDirection,visited
    # else continue current direction
    p = movePt(q,direction)
    #print ' considering next move to : ', p, ' bounds check:', checkBounds(p,gridSize) , ' prior visitation: ', p in visited
    if checkBounds(p,gridSize) and not (p in visited):
        visited[p] = visited[q] + 1
        #print 'from:', q, ':', visited[q], 'moved to :', p, ':', visited[p], ' in direction', direction
        return p, direction, visited
    # else dont do anything
    #print 'from:', q , ' did not do anything'
    return q, direction, visited

def calculateDiag(grid,gridSize):
    rD = zip(range(gridSize),range(gridSize))
    lD = zip(range(gridSize),range(gridSize-1,-1,-1)) + rD
    print  sum( grid[p] for p in lD ) - 1

def p28():
    print ' Solution for P28'
    gridSize = 1001
    grid = [p for p in itertools.product(range(gridSize),range(gridSize))]
    #print grid
    origin = (gridSize/2, gridSize/2)
    print origin
    visited = dict()
    #notVisited = set(grid)
    p,direction = origin, ''
    visited[p] = 1
    for k in grid:
        p,direction, visited = nextMove(p,direction,visited,gridSize)

    printyPrintGrid(visited,gridSize)
    calculateDiag(visited,gridSize)
