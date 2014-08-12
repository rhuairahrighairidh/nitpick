import numpy
from tools import flatten
import matplotlib.pyplot as plt

def permanenceEvolutionPlot(allPermanences,activeColumn):
    """
    Danger Function - until this is fixed make sure you have enough swap space
    """
    #Get a set of all the synapse indexes in the form (to, from)
    allIndexes=set([tuple(i[:2]) for i in flatten(allPermanences,level=1)])

    #go through all the synapses and add in any missing (use 0 permenence)
    for i in xrange(len(allPermanences)):
        currentIndexes = set((tuple(synapse[:2]) for synapse in allPermanences[i]))
        missingIndexes = allIndexes-currentIndexes
        missingSynapses = [list(index)+[0.0] for index in missingIndexes]
        allPermanences[i].extend(missingSynapses)

    #convert to a more sensible format now that the lists aren't different lengths
    synapses = numpy.asarray(allPermanences)

    #Select out all the synapses connected to column 'activeColumn'
    #sort them so that they line up for plotting
    subsetPermanences = numpy.asarray([sorted([s for s in timestep if s[0]==activeColumn],key=lambda item: item[1]) for timestep in synapses])[:,:,2]

    #Plot all the above synapse permanences
    (figure,axes) = plt.subplots()
    axes.plot(subsetPermanences)
    figure.set_size_inches(20,5)
    
    return (figure,figure.axes)
    
