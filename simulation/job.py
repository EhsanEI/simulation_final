'''
Created on Jul 10, 2016

@author: Esi
'''
import numpy as np

class Job(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.elapsed_time = 0.0
        self.server_time = 0.0
    
    def forward(self, time):
        self.elapsed_time += time
        
    def remaining_time(self):
        return self.server_time - self.elapsed_time
    
    def __cmp__(self, other):
        return np.sign((self.remaining_time()) - (other.remaining_time())) 
        