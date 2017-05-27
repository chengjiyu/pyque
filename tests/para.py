import numpy as np
import matplotlib.pyplot as plt

l_1 = 1.0722
l_2 = 0.48976
s_1 = 8.4733*10**(-4)
s_2 = 5.0201*10**(-6)
u = 2.181162

pi = np.mat(np.array([0.9941103, 0.0058897]))
e = np.mat(np.ones((2,1)))
I = np.mat(np.eye(2))
L = np.mat(np.array([[1.0722, 0],[0, 0.48976]]))
Q = np.mat(np.array([[-s_1, s_1], [s_2, -s_2]]))
pb = (L - Q).I * L * (u*I-Q).I
# pb = pi * ((L - Q).I * L * (u*I-Q).I) * e
print(pb)
print(1-pb.sum())

R0 = 2*(l_1*s_2*(s_1+s_2+l_2)**2+l_2*s_1*(s_1+s_2+l_1)**2+(l_1-l_2)**2*s_1*s_2)/((l_1*s_2+l_2*s_1)*(l_1*s_2+l_2*s_1+l_1*l_2)**2)
c = s_1*s_2*(l_1-l_2)**2*l_1*l_2/((l_1*s_2+l_2*s_1)**2*(l_1*s_2+l_2*s_1+l_1*l_2)**2)
k = l_1*l_2/(l_1*s_2+l_2*s_1+l_1*l_2)
print(R0, c, k)
# f = s_2*l_1+s_1*l_2
# F = np.mat(np.array([s_2*l_1/f, s_1*l_2/f]))
l = np.mat(np.array([l_1, l_2]))
R00 = l*((Q-L).I)**4*L*3/8
print(R00)

T = l*0.25/2*(R0+c/(1-0.5*k)) + 0.25/(2*l*(1-0.5))
print(T)

l_avg = pi * T.T
print(l_avg)
