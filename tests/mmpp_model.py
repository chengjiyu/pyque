import numpy as np
import matplotlib.pyplot as plt

lambda_1 = 1.0722
lambda_2 = 0.48976
sigma_1 = 8.4733*10**(-4)
sigma_2 = 5.0201*10**(-6)
a = 2*(lambda_1-lambda_2)**2*sigma_1*sigma_2
b = (sigma_1+sigma_2)**2*(lambda_1*sigma_2+lambda_2*sigma_1)
# c = (sigma_1+sigma_2)**3*(lambda_1*sigma_2+lambda_2*sigma_1)*t
# d = 1-np.e**((-sigma_1+sigma_2)*t)
I = 1.+(2*(lambda_1-lambda_2)**2*sigma_1*sigma_2)/((sigma_1+sigma_2)**2*(lambda_1*sigma_2+lambda_2*sigma_1))
J = 1. + a/b
k = []      # I_t
for t in range(1, 10000):
    c = (sigma_1+sigma_2)**3*(lambda_1*sigma_2+lambda_2*sigma_1)*t
    d = 1 - np.e ** ((-sigma_1 + sigma_2) * t)
    K = J - a/c*d
    k.append(K)
# the vartual waiting time distribution
u = 2.5
g_1 =0.00588774 # (sigma_2*lambda_2)/(lambda_1*sigma_1+lambda_2*sigma_2)
g_2 = 0.99411226 # (sigma_1*lambda_1)/(lambda_1*sigma_1+lambda_2*sigma_2)
print("g 的稳态分布：%f %f" %(g_1, g_2))
w = []      # vartual waiting time
for s in range(1, 100):
    h = -s/(s+u)
    w_1 = 0.51*s*(s-sigma_1-sigma_2)+h*(g_1*lambda_2+g_2*lambda_1)
    w_2 = (s+lambda_1*h-sigma_1)*(s+lambda_2*h-sigma_2)-sigma_1*sigma_2
    w_v = w_1/w_2
    w.append(w_v)

# the arrival interval
l = []
for s in range(1,100):
    l_1 = (0.209015861*s + 0.220922157)/(0.4203708920*(s**2+1.562812350*s+0.525541043))
    l.append(l_1)

T = [i for i in range(1, 10000)]
# --------------------------------------------I_t 的变化图------------------------------------------
fig= plt.figure(1)
plt.plot(T,k)
plt.title('I_t')

v = []
for t in range(1,10000):
    s = (lambda_1*sigma_2+lambda_2*sigma_1)/(sigma_1+sigma_2)*t
    v.append(s)
# --------------------------------------------N_t 的变化图------------------------------------------
fig= plt.figure(2)
plt.plot(T,v)
plt.title('N_t')

def p(x, y):
    return x*y
s = list(map(p,k,v))
# print(s)

# --------------------------------------------N_t * I_t--------------------------------------------
fig= plt.figure(3)
plt.plot(T,s)
plt.title('N_t * I_t')

s = [i for i in range(1,100)]
# --------------------------------------------the vartual waiting time distribution-----------------
fig= plt.figure(4)
plt.plot(s,w)
plt.title('The vartual waiting time distribution')

# --------------------------------------------the arrival interval-----------------------------------
fig= plt.figure(5)
plt.plot(s,l)
plt.title('The arrival interval')

# --------------------------------------------packet loss-------------------------------------------
P = 0.001
q = []      # packet loss
for i in range(1,47):
    if i <= 3:
        q_i = 1.
    else:
        q_i = ((1-(1-P)**3)*(1+(1-P)**3-(1-P)**i)) / (1-(1-P)**i)
    q.append(q_i)
print("丢包率：{0}".format(q))
fig= plt.figure(6)
plt.plot(q)
plt.title('Packet loss')

# --------------------------------------------throughput---------------------------------------------
T = []
G = []
Tp = (lambda_1*sigma_2+lambda_2*sigma_1)/(sigma_1+sigma_2)

for i in q:
    if i == 1:
        Gp = 0
    else:
        Gp = (1-P-i)*Tp
    G.append(Gp)
print("goodput：{0}".format(G))
T = [Tp]*len(G)
fig= plt.figure(7)
plt.plot(G, 'b')
plt.plot(T, 'r')
plt.title('Goodput & Throughput')

# show the figure
plt.show()
