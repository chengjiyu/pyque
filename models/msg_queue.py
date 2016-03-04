from unit import Message, Pdu
from server import BaseServer, Server
import simpy
from collections import deque


class MsgQueue(object):
    '''
    The queue that waits for serve
    FCFS(FIFO)
    '''
    def __init__(self, env, server = None):
        self.queue = deque()
        assert isinstance(env, simpy.Environment)
        self.__env = env

        if server:
            self.__server = server
        else:
            self.__server = BaseServer(self.__env, self)
        self.action = self.__env.process(self.run())

    def set_server(self, server):
        assert isinstance(server, Server)
        self.__server = server

    def get_server(self):
        return self.__server
    server = property(get_server, set_server, None, 'Server for this queue')


    def on_arrival(self,msg):
        isinstance(msg, Message)
        self.queue.extend([packet.at_arrive() for packet in msg])

    def run(self):
        while True:
            try:
                continue
            except simpy.Interrupt:
                to_serve = self.__server.get_serve_size()
                serve_pdu = Pdu(to_serve)
                while True:
                    if self.queue.__len__() > 0:
                        first = self.queue.popleft()
                        if first.size > to_serve:
                            serve_pdu.append(first.get(to_serve))
                            self.queue.appendleft(first)
                            break
                        elif first.size == to_serve:
                            serve_pdu.append(first.get(to_serve))
                            break
                        else:
                            to_serve -= first.size
                            serve_pdu.append(first.get(first.size))
                    else:
                        break
                yield self.__env.process(self.__server.serve(serve_pdu))