import numpy
from arrayPlot import arrayPlot

def permanencePlot(permanences,numOfSources,numOfEndPoints):
    """
    permanences -> [[synapseStart(ie column), synapseEnd(ie input bit), permanence],[45,162,0.230001], ... ]
    numOfSources -> e.g. number of columns in a SP
    numOfEndPoints -> e.g. number of input bits in a SP
    """
    #create an adjacency matrix
    adjMatrix = numpy.zeros([numOfSources,numOfEndPoints])
    #Set each value to be the permanence of the corresponding synapse or NaN if no synapse exists
    adjMatrix.fill(numpy.nan)
    for synapse in permanences:
        adjMatrix[synapse[0],synapse[1]]=synapse[2]
        
    #plot the matrix using arrayPlot
    returnValues = arrayPlot(adjMatrix)
    #make it big
    returnValues[0].set_size_inches(20,20)
    
    return returnValues
