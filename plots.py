import numpy
import matplotlib.pyplot as plt
import matplotlib


def differenceBarChart(activeColumns,dimensions):
    #Make sure inputs are numpy arrays
    activeColumns = numpy.asarray(activeColumns)
    dimensions = numpy.asarray(dimensions)
    
    
    
    ##Transform the input before plotting (compute the differences between consecutive states)
    
    import itertools
    #Example function from itertools documentation. Used for looping through a list in pairs
    def pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = itertools.tee(iterable)
        next(b, None)
        return itertools.izip(a, b)
    
    turnOns=[] # list containing the number of bits that became active (from inactive) between each timestep
    turnOffs=[] # list containing the number of bits that became inactive (from active) between each timestep
    stayOns=[] # list containing the number of bits that remained active between each timestep
    #calculate the above lists
    for inputPair in pairwise(activeColumns):
        numberThatTurnOn = len(numpy.setdiff1d(*inputPair))
        numberThatTurnOff = len(numpy.setdiff1d(*inputPair)) # "remove from arr1 all the elements that are also in arr2"
        numberThatStayOn = len(numpy.intersect1d(*inputPair))
        turnOns.append(numberThatTurnOn)
        turnOffs.append(numberThatTurnOff)
        stayOns.append(numberThatStayOn)
        
        
        
        
    ##Plot the differences between states
    
    #Define the colors used for the bars
    darkOrange = numpy.array([96,63,32])/255.0
    darkGreen = numpy.array([67,93,51])/255.0
    lightGreen = numpy.array([160,191,139])/255.0
    
    #Create the plotting objects
    (figure,axes) = plt.subplots()
    #Set the bars so that the edges lie on whole numbers - to emphasise that that each bar shows the difference between consecutive states
    xPositionsOfBars = numpy.arange(activeColumns.shape[0]-1)
    #Plot the bars (as a stacked bar chart (which matplotlib doesn't seem to automatically support))
    axes.bar(xPositionsOfBars,stayOns, width=1, color=darkOrange)
    axes.bar(xPositionsOfBars,turnOns, width=1, color=darkGreen, bottom=stayOns)
    axes.bar(xPositionsOfBars,turnOffs, width=1, color=lightGreen, bottom=[stayOns[j] +turnOns[j] for j in range(len(stayOns))])
    #get rid of annoying gap at the end
    axes.set_xlim(right=xPositionsOfBars[-1]+1)
    
    #set the aspect ratio of the plot so that the tallest column is a fixed aspec ratio (actually uses the maximum of the y axis, not the maximum column height)
    barScreenAspectRatio=15
    axes.set_aspect(barScreenAspectRatio/axes.get_ylim()[1], adjustable='box-forced')
    #make the plot bigger
    figure.set_size_inches(15,10) #plot keeps aspect ratio from above and expands to fill this box
    
    
    #Set up another axis to show percentage
    def convertToPercentage(numberOfColumns,totalNumberOfColumns=dimensions[0]*dimensions[1]):
        return 100*float(numberOfColumns)/float(totalNumberOfColumns)
    
    percentageAxis = axes.twinx()
    percentageAxis.set_ylim(bottom=convertToPercentage(axes.get_ylim()[0]),top=convertToPercentage(axes.get_ylim()[1]))
    percentageAxis.set_aspect(barScreenAspectRatio/percentageAxis.get_ylim()[1], adjustable='box-forced')
    percentageAxis.set_ylabel("%")
    
    #return figure #Not sure if this is the appropriate thing to return for custom plots






def timeOrderedSDRPlot(activeColumns):
    #Make sure inputs are numpy arrays
    activeColumns = numpy.asarray(activeColumns)
    
    
    #Transform the input values into x and y coordinates
    
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
    
    
    #Plot the x and y coordinates
    
    #set up plot
    (figure,axes) = plt.subplots()
    #plot the actiive bits
    axes.plot(xValues,yValues,'o')
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

