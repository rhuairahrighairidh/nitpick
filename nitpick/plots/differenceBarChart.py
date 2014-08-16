import numpy
import matplotlib.pyplot as plt
import matplotlib
import operator
from functools import reduce

def differenceBarChart(activeColumns,arraySize=None):
    #Make sure inputs are numpy arrays
    activeColumns = numpy.asarray(activeColumns)
    
    
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
    figure.set_size_inches(20,20) #plot keeps aspect ratio from above and expands to fill this box
    
    
    #Set up another axis to show percentage
    if arraySize != None:
        try:
            arraySize = float(arraySize) #converting to int might produce unexpected behaviour if you input a float
        except:
            #assumes arraySize is a list of dimensions
            arraySize = reduce(operator.mul, arraySize, 1)
            
        def convertToPercentage(numberOfColumns,totalNumberOfColumns=arraySize):
            return 100*float(numberOfColumns)/float(totalNumberOfColumns)
        
        percentageAxis = axes.twinx()
        percentageAxis.set_ylim(bottom=convertToPercentage(axes.get_ylim()[0]),top=convertToPercentage(axes.get_ylim()[1]))
        percentageAxis.set_aspect(barScreenAspectRatio/percentageAxis.get_ylim()[1], adjustable='box-forced')
        percentageAxis.set_ylabel("%")
    
    return (figure, figure.axes)


