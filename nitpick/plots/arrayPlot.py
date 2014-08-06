import matplotlib.pyplot as plt
import matplotlib.ticker

def arrayPlot(array):
    #create a figure
    (figure,axes) = plt.subplots()
    
    #plot the array
    cAxes = axes.matshow(array,cmap='binary')
    
    #add a colorbar next to the array plot
    figure.colorbar(cAxes)
    
    #draw gridlines between each array value
    loc = matplotlib.ticker.IndexLocator(1,0)
    
    axes.xaxis.set_minor_locator(loc)
    axes.yaxis.set_minor_locator(loc)
       
    axes.grid(True,axis='both',which='minor',linestyle='solid',color=(0.7,0.7,0.7))
