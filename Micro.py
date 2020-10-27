import math
from pprint import pprint
class Micro :
    firstProcess = True
    processList = []
    finalTime = 0

    def __init__(self, id, blockTime, quantum, tcc):
            self.id = id
            self.blockTime = blockTime
            self.quantum = quantum
            self.tcc = tcc



    def calculateTvc(self, executionTime):
        value = (math.ceil(executionTime / self.quantum) -1 ) * self.tcc
        return value
  
  
  
    def fillTable(self, process): 
        executionTime= process.executionTime
        if(self.finalTime < process.startTime):
            self.processList.append([self.id, "WAITING", 0, 0,0,0,0,self.finalTime,process.startTime])
        if(self.firstProcess or self.finalTime < process.startTime):
            currentTcc=0
            self.firstProcess = False
        else:
            currentTcc=self.tcc
        tvc= self.calculateTvc(process.executionTime)
        tb= self.blockTime*process.numberBlocks
        tt= executionTime+currentTcc+ tvc+ tb
        if self.finalTime >= process.startTime: 
            initalTime = self.finalTime
        else:
            initalTime = process.startTime
        tf = tt + initalTime
        self.finalTime = tf
        
        self.processList.append([self.id, process.id, executionTime, currentTcc,tvc,tb,tt,initalTime,tf])
        
    
    
            
