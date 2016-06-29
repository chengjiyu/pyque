from .unit import Packet

class TcpReno():
    __doc__ = """
    The TcpReno class emulates the cwnd evolution.
    Based on the TCP NewReno cwnd evolution.
    On Slow Start phase, the cwnd increase by 1 for every ack
    On Congesion Avoidance phase, the cwnd is increas by 1/cwnd for every ack
    On duplicate acks, the cwnd decrease to cwnd/2
    On timeout, the cwnd is set to 0
    Once recover from timeout, the cwnd is set to init_cwnd
    """

    def __init__(self):
        self.__init_cwnd = 1
        self.__init_ssth = 65535
        self.__cwnd = 1
        self.__ssth = 65535
        self.__accumulator = 0

    def on_ack(self, func):
        def wrapper(self):
            if self.__cwnd <= self.__ssth:
                self.__cwnd += 1
            else:
                self.__accumulator += 1
                if self.__accumulator == self.__cwnd:
                    self.__cwnd += 1
                    self.__accumulator = 0
            func()
        return wrapper

    def on_

