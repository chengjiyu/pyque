from numpy import random
from unit import Pdu

class Channel(object):

    def __init__(self):
        pass


class ErrorChannel(Channel):

    def __init__(self):
        super(ErrorChannel, self).__init__()
        pass

    def get_available(self):
        return random.randint(0,1400,)

    def do_serve(self, serve_pdu):
        assert isinstance(serve_pdu, Pdu)
        err_p = random.random()
        dice = random.random()
        if dice < err_p:
            error = True
        else:
            error = False
        duration = random.geometric(0.1)
        return duration, error