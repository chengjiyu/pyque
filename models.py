import simpy
from numpy import random
from collections import *


class packet(object):
    '''
    Packet arrive at the queue, it has a fixed and settable length,
    Usage
    '''
    pkt_num = 0

    def __init__(self, env, length=1400):
        packet.pkt_num += 1
        self.env = env
        self.index = packet.pkt_num
        self.length = length
        self.birth_time = self.env.now

        self.arrive_time = None
        self.arrive = False

        self.drop_time = None
        self.dropped = False

        self.served_time = None
        self.served = False

        self.serve_on_time = None
        self.serve_on = False

        self.segmented = False

    def __str__(self):
        msg = 'Packet\tid=%d\t create = %f\t length = %d' % (self.index, self.birth_time, self.length)
        if self.arrive:
            msg += '\t arrive = %f' % self.arrive_time
        if self.dropped:
            msg += '\t dropped =' % self.drop_time
        if self.served:
            msg += '\t served = {0:f} \t service_time = {1:f}' \
                .format(self.served_time, self.served_time - self.serve_on_time)

    def at_arrive(self):
        self.arrive = True
        self.arrive_time = self.env.now
        return self

    def at_serve_start(self):
        self.serve_on_time = self.env.now
        self.serve_on = True

    def at_served(self):
        self.served_time = self.env.now
        self.served = True
        self.serve_on = False

    def at_drop(self):
        self.drop_time = self.env.now
        self.dropped = True

    def get(self, size):
        assert (size <= self.length)
        seg = segment(size)
        seg.set_attribution(self)
        self.length -= size
        seg.end_of_packet = (self.length == 0)
        if self.segmented:
            seg.middle_of_packet = not seg.end_of_packet
            seg.begin_of_packet = False
        else:
            seg.begin_of_packet = True
            seg.middle_of_packet = False
            self.segmented = True
        return seg


class segment(object):
    def __init__(self, size):
        self.size = size
        self.begin_of_packet = True
        self.end_of_packet = True
        self.middle_of_packet = False

    def is_full_packet(self):
        return self.begin_of_packet and self.end_of_packet

    def set_attribution(self, packet):
        self.attribution = packet


class massage(object):
    msg_num = 0

    def __init__(self, env, pkt_num):
        massage.msg_num += 1
        self.index = massage.msg_num
        self.env = env
        self.packets_num = pkt_num
        self.packets = [packet(self.env) for i in range(pkt_num)]
        self.arrive = False
        self.dropped = False
        self.served = False

    def __getitem__(self, item):
        return self.packets[item]

    def __setitem__(self, key, value):
        self.packets[key] = value


class source(object):
    def __init__(self, env, lamb=1, geo_para=0.3):
        self.env = env
        self.lamb = lamb
        self.geo_para = geo_para
        self.action = self.env.process(self.run())
        self.__dst_server = None

    def set_dst(self, dst):
        self.__dst_server = dst

    def get_dst(self):
        return self.__dst_server

    dst_server = property(get_dst, set_dst)

    def run(self):
        while True:
            interval = random.exponential(self.lamb)
            pkt_num = random.geometric(self.geo_para)
            msg = massage(self.env, pkt_num)
            self.sendto(self.dst_server, msg)
            yield self.env.timeout(interval)

    def sendto(self, queue, massage):
        queue.on_arrive(massage)


class pdu(object):
    def __init__(self, size):
        self.total_bytes = size
        self.segments = deque()
        self.bytes = 0
        self.seg_num = 0
        self.remain_bytes = self.total_bytes

    def __getitem__(self, item):
        return self.segments[item]

    def __setitem__(self, key, value):
        self.segments[key] = value

    def append(self, segment):
        self.segments.append(segment)
        self.bytes += segment.size
        self.remain_bytes -= segment.size
        self.seg_num += 1

    def on_serve_start(self):
        for seg in self.segments:
            if seg.begin_of_packet:
                seg.attribution.at_serve_start()

    def on_served(self):
        for seg in self.segments:
            if seg.end_of_packet:
                seg.attribution.at_served()

    def on_dropped(self):
        for seg in self.segments:
            seg.attribution.at_drop()


class system_queue(object):
    '''
    the queueing system with multiple servers
    '''

    def __init__(self, env, server=None):
        self.queue = deque()
        self.env = env
        if server:
            self.__server = server
        else:
            self.__server = base_server(self)
        self.action = self.env.process(self.run())

    def set_server(self, server):
        self.__server = server

    def get_server(self):
        return self.__server

    server = property(get_server, set_server)

    def on_arrive(self, massage):
        self.queue.extend([packet.at_arrive() for packet in massage])

    def run(self):
        while True:
            try:
                continue
            except simpy.Interrupt:
                to_serve = self.__server.capacity()
                serve_pdu = pdu(to_serve)
                while True:
                    if self.queue.__len__() > 0:
                        head = self.queue.popleft()
                        if head.length > to_serve:
                            serve_pdu.append(head.get(to_serve))
                            self.queue.appendleft(head)
                            break
                        elif head.length == to_serve:
                            serve_pdu.append(head.get(to_serve))
                            break
                        else:
                            to_serve -= head.length
                            serve_pdu.append(head.get(head.length))
                    else:
                        break
                yield self.env.process(self.__server.serve(serve_pdu))


class base_server(object):
    def __init__(self, served_queue, serve_rate=1):
        self.rate = serve_rate
        self.env = served_queue.env
        self.served_queue = served_queue

    def serve(self, pdu):
        duration = random.exponential(self.rate)
        pdu.on_serve_start()
        yield self.env.process(self.do_serve(duration))
        pdu.on_served()
        self.served_queue.action.interrupt()

    def capacity(self):
        return 1400

    def do_serve(self, duration):
        yield (self.env.timeout(duration))
