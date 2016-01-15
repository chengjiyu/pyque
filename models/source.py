import simpy
from numpy import random
from unit import Message
from msg_queue import MsgQueue

discrete_distributions = dict(binomial=random.binomial, geometric=random.geometric)


class Source(object):
    """
    source generator in queueing theory
    generates customers as a given process
    default is Possion process with lambda = 1
    Usage: source(env, gen_rate = 1,compound = False, comp_dist = None, comp_dist_params = None)
    """

    def __init__(self, env, **kwargs):
        assert (isinstance(env, simpy.Environment()))
        self.__env = env

        if 'gen_rate' in kwargs:
            self.__gen_rate = kwargs['gen_rate']
        else:
            self.__gen_rate = 1.

        if 'compound' in kwargs:
            self.__compound = kwargs['compound']
            if self.__compound:
                assert (kwargs['comp_dist'] is not None)
                assert (kwargs['comp_dist_params'] is not None)
                self.__comp_dist = discrete_distributions[kwargs['comp_dist']]
                self.__comp_dist_params = kwargs['comp_dist_params']

        self.action = self.__env.process(self.run())
        self.__dst_server = None

    def run(self):
        assert (self.__dst_server is not None)
        while True:
            interval = random.exponential(self.__gen_rate)
            packet_num = self.__comp_dist(self.__comp_dist_params)
            msg = Message(self.__env, packet_num)
            self.sendto(self.__dst, msg)
            yield self.__env.timeout(interval)

    def sendto(self, dst, msg):
        assert isinstance(dst, MsgQueue)
        assert isinstance(msg, Message)
        dst.on_arrival(msg)

