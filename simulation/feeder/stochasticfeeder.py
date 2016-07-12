'''
Created on Jul 10, 2016

@author: Esi
'''
from simulation.feeder.feeder import Feeder
from simulation.job import Job
from simulation.randomgenerator import exponential_random
from simulation import randomgenerator
from simulation.event.arrivalevent import ArrivalEvent
from simulation.simulationtime import SimulationTime
from simulation.event.eventhandler import EventHandler

class StochasticFeeder(Feeder):
    '''
    classdocs
    '''

    def __init__(self, destination, rate):
        '''
        Constructor
        '''
        super(StochasticFeeder, self).__init__(destination)
        self.rate = rate
        
    def arrival_event(self):
        job = Job()
        self.destination.put(job)
        self.create_arrival_event()
        
    def create_arrival_event(self):
        new_time = SimulationTime.Instance().get_time() 
        new_time += randomgenerator.exponential_random(self.rate)
        event = ArrivalEvent(new_time, self)
        EventHandler.Instance().put(event)