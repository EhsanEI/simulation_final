'''
Created on Jul 10, 2016

@author: Esi
'''
import abc
from simulation.feeder.feeder import Feeder
from simulation import randomgenerator
from simulation.forwardable import Forwardable

class Core(Feeder, Forwardable):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta


    def __init__(self, destination, core_id, queue, mean_server_time):
        '''
        Constructor
        '''
        super(Core, self).__init__(destination)
        self.core_id = core_id
        self.queue = queue
        self.mean_server_time = mean_server_time
        
    @abc.abstractmethod
    def put(self, job):
        return
        
    @abc.abstractmethod
    def served_event(self):
        return
    
    @abc.abstractmethod
    def get_soonest_event(self):
        return
    
    @abc.abstractmethod
    def print_info(self):
        return