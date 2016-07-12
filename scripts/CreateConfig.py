'''
Created on Jul 10, 2016

@author: Esi
'''
from os.path import join as opj
import cPickle as pickle

if __name__ == '__main__':
    params = {}
    
    params['l1'] = 7.0
    params['m1'] = 5.0 
    params['k1'] = 100
    params['l2'] = 2.0
    params['m2'] = 3.0
    params['k2'] = 12
    params['m3'] = 1.0
    
    ind = 0
    for k3 in xrange(8,17):
        params['k3'] = k3
        
        with open(opj('..', 'configs', str(ind)), 'wb') as f:
            pickle.dump(params, f)
            
        ind += 1