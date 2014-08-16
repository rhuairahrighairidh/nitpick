import numpy
from tools import flatten
import matplotlib.pyplot as plt

def permanenceEvolutionPlot(allPermanences,bitIndex):
    """
    allPermanences is a list of synapses across time - the result returned by history.proximal_synapses()
    bitIndex is the index of the column you want to plot the synapses for
    """
    #take out only synapses connectd to active bit
    permanences = [[s for s in timestep if s[0]==bitIndex] for timestep in allPermanences]

    
    #Get a set of all the synapse indexes in the form (to, from)
    allIndexes=set([tuple(i[:2]) for i in flatten(permanences,level=1)])

    #go through all the synapses and add in any missing (use 0 permenence)
    for i in xrange(len(permanences)):
        currentIndexes = set((tuple(synapse[:2]) for synapse in permanences[i]))
        missingIndexes = allIndexes-currentIndexes
        missingSynapses = [list(index)+[0.0] for index in missingIndexes]
        permanences[i].extend(missingSynapses)

    #convert to a more sensible format now that the lists aren't different lengths
    synapses = numpy.asarray(permanences)

    #Select out all the synapses connected to column 'bitIndex'
    #sort them so that they line up for plotting
    sortedPermanences = numpy.asarray([sorted(timestep,key=lambda item: item[1]) for timestep in synapses])[:,:,2]

    #Plot all the above synapse permanences
    (figure,axes) = plt.subplots()
    axes.plot(sortedPermanences)
    figure.set_size_inches(20,5)

    return (figure,figure.axes)
    
    
