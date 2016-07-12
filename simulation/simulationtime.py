'''
Created on Jul 10, 2016

@author: Esi
'''

from simulation.forwardable import Forwardable
from simulation.singleton import Singleton


@Singleton
class SimulationTime(Forwardable):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._time = 0.0
        
    def get_time(self):
        return self._time
    
    def forward(self, time):
        assert time > 0
        self._time += time