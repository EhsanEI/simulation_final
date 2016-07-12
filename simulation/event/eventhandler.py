'''
Created on Jul 11, 2016

@author: Esi
'''
from simulation.singleton import Singleton
from Queue import Queue
from simulation.simulationtime import SimulationTime
from _heapq import heappush, heappop

@Singleton
class EventHandler(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._queue = []
        
    def initialize(self, cores):
        self._cores = cores
        
    def put(self, event):
        heappush(self._queue, event)
        
    def check_candidates(self):
        cand_queue = []
        for core in self._cores:
            cand = core.get_soonest_event()
            if cand is not None:
                heappush(cand_queue, cand)
        
        print 'candidates: ', [event.time for event in cand_queue]
        
        soonest_candidate = None
        if len(cand_queue) > 0:
            soonest_candidate = cand_queue[0] 
        
        soonest_event = None
        if len(self._queue) > 0:
            soonest_event = self._queue[0]
            
        if soonest_candidate is not None and soonest_event is not None and soonest_candidate < soonest_event:
            self.put(soonest_candidate)
        
    def start(self):
        while len(self._queue) > 0 and SimulationTime.Instance().get_time() < 10:
            event = heappop(self._queue)
            print SimulationTime.Instance().get_time(), '->', event.time, event
            forward_time = event.time - SimulationTime.Instance().get_time()
            SimulationTime.Instance().forward(forward_time)
            for core in self._cores:
                core.forward(forward_time)
            event.handle()
            self.check_candidates()
            self.print_info()
            print ''
            
            
    def print_info(self):
        for core in self._cores:
            core.print_info()