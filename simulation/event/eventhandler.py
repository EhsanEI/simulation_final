'''
Created on Jul 11, 2016

@author: Esi
'''
from simulation.singleton import Singleton
from Queue import Queue
from simulation.simulationtime import SimulationTime
from _heapq import heappush, heappop
from simulation.logger import Logger

@Singleton
class EventHandler(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def initialize(self, cores, verbose=False):
        self._cores = cores
        self._verbose = verbose
        self._queue = []
        self._finished_jobs = 0
        self.all_jobs = 50
        self.warm_up = 10
        
    def put(self, event):
        heappush(self._queue, event)
        
    def check_candidates(self):
        cand_queue = []
        for core in self._cores:
            cand = core.get_soonest_event()
            if cand is not None:
                heappush(cand_queue, cand)
        
#         print 'candidates: ', [event.time for event in cand_queue]
        
        soonest_candidate = None
        if len(cand_queue) > 0:
            soonest_candidate = cand_queue[0] 
        
        soonest_event = None
        if len(self._queue) > 0:
            soonest_event = self._queue[0]
            
        if soonest_candidate is not None and soonest_event is not None and soonest_candidate < soonest_event:
            self.put(soonest_candidate)
            
    def job_finished(self):
        self._finished_jobs += 1
        
    def start(self):
        if self._verbose:
            print'------------------------------- starting event handler -------------------------------'
        while len(self._queue) > 0 and self._finished_jobs < self.all_jobs:
            event = heappop(self._queue)
            if self._verbose:
                print SimulationTime.Instance().get_time(), '->', event.time, event
            forward_time = event.time - SimulationTime.Instance().get_time()
            SimulationTime.Instance().forward(forward_time)
            for core in self._cores:
                core.forward(forward_time)
            event.handle()
            self.check_candidates()
            if (not Logger.Instance().active) and self._finished_jobs >= self.warm_up:
                Logger.Instance().activate()
            if self._verbose:
                self.print_info()
                print ''
            
            
    def print_info(self):
        for core in self._cores:
            core.print_info()