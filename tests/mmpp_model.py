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
Tp = (lambda_1*sigma_2+lambda_2*sigma_1)/(sigma_1+sigma_2) # lambda 的均值
print('lambda均值:',Tp)
for t in range(1, 10000):
    c = (sigma_1+sigma_2)**3*(lambda_1*sigma_2+lambda_2*sigma_1)*t
    d = 1 - np.e ** ((-sigma_1 + sigma_2) * t)
    K = J - a/c*d
    k.append(K)
# the vartual waiting time distribution
u = 2.181162
g_1 =0.00588774 # (sigma_2*lambda_2)/(lambda_1*sigma_1+lambda_2*sigma_2)
g_2 = 0.99411226 # (sigma_1*lambda_1)/(lambda_1*sigma_1+lambda_2*sigma_2)

print(sigma_1+sigma_2)
print(g_1*lambda_2+g_2*lambda_1)
print(sigma_1*sigma_2)
print("g 的稳态分布：%f %f" %(g_1, g_2))
w = []      # vartual waiting time
w_aa = []   # the waiting time at customer arrival instants
for s in range(1, 41):
    h = -s/(s+u)
    w_1 = 0.51*s*(s-sigma_1-sigma_2)+h*(g_1*lambda_2+g_2*lambda_1)
    # w_2 = (s+lambda_1*h-sigma_1)*(s+lambda_2*h-sigma_2)-sigma_1*sigma_2
    w_2 = s*s+(h*(lambda_1+lambda_2)-(sigma_1-sigma_2))*s+h*(h*lambda_1*lambda_2-sigma_1*lambda_2-sigma_2*lambda_1)
    w_v = w_1/w_2
    w_a = (s+u)/Tp * (w_v-0.51)
    w.append(w_v)
    w_aa.append(w_a)

# the arrival interval
l = []
interval = []
for s in range(0,30):
    l_1 = (0.209015861*s + 0.220922157)/(0.4203708920*(s**2+1.562812350*s+0.525541043))
    l_2 = 0.49*np.e**(-0.48976*s)+0.01*np.e**(-1.0722*s)
    l.append(l_1)
    interval.append(l_2)

T = [i for i in range(1, 10000)]
# --------------------------------------------I_t 的变化图------------------------------------------
fig= plt.figure(1)
plt.plot(T,k)
plt.title('I_t')

v = []
for t in range(1,10000):
    s = Tp*t
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

s = [i for i in range(1,41)]
# --------------------------------------------the vartual waiting time distribution-----------------
fig= plt.figure(4)
plt.plot(s,w,'b',label = "the vartual waiting time")    # 有问题？？？？？？？？？？？？？？？？？？？？？？？？？？
plt.plot(s,w_aa,'r', label = "the waiting time arrival instants")
plt.title('The waiting time distribution')
plt.xlabel('time')# make axis labels
plt.ylabel('probability')
plt.legend()
# --------------------------------------------the arrival interval-----------------------------------
inter = [i for i in range(0,30)]
fig= plt.figure(5)
plt.plot(inter,l,'b',label = "the LST of arrival interval")
plt.plot(inter,interval,'r', label = "the arrival interval")
plt.title('The arrival interval')
plt.legend()

# --------------------------------------------u = 2.181162的指数分布 服务时间------------------------------------------
fig= plt.figure(8)
u = 2.181162
x = np.arange(0, 10, 1)
y = (1/u)*np.exp(-x/u)
plt.plot(x,y)
plt.title('Exponential: 1/$\mu$=%f' % u)

# --------------------------------------------packet loss-------------------------------------------
cwnd = []
with open ('cwnd.txt', 'r') as d:
    for line in d:
        cwnd.append(line)

a = []
P = 0.001
q = []      # packet loss
for i in cwnd:
    i = int(i)/1400
    a.append(i)
for i in sorted(a):
    if i <= 3:
        q_i = 1.
    else:
        q_i = ((1-(1-P)**3)*(1+(1-P)**3-(1-P)**i)) / (1-(1-P)**i)
    q.append(q_i)
print("丢包率：{0}".format(q))

fig= plt.figure(6)
plt.plot(q)
plt.title('Packet loss')
plt.xlabel('time')# make axis labels
plt.ylabel('packet loss')
plt.legend()

# --------------------------------------------throughput---------------------------------------------
T = []
G = []

for i in q:
    if i == 1:
        Gp = 0
    else:
        Gp = (1-P-i)*Tp
    G.append(Gp)
print("goodput：{0}".format(G))
T = [Tp]*len(G)
fig= plt.figure(7)
plt.plot(G, 'b', label = "Goodput")
plt.plot(T, 'r', label = "Throughput")
plt.title('Goodput & Throughput')
plt.xlabel('time')# make axis labels
plt.ylabel('throughput')
plt.legend()

# show the figure
plt.show()
plt.close('all')
