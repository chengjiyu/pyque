import random
import simpy
from models import source, msg_queue, server
from models import source_model, channel

RANDOM_SEED = 42
SIM_TIME = 20       # Simulation time

def session():
    menv = simpy.Environment()

    src_model = source_model.BaseSourceModel()
    soc = source.BaseSource(menv, src_model)
    mq = msg_queue.MsgQueue(menv)
    soc.dst = mq
    cn = channel.ErrorChannel()
    mq.server.set_channel(cn)

    random.seed(RANDOM_SEED)        # This helps reproducing the results
    menv.run(until = 1000)

def session1():
    env = simpy.Environment()

    src_model = source_model.BaseSourceModel()
    src = source.BaseSource(env, src_model)
    mq = msg_queue.MsgQueue(env)
    src.dst = mq
    ch = channel.ErrorChannel()
    mq.server.set_channel(ch)

    env.run(until = 100)

def main():
    session1()

if __name__ == "__main__":
    main()

