'''
Created on Jul 10, 2016

@author: Esi
'''
import random
import numpy as np

def exponential_random(rate):
    x = random.random()
    return -(np.log(1-x))/rate