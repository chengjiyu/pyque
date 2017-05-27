import simpy
from collections import deque

from .unit import Message, Pdu
from .server import BaseServer
from .log import Logger

class MsgQueue(object):
    '''
    The queue that waits for serve
    FCFS(FIFO)
    '''

    def __init__(self, env, server=None):
        self.queue = deque(maxlen = 10)     # 2017/04/19 chengjiyu
        assert isinstance(env, simpy.Environment)
        self.__env = env
        self.__log = Logger('buffer', 'data.txt')

        if server:
            self.__server = server
        else:
            self.__server = BaseServer(self.__env, self)
        # self.action = self.__env.process(self.run())

    def set_server(self, server):
        assert isinstance(server, BaseServer)
        self.__server = server

    def get_server(self):
        return self.__server
    server = property(get_server, set_server, None, 'Server for this queue')

    def on_arrival(self, msg):
        isinstance(msg, Message)
        print("new message with {0:d} packets arrive at MsgQueue".format(msg.packets_num))

        self.queue.extend([packet.at_arrive() for packet in msg])

    def get_pdu(self, pdu_size):
        to_serve = pdu_size
        serve_pdu = Pdu(self.__env, pdu_size)

        while True:
            if self.queue.__len__() > 0:
                print("generate pdu, except {0:d} bytes".format(to_serve))
                first = self.queue.popleft()
                if first.size > pdu_size:
                    serve_pdu.append(first.get(to_serve))
                    self.queue.appendleft(first)
                    break
                elif first.size == to_serve:
                    serve_pdu.append(first.get(to_serve))
                    break
                else:
                    to_serve -= first.size
                    serve_pdu.append(first.get(first.size))
                    print('Buffer size:{0}'.format(self.queue.__len__()))       # add output buffer size by chengjiyu on 2016/10/13
                    self.__log.logger.info('Buffer size:{0}'.format(self.queue.__len__()))
            else:
                break
        if serve_pdu.filled is 0:
            print("empty pdu")
            return None
        else:
            return serve_pdu


    # def run(self):
    #     while True:
    #         try:
    #             yield self.__env.process(self.check_queue())
    #         except simpy.Interrupt:
    #             print("send one pdu to server....")
    #             to_serve = self.__server.get_serve_size()
    #             serve_pdu = Pdu(self.__env, to_serve)
    #             while True:
    #                 if self.queue.__len__() > 0:
    #                     first = self.queue.popleft()
    #                     if first.size > to_serve:
    #                         serve_pdu.append(first.get(to_serve))
    #                         self.queue.appendleft(first)
    #                         break
    #                     elif first.size == to_serve:
    #                         serve_pdu.append(first.get(to_serve))
    #                         break
    #                     else:
    #                         to_serve -= first.size
    #                         serve_pdu.append(first.get(first.size))
    #                 else:
    #                     break
    #             print("Pdu with {0:d} bytes generated".format(serve_pdu.total_size))
    #             yield self.__env.process(self.__server.serve(serve_pdu))
    #         else:
    #             yield self.__env.timeout(10)
    #
    # def check_queue(self):
    #     if len(self.queue) == 0:
    #         yield self.__env.timeout(10)
    #     else:
    #         pass
