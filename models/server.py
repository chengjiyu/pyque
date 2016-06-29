import simpy
from numpy import random

from .unit import Pdu
from .channel import ErrorChannel, Channel


class Server(object):
    def __init__(self):
        pass


class BaseServer(Server):

    def __init__(self, env, queue):
        super(BaseServer, self).__init__()
        assert isinstance(env, simpy.Environment)
        self.__env = env
        self.__queue = queue
        self.__channel = None

    def get_channel(self):
        return self.__channel

    def set_channel(self, channel):
        assert isinstance(channel, Channel)
        self.__channel = channel
    channel = property(
        get_channel, set_channel, None, 'the associated channel model')

    # TODO: get the serve size according to channel state
    def get_serve_size(self):
        return self.__channel.get_available()

    # TODO: get the service time according to channel model
    # TODO: get error prob according to channel model
    def serve(self, serve_pdu):
        assert isinstance(serve_pdu, Pdu)
        service_time, error = self.__channel.do_serve(serve_pdu)
        serve_pdu.on_serve_begin()
        yield self.__env.process(self.do_serve(service_time))

        dice = random.random()
        if error:
            serve_pdu.on_dropped()
        else:
            serve_pdu.on_serve_end()
        self.__queue.action.interrupt()

    def do_serve(self, duration):
        yield(self.__env.timeout(duration))
