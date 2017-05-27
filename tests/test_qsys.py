import random
import simpy
import numpy as np
from models import source, msg_queue, server
from models import source_model, channel
import logging

RANDOM_SEED = 42
SIM_TIME = 20       # Simulation time

def session1():
    env = simpy.Environment()

    # Q = np.array([[0.1, 0.2, 0.3, 0.4], [0.25, 0.25, 0.25, 0.25], [0.15, 0.25, 0.35, 0.25], [0, 0.3, 0.3, 0.4]])
    # Lambda = np.array([0.5, 1.0, 1.5, 2.0])
    Q = np.array([[0.7716, 0.2284], [0.5, 0.5]])      # [[1.0 - 0.4567804514083193434060809550457*z,0.4567804514083193434060809550457*z], [z,1-z]]
    # Q = np.array([[0.99411, 0.00589], [0.00589, 0.99411]])
    Lambda = np.array([1.0722, 0.48976])
    mmpp = source_model.MMPPModel(Q, Lambda)
    # tcp = source_model.TcpSourceModel(7000.)
    src = source.BaseSource(env, mmpp)
    mq = msg_queue.MsgQueue(env)
    src.dst = mq
    ch = channel.ErrorChannel()
    mq.server.set_channel(ch)

    random.seed(RANDOM_SEED)        # This helps reproducing the results
    env.run(until = 5000)

def main():
    session1()

if __name__ == "__main__":
    main()
