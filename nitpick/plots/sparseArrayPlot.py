import numpy
from arrayPlot import arrayPlot
import operator
from functools import reduce

def sparseArrayPlot(indexes, dimensions, reshape=False):
    #convert sparse array into dense array
    arraySize = reduce(operator.mul, dimensions, 1)
    denseArray = numpy.zeros(arraySize)
    denseArray[indexes]=1
    denseArray = numpy.reshape(denseArray,dimensions)
    
    #plot the dense array
    plotReturn = arrayPlot(denseArray,reshape=reshape)

    return plotReturn
    
