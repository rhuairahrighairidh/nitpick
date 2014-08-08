import numpy
from arrayPlot import arrayPlot

def sparseArrayPlot(indexes, dimensions, reshape=False):
    #convert sparse array into dense array
    denseArray = numpy.zeros(dimensions[0]*dimensions[1])
    denseArray[indexes]=1
    denseArray = numpy.reshape(denseArray,dimensions)
    
    print denseArray
    #plot the dense array
    arrayPlot(denseArray,reshape=reshape)
    
