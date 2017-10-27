import simpy
from numpy import random

from .unit import Packet
from .unit import Pdu
from .channel import ErrorChannel, Channel
from .log import Logger
from .gol import gol

class BaseServer():
    '''the base server model, associated with a transmission channel,
    do the serve process according to the channel capacity
    '''
    def __init__(self, env, queue):
        super(BaseServer, self).__init__()
        assert isinstance(env, simpy.Environment)
        self.__env = env
        self.__log = Logger('server', 'data.txt')
        self.__gol = gol()
        self.__queue = queue
        self.__channel = None
        self.action = self.__env.process(self.run())

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
        print("server start to serve pdu at : {0:f}".format(self.__env.now))        # {0:d} --> {0:f} by chengjiyu on 2016/9/23
        yield self.__env.process(self.do_serve(service_time))

        print("server finish serving pdu at : {0:f}".format(self.__env.now))        # {0:d} --> {0:f} by chengjiyu on 2016/9/23
        self.__log.logger.info("server finish serving pdu at : {0:f}".format(self.__env.now))
        wt = self.__gol.get_value("wait_time")
        rtt = service_time + wt
        if rtt < 5:                  # it need to be further modified, 应该计算从到达到结束服务的时间，service_time 是开始服务到结束服务时间
            if error:
                serve_pdu.on_dropped()
            else:
                serve_pdu.on_serve_end()
        else:
            serve_pdu.on_timeout()

    def do_serve(self, duration):
        yield(self.__env.timeout(duration))

    def run(self):
        while True:
            serve_pdu = self.__queue.get_pdu(self.get_serve_size())
            print("serve pdu")
            if serve_pdu is None:
                yield self.__env.timeout(1)
            else:
                yield self.__env.process(self.serve(serve_pdu))     # add yield self.__env.process() by chengjiyu on 2016/9/19