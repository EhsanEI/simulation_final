'''
Created on Jul 11, 2016

@author: Esi
'''
from simulation.event.simulationevent import SimulationEvent

class ArrivalEvent(SimulationEvent):
    '''
    classdocs
    '''


    def __init__(self, time, feeder):
        '''
        Constructor
        '''
        super(ArrivalEvent, self).__init__(time)
        self.feeder = feeder
        
    def handle(self):
        self.feeder.arrival_event()