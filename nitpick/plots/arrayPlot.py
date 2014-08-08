import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker

from tools import getClosestFactorPair

def arrayPlot(array, reshape=False):
    """
    Plot an array with each item shown in grey.
    reshape specifies that the array should be reshaped to be as close to the target as possible whilst keeping to integer dimensions.
    reshape = True -> reshape the array to the golden Ratio
    reshape = 1.2 -> reshape the array to 1.2
    reshape = [20,30] -> reshape the array to 30/20 = 3/2 = 1.5
    """

    array = numpy.asarray(array)
    
    if reshape != False:
        if reshape is True:
            targetRatio = 1.618 #if no shape specified, try and reshape to the golden ratio
        else:
            targetRatio = reshape
        newShape = getClosestFactorPair(array.size, targetRatio) 
        array = array.reshape(newShape)


    #create a figure
    (figure,axes) = plt.subplots()
    
    #plot the array
    cAxes = axes.matshow(array,cmap='binary',interpolation='none')
    
    #add a colorbar next to the array plot
    figure.colorbar(cAxes)
    
    #draw gridlines between each array value
    locx = matplotlib.ticker.IndexLocator(1,0)
    locy = matplotlib.ticker.IndexLocator(1,0)
       
    axes.xaxis.set_minor_locator(locx)
    axes.yaxis.set_minor_locator(locy)
       
    axes.grid(True,axis='both',which='minor',linestyle='solid',color=(0.7,0.7,0.7))
