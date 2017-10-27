from numpy import random
from .unit import Pdu
from scipy import stats

class Channel(object):

    def __init__(self):
        pass

class ErrorChannel(Channel):

    def __init__(self):
        super(ErrorChannel, self).__init__()
        pass

    def get_available(self):
        return random.randint(0, 1400,)

    def do_serve(self, serve_pdu):
        assert isinstance(serve_pdu, Pdu)
        err_p = random.random()                  # modify packet error rate by chengjiyu on 2016/9/28
        dice = random.uniform()                      # random.rand() --> 0.1
        if dice < 0.002:
            error = True
        else:
            error = False
        duration = stats.expon.rvs(scale=0.458471218552, size=1)[0]
        # duration = random.exponential(0.458471218552)        # random.geometric(0.1) --> random.exponential(1.) serve duration is long by chengjiyu on 2016/9/22
        return duration, error

class FixedChannel(Channel):

    def __init__(self, capacity, delay, error_rate):
        super().__init__()
        self.__cap = capacity
        self.__delay = delay
        self.__err_rate = error_rate

    @property
    def capacity(self):
        return self.__cap
    @capacity.setter
    def capacity(self, val):
        self.__cap = val

    @property
    def error_rate(self):
        return self.__err_rate
    @error_rate.setter
    def error_rate(self, val):
        assert(val > 0. and val < 1.)
        self.__err_rate = val

    @property
    def delay(self):
        return self.__delay
    @delay.setter
    def delay(self, val):
        self.__delay = val

    def get_available(self):
        return self.capacity

    def do_serve(self, serve_pdu):
        assert isinstance(serve_pdu, Pdu)
        dice = random.random()
        if dice < self.__err_rate:
            is_error = True
        else:
            is_error = False
        return self.delay, is_error