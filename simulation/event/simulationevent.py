'''
Created on Jul 11, 2016

@author: Esi
'''
import abc
import numpy as np

class SimulationEvent(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, time):
        '''
        Constructor
        '''
        self.time = time
    
    @abc.abstractmethod
    def handle(self):
        pass
    
    def __cmp__(self, other):
        return np.sign(self.time - other.time)