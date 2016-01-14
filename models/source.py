import simpy
from numpy import random

discrete_distributions = {
    'binomial' : random.binomial,
    'geometric' : random.geometric,
    'hypergeometric' : random.hypergeometric
}

class source(object):
    '''
    source generator in queueing theory
    generates customers as a given process
    default is Possion process with lambda = 1
    Usage: source(env, gen_rate = 1,compound = False, comp_dist = None, comp_dist_params = None)
    '''
    def __init__(self, env, **kwargs):
        self.__env = env

        if 'gen_rate' in kwargs:
            self.__gen_rate = kwargs['gen_rate']
        else:
            self.__gen_rate = 1.

        if 'compound' in kwargs:
            self.__compound = kwargs['compound']
            if self.__compound:
                assert(kwargs['comp_dist'] is not None)
                assert(kwargs['comp_dist_params'] is not None)
                self.__comp_dist = discrete_distributions[kwargs['comp_dist']]
                self.__comp_dist_params = kwargs['comp_dist_params']
