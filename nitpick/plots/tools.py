"""
Various useful functions used in generating plots.
"""


def getAllFactorPairs(inputNumber):
    """
    Return a list of all the possible factor pairs of the inputNumber; keyed by their quotient.
    e.g. getAllFactorPairs(6) -> [(1, 6),(2, 3),(3, 2),(6, 1)]
    """
    setOfFactors = set(reduce(
            list.__add__,
            ([i, inputNumber//i] for i in range(1, int(inputNumber**0.5) + 1) if inputNumber % i == 0)
            ))
    pairs = [(factor, inputNumber/factor) for factor in setOfFactors]
    pairs.sort()
    
    return pairs

def getClosestFactorPair(inputNumber,targetRatio):
    """
    Return a tuple of integers (x,y) such that x*y = inputNumber.
    x and y are chosen to be as close as possible to the targetRatio as allowed by inputNumber.
    targetRatio can be [vertical,horizontal] or horizontal/vertical
    """
    try:
        targetRatio = float(targetRatio)
    except:
        targetRatio = float(targetRatio[1])/float(targetRatio[0])
        
    pairs = getAllFactorPairs(inputNumber)
    closestPair = min(pairs, key=lambda x:abs((float(x[1])/float(x[0]))-targetRatio))
    
    return closestPair
    
#Supreme flattening generator from stack overflow
from collections import Iterable
def flatten(l,level = -1):
    """
    This generator flattens whatever youi throw at it. With an optional argument to only flatten down to a particular level.
    level = -1 flattens everything
    level = 0 doesn't flatten anything
    level = 1 flattens one level
    """
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, basestring) and not level==0:
            for sub in flatten(el,level = level -1):
                yield sub
        else:
            yield el
            
