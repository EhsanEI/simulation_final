'''
Created on Jul 10, 2016

@author: Esi
'''
import abc

class Forwardable(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        pass

    @abc.abstractmethod
    def forward(self, time):
        return
        