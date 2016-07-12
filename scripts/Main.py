'''
Created on Jul 10, 2016

@author: Esi
'''
from os.path import join as opj
import os
import cPickle as pickle
from simulation.logger import Logger
from simulation.queue.srjfqueue import SRJFQueue
from simulation.feeder.core.parallelcore import ParallelCore
from simulation.queue.randomqueue import RandomQueue
from simulation.feeder.core.sequentialcore import SequentialCore
from simulation.event.eventhandler import EventHandler
from simulation.feeder.stochasticfeeder import StochasticFeeder
import random
from simulation.simulationtime import SimulationTime

if __name__ == '__main__':
    configs = []
    for root,_,files in os.walk(opj('..', 'configs')):
        for f in files:
            with open(opj(root, f), 'rb') as f:
                params = pickle.load(f)
            configs.append(params)
            
    configs = [configs[0]]
    for params in configs:
        print params
        random.seed = 1
        core_cnt = 3
        Logger.Instance().initialize(core_cnt)
         
        queue3 = SRJFQueue(params['k3'])
        core3 = ParallelCore(destination=None, core_id=2, queue=queue3, mean_server_time=params['m3'])
        
        queue2 = RandomQueue(params['k2'])
        core2 = SequentialCore(destination=core3, core_id=1, queue=queue2, mean_server_time=params['m2'], preemptive=False)
         
        queue1 = SRJFQueue(params['k1'])
        core1 = SequentialCore(destination=core3, core_id=0, queue=queue1, mean_server_time=params['m1'], preemptive=True)
         
        SimulationTime.Instance().initialize()
        EventHandler.Instance().initialize([core1, core2, core3], verbose=False)
        
        feeder1 = StochasticFeeder(destination=core1, rate=1.0/params['l1'])
        feeder1.create_arrival_event()
        
        feeder2 = StochasticFeeder(destination=core2, rate=1.0/params['l2'])
        feeder2.create_arrival_event()
        
        EventHandler.Instance().start()
        
        for i in xrange(core_cnt):
            print "Pb", i, ":", Logger.Instance().getPb(i)
            print "L", i, ":", Logger.Instance().getLHat(i)
            print "LQ", i, ":", Logger.Instance().getLHatQ(i)
        
        print "Ttot:", Logger.Instance().getTtotal()