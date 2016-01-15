import simpy
from unit import Pdu
from msg_queue import MsgQueue
from channel import ErrorChannel, Channel
from numpy import random


class Server(object):
    def __init__(self):
        pass


class BaseServer(Server):

    def __init__(self, env, queue, serve_rate = 1):
        assert isinstance(queue. MsgQueue)
        super(BaseServer, self).__init__()
        assert isinstance(env, simpy.Environment)
        self.__env = env
        self.__queue = queue
        self.__serve_rate = serve_rate

    def get_rate(self):
        return self.__serve_rate

    def set_rate(self, serve_rate):
        self.__serve_rate = serve_rate
    serve_rate = property(get_rate, set_rate, None, 'serve rate of the server')

    #TODO: get the serve size according to channel state
    def get_serve_size(self):
        return 1400

    def serve(self, serve_pdu):
        assert isinstance(serve_pdu, Pdu)
        duration = random.exponential(self.__serve_rate)
        serve_pdu.on_serve_begin()
        yield self.__env.process(self.do_serve(duration))
        serve_pdu.on_serve_end()
        self.__queue.action.interrupt()

    def do_serve(self, duration):
        yield(self.__env.timeout(duration))