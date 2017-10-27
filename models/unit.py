import simpy
from collections import deque

from . import source_model
from .log import Logger
from .gol import gol

# ###############################  Source Units ###############################


class Message(object):
    __doc__ = """
    Unit for source generator, it may compound with several packets
    by default, 1 Message contains 1 packets
    the number of packets obey a discrete distribution
    Geometric, Binomial, etc.
    """

    msg_num = 0

    def __init__(self, env, s_m,  number):
        Message.msg_num += 1
        self.__index = Message.msg_num
        assert(isinstance(env, simpy.Environment))
        self.__env = env
        # self.__log = Logger('message', 'data.txt')
        assert(isinstance(s_m, source_model.BaseSourceModel))
        self.__source_model = s_m
        assert(isinstance(number, int))
        self.packets_num = number
        #TODO the size of packet should be configurable
        self.packets = [Packet(self.__env, self.__source_model, 1400) for i in range(self.packets_num)]

        self.create_time, self.create = None, False
        self.arrive_time, self.arrive = None, False
        self.dropped_time, self.dropped = None, False
        self.served_time, self.served = None, False
        self.serve_on_time, self.serve_on = None, False

        print("New Message generated, ID : {0:d}".format(self.__index))

    def __getitem__(self, item):
        assert isinstance(item, int)
        return self.packets[item]

    def get_index(self):
        return self.__index
    index = property(get_index)


class Packet(object):
    __doc__ = """
    Basic source unit, consist in message
    """

    pkt_num = 0

    def __init__(self, env, sm, size):
        assert isinstance(env, simpy.Environment)
        assert isinstance(sm, source_model.BaseSourceModel)
        self.__env = env
        self.__log = Logger('packet', 'data.txt')
        self.__gol = gol()
        self.__wt = "wait_time"
        self.__source_model = sm
        Packet.pkt_num += 1
        self.__index = Packet.pkt_num
        self.size = size

        self.create_time = self.__env.now
        self.arrive_time, self.arrive = None, False
        self.serve_on_time, self.serve_on = None, False
        self.served_time, self.served = None, False
        self.dropped_time, self.dropped = None, False

        self.segmented = False

        print("new packet generated with id : {0:d}".format(self.__index))

    def __str__(self):
        msg = 'Packet\tid=%d\t create = %f\t size = %d' \
              % (self.__index, self.create_time, self.size)
        if self.arrive:
            msg += '\t arrive = %f' % self.arrive_time
        if self.serve_on:
            msg += '\t serve on = %f' % self.serve_on_time
        if self.dropped:
            msg += '\t dropped = %s' % str(self.dropped_time)        # add %f by chengjiyu on 2016/9/19
        if self.served and self.serve_on:
            print(self.served_time)
            print(self.serve_on_time)
            print(self.arrive_time)
            msg += '\t served = {0:f} \t served_finish = {1:f} \t service_time = {2:f}' \
                .format(self.served_time - self.serve_on_time, self.served_time, self.served_time - self.arrive_time)
                # self.serve_on_time --> self.arrive_time changed by chengjiyu on 2016/10/24    # add 'self.served_time - self.serve_on_time' by chengjiyu on 2016/12/5
            self.__gol.set_value(self.__wt, self.served_time - self.arrive_time)  # 对等待时间赋值
        return msg

    def at_arrive(self):
        self.arrive = True
        self.arrive_time = self.__env.now
        print("arrive at queue %s" % self)
        return self

    def at_serve_on(self):
        self.serve_on_time = self.__env.now
        self.serve_on = True
        print("start serve %s" % self)
        return self

    def at_served(self):
        self.__source_model.on_served()
        self.served_time = self.__env.now
        self.served = True
        print("finish serve %s" % self)
        self.__log.logger.info("finish serve %s" % self)
        return self

    def at_dropped(self):
        self.__source_model.on_droped()
        self.dropped_time = self.__env.now
        self.dropped = True
        print("packet dropping " + str(self.__str__()))
        self.__log.logger.info("packet dropping " + str(self.__str__()))        # add str() by chengjiyu on 2016/9/19
        return self

    # add timeout by chengjiyu on 2016/10/8
    def at_timeout(self):
        self.dropped = True
        self.__source_model.on_timeout()

    def get(self, length):
        assert length <= self.size
        seg = Segment(self.__env, length)
        seg.packet = self
        self.size -= length
        seg.end_of_packet = (self.size == 0)
        if self.segmented:
            seg.middle_of_packet = not seg.end_of_packet
            seg.begin_of_packet = False
        else:
            seg.begin_of_packet = True
            seg.middle_of_packet = True
            self.segmented = True
        return seg


# ############################### Server Units ############################# #


class Segment(object):
    __doc__ = '''
    Size of packet may not match size of server PDU
    packet must be segmented into segments for transmission
    or packets should be combined into segments
    if the segments is dropped, the associate packet and peer segments are dropped
    all the segments in a packet is served result in a successful packet delivery
    '''

    def __init__(self, env, length):
        assert isinstance(env, simpy.Environment)
        self.__env = env
        self.__pkt = None
        self.length =length
        #__tags[0] : is the begin of a packet
        #__tags[1] : is middle of a packet
        #__tags[2] : is end of a packet

        self.__tags = [True, False, True]

    def get_begin(self):
        return self.__tags[0]

    def set_begin(self, value):
        assert type(value) is bool
        self.__tags[0] = value
    begin_of_packet = property(get_begin, set_begin, None, "whether this segment is begin of a packet")

    def get_mid(self):
        return self.__tags[1]

    def set_mid(self, value):
        assert type(value) is bool
        self.__tags[1] = value
    middle_of_packet = property(get_mid, set_mid, None, "whether this segment is middle of a packet")

    def get_end(self):
        return self.__tags[2]

    def set_end(self, value):
        assert type(value) is bool
        self.__tags[2] = value
    end_of_packet = property(get_end, set_end, None, "whether this segment is end of a packet")

    def set_packet(self, packet):
        self.__pkt = packet

    def get_packet(self):
        return self.__pkt
    packet = property(get_packet, set_packet, None, "the packet that this segment belongs to")      # ???? problem： 2016/11/16

    @property
    def is_full_packet(self):
        return self.__tags[0] and self.__tags[2]


class Pdu(object):
    __doc__ = '''
    Basic protocol data unit
    it contains at least 1 segment
    once it is dropped, all the segment in it is dropped
    and it is served, all the segment in it is served
    '''

    def __init__(self, env, size):
        assert isinstance(env, simpy.Environment)
        self.__env = env
        self.total_size = size
        self.segments = deque()
        self.filled = 0
        self.seg_num = 0
        self.remain = self.total_size

    def __getitem__(self, item):
        assert isinstance(item, int)
        return self.segments[item]

    def __setitem__(self, key, value):
        assert isinstance(key, int)
        assert isinstance(value,Segment)
        self.segments[key] = value

    def append(self, seg):
        assert isinstance(seg, Segment)
        self.segments.append(seg)
        self.filled += seg.length
        self.remain -= seg.length
        self.seg_num += 1

    def on_serve_begin(self):
        for seg in self:
            if seg.begin_of_packet:
                seg.packet.at_serve_on()

    def on_serve_end(self):
        for seg in self:
            if seg.end_of_packet:
                seg.packet.at_served()

    def on_dropped(self):
        for seg in self:
            seg.packet.at_dropped()

    # add time out by chengjiyu on 2016/10/8
    def on_timeout(self):
        for seg in self:
            seg.packet.at_timeout()
