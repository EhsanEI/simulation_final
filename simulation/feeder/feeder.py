'''
Created on Jul 10, 2016

@author: Esi
'''
import abc


class Feeder(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, destination):
        super(Feeder, self).__init__()
        self.destination = destination
        