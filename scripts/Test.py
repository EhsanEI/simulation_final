'''
Created on Jul 10, 2016

@author: Esi
'''
from simulation.feeder.core.core import Core
from simulation.logger import Logger
from simulation.simulationtime import SimulationTime
from simulation.job import Job
from simulation.queue.srjfqueue import SRJFQueue
from simulation.queue.randomqueue import RandomQueue
from simulation.feeder.stochasticfeeder import StochasticFeeder
from simulation.feeder.core.sequentialcore import SequentialCore
from simulation.event.servedevent import ServedEvent
from simulation.event.eventhandler import EventHandler
import random
from simulation.feeder.core.parallelcore import ParallelCore

def test_logger():
    core_cnt = 3
    Logger.Instance().initialize(core_cnt)
    
    Logger.Instance().job_added(0)
    Logger.Instance().job_added(0)
    Logger.Instance().job_added(0)
    Logger.Instance().job_added(0)
    Logger.Instance().job_blocked(0)
    Logger.Instance().job_blocked(0)
    Logger.Instance().job_blocked(0)
    
    Logger.Instance().L(0, 10)
    Logger.Instance().LQ(0, 0)
    SimulationTime.Instance().forward(1)
    Logger.Instance().L(0, 10)
    Logger.Instance().LQ(0, 0)
    SimulationTime.Instance().forward(1)
    Logger.Instance().L(0, 1)
    Logger.Instance().LQ(0, 1)
    SimulationTime.Instance().forward(1)
    
    print "Pb ", Logger.Instance().getPb(0)
    print "LHat ", Logger.Instance().getLHat(0)
    print "LQHat ", Logger.Instance().getLHatQ(0)
    print "TTotal ", Logger.Instance().getTtotal()
    
def test_queue():
    queue = RandomQueue(5)
    
    jobs = []
    for _ in xrange(10):
        jobs.append(Job())
    
    jobs[0].server_time = 10.0
    jobs[1].server_time = 10.0
    jobs[2].server_time = 10.0
    jobs[0].forward(1)
    jobs[1].forward(3)

    print queue.put(jobs[0])
    print queue.put(jobs[1])
    print queue.put(jobs[2])
    
    print queue.pop().elapsed_time
    
    print queue.put(jobs[3])
    print queue.put(jobs[4])
    print queue.put(jobs[5])
    print queue.put(jobs[6])
    
def test_core():
    
    core_cnt = 1
    Logger.Instance().initialize(core_cnt)
    
    queue = RandomQueue(5)
    core = SequentialCore(destination=None, core_id=0, queue=queue, mean_server_time=3, preemptive=False)
    
    jobs = []
    for _ in xrange(10):
        jobs.append(Job())

    core.put(jobs[0])
    
    print jobs[0].server_time
    print jobs[0].elapsed_time
    
def test_stochastic_feeder():
#     random.seed = 1
    core_cnt = 2
    Logger.Instance().initialize(core_cnt)
    
    queue2 = SRJFQueue(3)
    core2 = ParallelCore(destination=None, core_id=0, queue=queue2, mean_server_time=5.0)
    
    queue1 = RandomQueue(5)
    core1 = SequentialCore(destination=core2, core_id=1, queue=queue1, mean_server_time=1.0, preemptive=False)
    
    EventHandler.Instance().initialize([core1, core2])
    
    feeder = StochasticFeeder(destination=core1, rate=3.0)
    feeder.create_arrival_event()
    
    EventHandler.Instance().start()
    
if __name__ == '__main__':
    test_stochastic_feeder()