import numpy as np
import matplotlib.pyplot as plt

l_1 = 1.0722
l_2 = 0.48976
s_1 = 8.4733*10**(-4)
s_2 = 5.0201*10**(-6)
u = 2.181162

pi = np.mat(np.array([ 0.0058897, 0.9941103]))
e = np.mat(np.ones((2,1)))
In = np.mat(np.eye(2))
L = np.mat(np.array([[1.0722, 0],[0, 0.48976]]))
Q = np.mat(np.array([[-s_1, s_1], [s_2, -s_2]]))
# pb = (L - Q).I * L * (u*In-Q).I
# pb = pi * ((L - Q).I * L * (u*I-Q).I) * e
# print(pb)
# print(1-pb.sum())

# R0 = 2*(l_1*s_2*(s_1+s_2+l_2)**2+l_2*s_1*(s_1+s_2+l_1)**2+(l_1-l_2)**2*s_1*s_2)/((l_1*s_2+l_2*s_1)*(l_1*s_2+l_2*s_1+l_1*l_2)**2)
# c = s_1*s_2*(l_1-l_2)**2*l_1*l_2/((l_1*s_2+l_2*s_1)**2*(l_1*s_2+l_2*s_1+l_1*l_2)**2)
# k = l_1*l_2/(l_1*s_2+l_2*s_1+l_1*l_2)
# print(R0, c, k)
fai = pi*L/(pi*L*e)
l = np.mat(np.array([1.0722,0.48976]))
v = 0.17449907154352892
d = 0.5
b=v*fai*((Q-L).I**2*L*(1-d)*(In-(1-d)*(Q-L).I*L).I*(Q-L).I**2*L-(Q-L).I**3*L)*e
print(b*l)
# T = v*(l*0.5*(R0+c/(1-(1-d)*k)) + 0.5/d*l.I.T)
# print(T)
p_random = 0.113
p_timeout = 0.185
p = 0.702
E_l = 0.113*np.mat(np.array([5.89961103, 2.69482699]))+\
0.702*np.mat(np.array([6.63706241, 3.03168036]))+\
0.185*np.mat(np.array([4.4247105, 2.02112126]))
print(E_l)
print(1.0722/6.1444453,0.48976/2.8066625)

import itertools
a = list(itertools.combinations(range(1, 5), 2))
res = []
for i in a:
    res.append(i)
print(a)