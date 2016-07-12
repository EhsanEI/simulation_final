'''
Created on Jul 10, 2016

@author: Esi
'''
from simulation.feeder.core.core import Core
from simulation.logger import Logger
from simulation import randomgenerator
from simulation.event.servedevent import ServedEvent
from simulation.simulationtime import SimulationTime
from simulation.event.eventhandler import EventHandler
from sklearn.externals import joblib


class ParallelCore(Core):
    '''
    classdocs
    '''


    def __init__(self, destination, core_id, queue, mean_server_time):
        '''
        Constructor
        '''
        super(ParallelCore, self).__init__(destination, core_id, queue, mean_server_time)
        
    def put(self, job):
        if self.queue.full():
            Logger.Instance().job_blocked(self.core_id)
            return
        
        job.server_time = randomgenerator.exponential_random(1.0/self.mean_server_time)
        job.elapsed_time = 0.0
        
        self.queue.put(job)
        
        Logger.Instance().job_added(self.core_id)
        
    def served_event(self):
        finished_job = self.queue.pop()
        print 'parallel removing: ', finished_job.remaining_time()
        assert finished_job.remaining_time() < 1e-4
        
        if self.destination is not None:
            self.destination.put(finished_job)
        
    def forward(self, time):
        self.queue.foreach( lambda job: job.forward((time*1.0)/self.queue.get_length()) )
        
        Logger.Instance().LQ(self.core_id, self.queue.get_length() * time)
        if self.queue.get_length() > 0:
            Logger.Instance().L(self.core_id,  time)
            
    def print_info(self):
        print 'prallel: ', self.core_id, self.queue.get_length()
        def print_remaining_time(job):
            print ' ', job.remaining_time()
        self.queue.foreach(print_remaining_time)
        
        
    def get_soonest_event(self):
        if self.queue.get_length() > 0:
            event = ServedEvent(SimulationTime.Instance().get_time() + (self.queue.get_head().remaining_time() * self.queue.get_length()), self)
            return event 