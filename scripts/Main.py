'''
Created on Jul 10, 2016

@author: Esi
'''
from os.path import join as opj
import os
import cPickle as pickle

if __name__ == '__main__':
    configs = []
    for root,_,files in os.walk(opj('..', 'configs')):
        for f in files:
            with open(opj(root, f), 'rb') as f:
                params = pickle.load(f)
            configs.append(params)
            
    for params in configs:
        pass