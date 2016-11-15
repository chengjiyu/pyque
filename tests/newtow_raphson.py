import numpy as np
l_1 = 1.0722
l_2 = 0.48976
s_1 = 8.4733*10**(-4)
s_2 = 5.0201*10**(-6)
mu = 2.5
Q = np.array([[-1*s_1,s_1], [s_2,-1*s_2]])
L = np.array([[l_1,0], [0,l_2]])
M = np.array([[mu,0], [0,mu]])

# 求矩阵行列式 np.linalg.det

def NRSquareroot(x,ellipson):
    assert(ellipson > 0)
    ellipson = ellipson#ensure the epplison is appropriate
    J = 1
    ctr = 0
    while (abs(x-J)>ellipson and ctr<100):
        J = x
        s = s_1+s_2+s_1*x+(l_1*s_2*x)/(s_1+(s_1-s_2)*x)
        x = 1-(s_2*x)/(s_1+(s_1-s_2)*x)-mu/(mu+s)
        print(x)
        ctr += 1
    print('ans',x)
    G_1 = x
    G_2 = (s_2*x)/(s_1+(s_1-s_2)*x)
    G = np.array([[1-G_1,G_1], [G_2,1-G_2]])
    g = np.array([[G_2/(G_1+G_2),G_1/(G_1+G_2)]])
    print(G, g)
NRSquareroot(0,0.000001)