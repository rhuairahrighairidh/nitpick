import numpy
import matplotlib.pyplot as plt
import matplotlib

def densityOrderedSDRPlot(activeColumns):
    #Make sure inputs are numpy arrays
    activeColumns = numpy.asarray(activeColumns)
    
    
    ##Transform the input values into x and y coordinates
    
    #Calculate x values -FIX THIS - it won't work if the number of active columns varies with time
    #for each active bit, the x value is the time when it was active
    xValues = numpy.array([range(activeColumns.shape[0])])
    xValues = numpy.repeat(xValues.T,activeColumns.shape[1],axis=1)
    xValues = xValues.flatten()

    #Calculate y values 
    #for each active bit the y value is the number of times that bit is active over the whole time range
    from collections import Counter
    from operator import itemgetter

    inputIndexes = activeColumns.flatten()

    #get a list of tuples - [(columnIndex,count),(columnIndex, count),...]
    c=Counter(inputIndexes).items()
    #sort this list by column index first
    s=sorted(c,key=itemgetter(0))
    #then sort the sorted list by count (so columns that have the same count will be sorted by index)
    sortedCounts = sorted(s,key=itemgetter(1),reverse=True)
    #reassign the count number in each tuple to be the position in the list
    d=[]
    for i in xrange(len(sortedCounts)):
        item = list(sortedCounts[i])
        item[1] = i
        d.append(item)
    columnRank = dict(d)

    yValues = numpy.asarray([columnRank[index] for index in inputIndexes])
    
    
    
    #Calculate horizontal grid lines
    
    #split up plot into bands of the same activation count ie group the 'columns' by activation count
    yTickPositions = []
    lastValue = None
    for i in xrange(len(sortedCounts)):
        currentValue = sortedCounts[i][1]
        if currentValue != lastValue:
            yTickPositions.append(i)
        lastValue = currentValue
    yTickPositions = numpy.asarray(yTickPositions) + 0.5 #the y ticks should divide the columns into groups, so they go between line, hence the 0.5
    
    
    
    ##Plot the x and y coordinates
    
    #set up plot
    (figure,axes) = plt.subplots()
    #plot the values
    axes.plot(xValues,yValues,'.')

    #display the horizontal grid lines that go through each line of markers
    axes.minorticks_on()
    axes.grid(True,axis='y',which='minor',linestyle='solid',color=(0.7,0.7,0.7))
    axes.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1))

    #display the horizontal lines that seperate the columns into activation amounts
    axes.grid(True,axis='y',which='major',linestyle='solid',color=(0.3,0.3,0.3))
    axes.set_yticks(yTickPositions)
    axes.set_yticklabels(numpy.unique([item[1] for item in sortedCounts])[::-1])

    #Add a gap to the bottom and left edges so all points can be seen
    axes.set_xlim(left=-1)
    axes.set_ylim(bottom=-1)

    #set plot aspect ratio so the axes are even. Make the plot bigger (the plot expands to the maximum size allowed by aspect ratio)
    axes.set_aspect(aspect='equal')
    figure.set_size_inches(15,15)

    return figure

