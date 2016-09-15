import simpy
from models import source, msg_queue, server
from models import source_model, channel

def session():
    menv = simpy.Environment()

    src_model = source_model.BaseSourceModel()
    soc = source.BaseSource(menv, src_model)
    mq = msg_queue.MsgQueue(menv)
    soc.dst = mq
    cn = channel.ErrorChannel()
    mq.server.set_channel(cn)

    menv.run(until = 1000)

def main():
    session()

if __name__ == "__main__":
    main()

