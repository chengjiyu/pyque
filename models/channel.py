from numpy import random
from .unit import Pdu


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
        err_p = random.random()
        dice = random.random()
        if dice < err_p:
            error = True
        else:
            error = False
        duration = random.geometric(0.2)
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