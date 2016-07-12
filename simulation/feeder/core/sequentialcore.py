'''
Created on Jul 10, 2016

@author: Esi
'''
from simulation.feeder.core.core import Core
from simulation import randomgenerator
from simulation.event.servedevent import ServedEvent
from simulation.simulationtime import SimulationTime
from simulation.event.eventhandler import EventHandler
from simulation.logger import Logger

class SequentialCore(Core):
    '''
    classdocs
    '''


    def __init__(self, destination, core_id, queue, mean_server_time, preemptive):
        '''
        Constructor
        '''
        super(SequentialCore, self).__init__(destination, core_id, queue, mean_server_time)
        self.preemptive = preemptive
        self.current_job = None
        
    def put(self, job):
        if self.queue.full():
            Logger.Instance().job_blocked(self.core_id)
            return
        
        job.server_time = randomgenerator.exponential_random(1.0/self.mean_server_time)
        job.elapsed_time = 0.0
        
        if self.preemptive:
            if self.current_job is None:
                self.set_as_current(job)
            elif self.current_job > job:
                self.queue.put(self.current_job)
                self.set_as_current(job)
            else:
                self.queue.put(job)
        else:
            if self.current_job is None:
                self.set_as_current(job)
            else:
                self.queue.put(job)
        
        Logger.Instance().job_added(self.core_id)
        
    def set_as_current(self, job):
        self.current_job = job
        
    def served_event(self):
#         print 'sequential removing: ', self.current_job.remaining_time()
        assert self.current_job.remaining_time() < 1e-4
        
        if self.destination is not None:
            self.destination.put(self.current_job)
        else:
            EventHandler.Instance().job_finished()
            
        if self.queue.get_length() > 0:
            self.set_as_current(self.queue.pop())
        else:
            self.current_job = None
        
    def forward(self, time):
        if self.current_job is not None:
            self.current_job.forward(time)
        
        Logger.Instance().LQ(self.core_id, self.queue.get_length() * time)
        if self.current_job is not None:
            Logger.Instance().L(self.core_id,  time)
            
    def print_info(self):
        print 'sequential: ', self.core_id, self.queue.get_length(), 0 if self.current_job is None else 1
        def print_remaining_time(job):
            print '   ', job.remaining_time()
        if self.current_job is not None:
            print ' ', self.current_job.remaining_time()
        self.queue.foreach(print_remaining_time)
        
    def get_soonest_event(self):
        if self.current_job is not None:
            event = ServedEvent(SimulationTime.Instance().get_time() + self.current_job.remaining_time(), self)
            return event