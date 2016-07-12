'''
Created on Jul 10, 2016

@author: Esi
'''
from simulation.queue.corequeue import CoreQueue
from heapq import heappop, heappush

class SRJFQueue(CoreQueue):
    '''
    classdocs
    '''

    def __init__(self, capacity):
        '''
        Constructor
        '''
        super(SRJFQueue, self).__init__(capacity)
        self._heap = []
        
        
    def put(self, job):
        if self.full():
            return False
        heappush(self._heap, job)
        return True
    
    def pop(self):
        if self.get_length() <= 0:
            return None
        return heappop(self._heap)
    
    def get_length(self):
        return len(self._heap)
        
    def get_head(self):
        return self._heap[0]
         
    def foreach(self, func):
        for job in self._heap:
            func(job)