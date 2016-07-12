'''
Created on Jul 11, 2016

@author: Esi
'''
from simulation.event.simulationevent import SimulationEvent

class ServedEvent(SimulationEvent):
    '''
    classdocs
    '''


    def __init__(self, time, core):
        '''
        Constructor
        '''
        super(ServedEvent, self).__init__(time)
        self.core = core
        
    def handle(self):
        self.core.served_event()