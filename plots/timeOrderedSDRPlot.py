import numpy
import matplotlib.pyplot as plt
import matplotlib

def timeOrderedSDRPlot(activeColumns):
    #Make sure inputs are numpy arrays
    activeColumns = numpy.asarray(activeColumns)
    
    
    ##Transform the input values into x and y coordinates
    
    #Calculate x values -FIX THIS - it won't work if the number of active columns varies with time
    #for each active bit, the x value is the time when it was active
    xValues = numpy.array([range(activeColumns.shape[0])])
    xValues = numpy.repeat(xValues.T,activeColumns.shape[1],axis=1)
    xValues = xValues.flatten()

    #Calculate y values 
    #for each active bit the y value is the time when that bit was first active
    def transformActiveColumnIndexes(activeColumns):

        pastIndexes = []
        yValues = []
        for activeColumn in activeColumns.flatten():
            if activeColumn not in pastIndexes:
                pastIndexes.append(activeColumn)
            yValue = pastIndexes.index(activeColumn)
            yValues.append(yValue)

        return yValues

    yValues = numpy.asarray(transformActiveColumnIndexes(activeColumns))
    
    
    ##Plot the x and y coordinates
    
    #set up plot
    (figure,axes) = plt.subplots()
    #plot the actiive bits
    axes.plot(xValues,yValues,'.')
    #display the horizontal grid
    axes.minorticks_on()
    axes.grid(True,axis='y',which='both',linestyle='solid',color=(0.7,0.7,0.7))
    #Set the horizontal gridlines to have spacing of 1
    axes.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1))

    #Add a gap to the bottom and left edges so all points can be seen
    axes.set_xlim(left=-1)
    axes.set_ylim(bottom=-1)

    #set plot aspect ratio so the axes are even.
    axes.set_aspect(aspect='equal')
    #Make the plot bigger (the plot expands to box whilst retaining aspect ratio)
    figure.set_size_inches(15,15)

