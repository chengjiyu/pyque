import simpy
import numpy as np


class BaseSourceModel():
    '''The Base class for source model,
    ------------methods---------------
    get_pkt_num() : return a int that represents the amount of packets that the source generated
    get_interval() : return a float that represents the interval for the next message
    on_served() : decorator for feedback on the successful delivering
    on_dropped() : decorator for feedback on the fail delivering
    '''
    def __init__(self):
        pass

    def get_pkt_num(self):
        return 1

    def get_interval(self):
        return 1.

    def on_served(self):
        print('The source received feedback for successful delivering')

    def on_droped(self):
        print('The source received feedback for transmission failure')

class MMPPModel(BaseSourceModel):
    '''The Markov Modulated Poisson Process Source Model'''

    def __init__(self, Q, Lambda):
        assert(len(np.shape(Q)) is 2)
        assert(len(np.shape(Lambda)) is 1)
        assert(np.shape(Q)[0] == np.shape(Q)[1])
        assert(np.shape(Q)[0] == len(Lambda))
        self.__Q = np.atleast_2d(Q)
        self.__state_transition = np.cumsum(self.__Q, axis = 1)
        self.__Lambda = np.atleast_1d(Lambda)
        self.__states = np.array([i for i in range(Lambda.shape[0])])
        self.__cur_state = np.random.randint(0, self.__states[-1])      # self.__states=[0,1,2,3]; self.__cur_state=[0,1,2]

    def get_interval(self):
        state = self.__states[self.__cur_state]
        rate = self.__Lambda[state]
        dice = np.random.random()
        self.__cur_state = np.argwhere(self.__state_transition[self.__cur_state] > dice)[0][0]
        # Find the indices of array elements that are non-zero, grouped by element.
        # return position of the first meet specified condition
        return np.random.exponential(1./ rate) / rate

    @property
    def cur_state(self):
        return self.__cur_state

    @property
    def Q(self):
        return self.__Q


class TcpSourceModel(BaseSourceModel):
    '''The emulated TCP source model'''

    def __init__(self, rtt):
        self.__rtt = rtt
        self.segsize = 1440
        self.__cwnd = 1
        self.__ssth = 0xffff
        self.__acked = 0
        self.__cum = 0

    @property
    def cwnd(self):
        return self.__cwnd

    @property
    def ssth(self):
        return self.__ssth

    def get_interval(self):
        rate = self.segsize * self.__cwnd / self.__rtt
        return np.random.exponential(1. / rate) / rate

    def on_served(self):
        if self.__cwnd < self.__ssth:
            self.__cwnd += 1
            print("Acked in Slow Start Phase")
            print("cwnd is {0}, ssth is {1}".format(self.__cwnd, self.__ssth))
        else:
            print("Acked in Congestion avoidance")
            self.__cum += 1
            if self.__cum == self.__cwnd:
                self.__cwnd += 1
                self.__cum = 0
            print("cwnd is {0}, ssth is {1}".format(self.__cwnd, self.__ssth))

