'''
Created on Jul 10, 2016

@author: Esi
'''
from simulation.queue.corequeue import CoreQueue
import random

class RandomQueue(CoreQueue):
    '''
    classdocs
    '''


    def __init__(self, capacity):
        '''
        Constructor
        '''
        super(RandomQueue, self).__init__(capacity)
        self._queue = []
        
        
    def put(self, job):
        if self.full():
            return False
        self._queue.append(job)
        return True
    
    def pop(self):
        if self.get_length() <= 0:
            return None
        return self._queue.pop(random.randint(0,self.get_length()-1))
    
    def get_length(self):
        return len(self._queue)
    
    def get_head(self):
        raise Exception("No head in random queue")
        
    def foreach(self, func):
        for job in self._queue:
            func(job)