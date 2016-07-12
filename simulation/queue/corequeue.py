'''
Created on Jul 10, 2016

@author: Esi
'''
import abc

class CoreQueue(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta


    def __init__(self, capacity):
        '''
        Constructor
        '''
        self.capacity = capacity
        
    @abc.abstractmethod
    def put(self, job):
        return
    
    @abc.abstractmethod
    def pop(self):
        return
    
    @abc.abstractmethod
    def get_length(self):
        return
        
    @abc.abstractmethod
    def foreach(self, func):
        return
    @abc.abstractmethod
    def get_head(self):
        return
    
    def full(self):
        return self.get_length() >= self.capacity