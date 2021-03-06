'''
Created on Jul 10, 2016

@author: Esi
'''
from simulation.singleton import Singleton
from simulation.simulationtime import SimulationTime

@Singleton
class Logger(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.active = False
        self.warmup_time = 0
    
    def activate(self):
        self.active = True
        self.warmup_time = SimulationTime.Instance().get_time()
        
    def initialize(self, core_cnt):
        self.sumL = [0] * core_cnt
        self.sumLQ = [0] * core_cnt
        self.added_jobs = [0] * core_cnt
        self.blocked_jobs = [0] * core_cnt
        
    def job_added(self, core_id):
        if not self.active:
            return 
        self.added_jobs[core_id] += 1
    
    def job_blocked(self, core_id):
        if not self.active:
            return
        self.blocked_jobs[core_id] += 1
    
    def L(self, core_id, length):
        if not self.active:
            return
        self.sumL[core_id] += length
            
    def LQ(self, core_id, length):
        if not self.active:
            return
        self.sumLQ[core_id] += length
        
    def getPb(self, core_id):
        return (self.blocked_jobs[core_id]*1.0)/(self.blocked_jobs[core_id] + self.added_jobs[core_id])
    
    def getLHat(self, core_id):
        return (self.sumL[core_id]*1.0)/(SimulationTime.Instance().get_time() - self.warmup_time)
    
    def getLHatQ(self, core_id):
        return (self.sumLQ[core_id]*1.0)/(SimulationTime.Instance().get_time() - self.warmup_time)
    
    def getTtotal(self):
        return ((sum(self.sumL) + sum(self.sumLQ)) *1.0)/(sum(self.added_jobs))