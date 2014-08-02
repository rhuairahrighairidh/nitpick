import json
import os
from cerebro2.paths import Paths


##model state reloading
class History():
    def __init__(self, dataDir='/tmp/cerebro2/model', modelID=None):
        self.paths = Paths(dataDir, deleteExisting=False)
    
    def getNumberOfIterations(self):
        fileNames = os.listdir(self.paths.states())
        listOfIterations = [state for state in fileNames if not state.startswith(".")]
        return len(listOfIterations)
        
        
        
    def inputDimensions(self):
        return readJSON(self.paths.dimensions("input"))
    
    def dimensions(self):
        return readJSON(self.paths.dimensions("output"))
    
    def inputVector(self):
        inputVector = []       
        for iteration in xrange(1,self.getNumberOfIterations()+1):
            inputVector.append(readJSON(self.paths.activeCells("input", iteration)))
        return inputVector
    
    def activeColumns(self):
        activeColumns = []       
        for iteration in xrange(1,self.getNumberOfIterations()+1):
            activeColumns.append(readJSON(self.paths.activeColumns("output", iteration)))
        return activeColumns
        
    def activeCells(self):
        activeCells = []       
        for iteration in xrange(1,self.getNumberOfIterations()+1):
            activeCells.append(readJSON(self.paths.activeCells("output", iteration)))
        return activeCells
    
    def predictiveCells(self):
        predictiveCells = []       
        for iteration in xrange(1,self.getNumberOfIterations()+1):
            predictiveCells.append(readJSON(self.paths.predictedCells("output", iteration)))
        return predictiveCells
    
    def proximalSynapses(self):
        proximalSynapses = []       
        for iteration in xrange(1,self.getNumberOfIterations()+1):
            proximalSynapses.append(readJSON(self.paths.proximalSynapses("output", iteration)))
        return proximalSynapses

        
    #encoder stuff
    def encoderInputs(self):
        encoderInputs = {}
        for encoderDetails in readJSON(self.paths.encoders()):
            name = encoderDetails['name']
            encoderInputs[name] = []
            for iteration in xrange(1,self.getNumberOfIterations()+1):
                encoderInputs[name].append(readJSON(self.paths.encoderInput(name, iteration)))
        return encoderInputs
        
    def encoderOutputs(self):
        encoderOutputs = {}
        for encoderDetails in readJSON(self.paths.encoders()):
            name = encoderDetails['name']
            encoderOutputs[name] = []
            for iteration in xrange(1,self.getNumberOfIterations()+1):
                encoderOutputs[name].append(readJSON(self.paths.encoderOutput(name, iteration)))
        return encoderOutputs
        
    def encoderNeighbors(self):
        encoderNeighbors = {}
        for encoderDetails in readJSON(self.paths.encoders()):
            name = encoderDetails['name']
            encoderNeighbors[name] = []
            for iteration in xrange(1,self.getNumberOfIterations()+1):
                encoderNeighbors[name].append(readJSON(self.paths.coordinateEncoderNeighbors(name, iteration)))
        return encoderNeighbors

    def encoderTopWCoordinates(self):
        encoderTopWCoordinates = {}
        for encoderDetails in readJSON(self.paths.encoders()):
            name = encoderDetails['name']
            encoderTopWCoordinates[name] = []
            for iteration in xrange(1,self.getNumberOfIterations()+1):
                encoderTopWCoordinates[name].append(readJSON(self.paths.coordinateEncoderTopWCoordinates(name, iteration)))
        return encoderTopWCoordinates



def readJSON(filepath):
  with open(filepath, 'r') as infile:
    return json.load(infile)

##model state saving
#TODO This will attach a History object that loads data from the default location only

from cerebro2.patcher import Patcher

originalPatchSP = Patcher.patchSP
def modifiedPatchSP(*args, **kwargs):
    result = originalPatchSP(*args, **kwargs)
    args[1].history = History()
    return result
Patcher.patchSP = modifiedPatchSP


originalPatchTP = Patcher.patchTP
def modifiedPatchTP(*args, **kwargs):
    result = originalPatchTP(*args, **kwargs)
    args[1].history = History()
    return result
Patcher.patchTP = modifiedPatchTP

#TODO Attach history objects to patched encoders and 'CLAModels'
