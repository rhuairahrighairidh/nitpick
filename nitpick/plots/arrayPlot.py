import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable

from tools import getClosestFactorPair

def arrayPlot(array, reshape=False, grid=True):
    """
    Plot an array with each item shown in grey.
    reshape specifies that the array should be reshaped to be as close to the target as possible whilst keeping to integer dimensions.
    reshape = True -> try and reshape the array to the golden Ratio
    reshape = 1.2 -> try and reshape the array to 1.2
    reshape = [20,30] -> try and reshape the array to 30/20 = 3/2 = 1.5
    """
    
    #make the array 2D if it is 1D so that matshow can plot it
    array = numpy.asarray(array)
    if len(array.shape)==1:
        array = numpy.asarray([array])
    
    #reshape the array if required
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
    imageAxes = axes.matshow(array,cmap='binary',interpolation='none')
    
    #add a colorbar next to the array plot (this appends a new axes next to the matshow one)
    divider = make_axes_locatable(axes)
    cAxes = divider.append_axes("right", size=0.15, pad=0.15)

    plt.colorbar(imageAxes, cax=cAxes)
    
    if grid:
        #draw gridlines between each array value
        locx = matplotlib.ticker.IndexLocator(1,0)
        locy = matplotlib.ticker.IndexLocator(1,0)
        
        axes.xaxis.set_minor_locator(locx)
        axes.yaxis.set_minor_locator(locy)
           
        axes.grid(True,axis='both',which='minor',linestyle='solid',color=(0.7,0.7,0.7))
        #Turn off major gridlines to stop them interfering
        axes.grid(False,axis='both',which='major')
    
    #Make the plot bigger
    figure.set_size_inches([9,6])

    return (figure, figure.axes)
    
