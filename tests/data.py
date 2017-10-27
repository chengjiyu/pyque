import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 参数初始化
lambda_1 = 1.14197615
lambda_2 = 0.86498876
sigma_1 = 8.4733*10**(-4)
sigma_2 = 5.0201*10**(-6)
a = 2*(lambda_1-lambda_2)**2*sigma_1*sigma_2
b = (sigma_1+sigma_2)**2*(lambda_1*sigma_2+lambda_2*sigma_1)
# c = (sigma_1+sigma_2)**3*(lambda_1*sigma_2+lambda_2*sigma_1)*t
# d = 1-np.e**((-sigma_1+sigma_2)*t)
I = 1.+(2*(lambda_1-lambda_2)**2*sigma_1*sigma_2)/((sigma_1+sigma_2)**2*(lambda_1*sigma_2+lambda_2*sigma_1))
J = 1. + a/b
Th_It = []      # I_t
for t in range(1, 5000):
    c = (sigma_1+sigma_2)**3*(lambda_1*sigma_2+lambda_2*sigma_1)*t
    d = 1 - np.e ** ((-sigma_1 + sigma_2) * t)
    K = J - a/c*d
    Th_It.append(K)

data = []       # 生成的原始数据
cwnd = []       # 保存过滤得到含有 cwnd 的行
cw = []         # 保存 cwnd 的值
ssth = []       # 保存过滤得到含有 ssth 的行
ss = []         # 保存 ssth 的值
time = []
ti = []
finish = []     # 保存过滤得到完成服务 packet 信息
id = []         # 保存结束服务 packet 的 id
create = []      # 保存 packet 生成的时间 和 到达队列的时间
size = []      # 保存 packet 生成的大小
create_inter = []
service_time = []   # 保存结束服务 packet 的 服务时长
wait_time = []      # 保存从到达到开始服务的等待时间
served_finish = []  # 保存结束服务时的时间
served = []     # 保存服务了多长时间
buffer = []     # 保存过滤得到的 buffer size 行
length = []     # 保存队列长度
success = []    # 成功接收的包
failure = []    # 接收失败的包
ACK   = []      # 确认的包
cwnd_time = []  # 窗口反馈时间

match = ['cwnd']
match1 = ['ssth']
match2 = ['server finish serving pdu at']
match3 = ['finish serve Packet	id=']
match4 = ['Buffer size']
match5 = ['The source received feedback for']
match6 = ['The source received feedback for transmission failure']
match7 = ['ack']

with open ('data.txt', 'r') as d:
    for line in d:
        data.append(line)

# -----------------------------------------------数据读取----------------------------------------------
# 匹配cwnd 和 time 在的行
for i in range(len(data)):
    if match == re.findall(r'cwnd', data[i]):
        cwnd.append(data[i])
    if match1 == re.findall(r'ssth', data[i]):
        ssth.append(data[i])
    if match2 == re.findall(r'server finish serving pdu at', data[i]):
        time.append(data[i])
    if match3 == re.findall(r'finish serve Packet	id=', data[i]):
        finish.append(data[i])
    if match4 == re.findall(r'Buffer size', data[i]):
        buffer.append(data[i])
    if match5 == re.findall(r'The source received feedback for', data[i]):
        if 'success' in data[i]:
            ACK.append(1)       # 1 表示成功接收
        if 'failure' in data[i]:
            ACK.append(0)       # 0 表示没有成功接收
    if match7 == re.findall(r'ack', data[i]):
        success.append(data[i])

# 找到cwnd的值           
for i in range(len(cwnd)):
    m = re.findall(r'\d+\.?\d*',cwnd[i])
    cw.append(m[0])
print('cwnd: {0}'.format(cw))
# cwnd 写入文件
with open ('cwnd.txt', 'w') as c:
    for i in cw:
        c.write(i)
        c.write('\n')

# 找到ssth的值           
for i in range(len(ssth)):
    m = re.findall(r'\d+\.?\d*',ssth[i])
    ss.append(m[1])
print('ssth: {0}'.format(ss))

# 找到time的值
for i in range(len(time)):
    m = re.findall(r'\d+\.?\d*',time[i])
    ti.append(float(m[0]))
print('time: {0}'.format(ti))

# 找到finsih serve Packet id and service_time
for i in range(len(finish)):
    m = re.findall(r'\d+\.?\d*',finish[i])
    id.append(float(m[0]))
    create.append(float(m[1]))
    size.append(float(m[2]))
    create_inter.append(float(m[1]))
    service_time.append(float(m[-1]))
    served_finish.append(float(m[-2]))
    served.append(float(m[-3]))
    wait_time.append(float(m[-1])-float(m[-3]))
print('ID: {0}'.format(id))
print('create: {0}'.format(create))
print('service_time: {0}'.format(service_time))
print('served_time: {0}'.format(served))
print('wait_time: {0}'.format(wait_time))
print(len(ss[:len(served_finish)]),len(cw[:len(served_finish)]),len(served_finish))
# -----------------------------------------------计算丢包率----------------------------------------------
# 计算无线丢包率
ACK = ACK[0:len(service_time)]
pr = []
wuxian = 0
for i, n in enumerate(ACK, 1):
    if n == 0:
        wuxian += 1
    pr.append(wuxian/i)
print(len(pr), '由于随机错误的丢包率：{0}'.format(pr))

# 计算超时的丢包率
t = 5       # 4.75
j = 0
pt = []

for i in range(len(service_time)):
    if service_time[i] > t:
        j += 1
        loss = j/(i+1)
        pt.append(loss)
    else:
        loss = j/(i+1)
        if loss == 0:
            loss += 1
        pt.append(loss)
print(len(pt), '由于超时的丢包率：{0}'.format(pt))

# -----------------------------------------------队长和等待时间----------------------------------------------
# 找到当前队列长度值
for i in range(len(buffer)):
    m = re.findall(r'\d+\.?\d*',buffer[i])
    length.append(int(m[0]))
length = length[0:len(service_time)]
print(len(length),'queue size: {0}'.format(length))
# 计算拥塞丢包率
pb = []
yongse = 0
for i, n in enumerate(length, 1):
    if n == 9:
        yongse += 1
    pb.append(yongse/i)
print(len(pb), '由于拥塞的丢包率：{0}'.format(pb))
P = ACK.count(0)/(len(ACK))
print('无线丢包率 ： %f %%' %(pr[-1]*100))
print('拥塞丢包率 ： %f %%' %(pb[-1]*100))
print('超时丢包率 ： %f %%' %(pt[-1]*100))
# ------------------------------------------------计算仿真吞吐量----------------------------------------------------
# 吞吐量
avg_th = (1-pr[-1]-pb[-1]-pt[-1])*(id[-1])/5000
print('平均吞吐量 ： %f' %avg_th)

path = 'E:\chengjiyu\研究生毕设\结果图\仿真结果tcpmodel\\'
with open (path+'result_'+'str(0.2)'+'.txt', 'w') as r:
    r.write('无线丢包率 ： %f %%' %(pr[-1]*100)+"\n")
    r.write('拥塞丢包率 ： %f %%' %(pb[-1]*100)+"\n")
    r.write('超时丢包率 ： %f %%' %(pt[-1]*100)+"\n")
    r.write('平均吞吐量 ： %f' %avg_th)

th = (id[-1])/5000
print(th)
T = []
for i in range(10,len([i for i in size if i == 0] )):
    Tp = id[i]/create[i]
    T.append(Tp)
print('Throughput: {}'.format(T))
pac_loss = [sum(i) for i in list(zip(pr,pb,pt))]
sim_G = []
for i in pac_loss:
    if i >= 1:
        Gp = 0
    else:
        Gp = (1-i)*th
    sim_G.append(Gp)
print('Goopput: {}'.format(sim_G))
# -----------------------------------------------到达间隔、服务时间、等待时间概率分布----------------------------------------------
# 找到 packet arrival interval
def sub(x,y):
    return x-y
create_2 = create_inter[1:]
interval = sorted(list(map(sub,create_2,create_inter)))
interval_1 = []
interval_2 = []
for i in interval:
    arr = int(i)
    interval_1.append(arr)
arrset = set(interval_1)
for item in arrset:
    a = interval_1.count(item)
    interval_2.append(a/len(interval_1))

print('arrival interval: {0}'.format(interval_2))

# the service_time time 从到达到服务结束的时间
service_time_0 = sorted(service_time)
service_time_1 = []
service_time_2 = []
for i in service_time_0:
    arr = int(i)
    service_time_1.append(arr)
arrset = set(service_time_1)
for item in arrset:
    a = service_time_1.count(item)
    service_time_2.append(a/len(service_time_1))
print('到达到结束服务的时间service interval: {0}'.format(service_time_2))

# the wait_time time 从到达到开始服务的时间
wait_time_0 = sorted(wait_time)
wait_time_1 = []
wait_time_2 = []
for i in wait_time_0:
    arr = int(i*1)
    wait_time_1.append(arr)
arrset = set(wait_time_1)
for item in arrset:
    a = wait_time_1.count(item)
    wait_time_2.append(a/len(wait_time_1))
print('到达到开始服务的时间wait_time_2: {0}'.format(wait_time_2))

# the served time 开始服务到服务结束时间
served_0 = sorted(served)
served_1 = []
served_2 = []
for i in served_0:
    arr = int(i)
    served_1.append(arr)
arrset = list(set(served_1))
for item in arrset:
    a = served_1.count(item)
    served_2.append(a/len(served_1))
print('开始服务到服务结束时间served interval: {0}'.format(served_2))


# 计算I = Var（X）/E(X)
N, N_t, I_t, V = [], [], [], []
for i in id:
    N.append(i)
    l = len(N)
    narray = np.array(N)
    sum_1 = narray.sum()
    N_t.append(sum_1)
    narray_2 = narray*narray
    sum_2 = narray_2.sum()
    mean = sum_1/l
    var = sum_2/l-mean**2
    i_t =var/mean**2
    I_t.append(i_t*30)
print('N_t: {0}'.format(N_t))
print('I_t: {0}'.format(I_t))

# 队长和等待时间
c = []
queue = []      # 保存队列长度
for j in set(length):       # j 是队长列表中的值
    queue.append(j)
    b = [i for i, a in enumerate(length) if a == j]      # b 是不同队长对应的索引值
    c.append(b)
wait = []
for k in range(len(c)):
    s = 0
    for l in range(len(c[k])):
        s += service_time[c[k][l]]     # [c[k][l]] 是队长列表相同队长对应等待时间的索引值
    if len(c[k]) != 0:
        wait.append(s/len(c[k]))

print('队长和平均等待时间queue & wait: {0} {1}'.format(queue,wait))
# -----------------------------------------------画图----------------------------------------------

# declare a figure object to plot
fig = plt.figure(1)     # 拥塞窗口变化
# plot tps
# advance settings
plt.title('cwnd & ssth')
# plt.xticks(range(len(time), time))
plt.plot(served_finish,cw[:len(served_finish)],label = "cwnd",color="blue")
plt.plot(served_finish,ss[:len(served_finish)],label = "ssth",color="red")
plt.xlabel('time')
plt.ylabel('cwnd & ssth')
plt.legend(loc='best')
plt.savefig(path + 'cwnd_ssth'+'.png')

# 队列长度与等待时间关系图
fig= plt.figure(2)
plt.plot(queue,wait,color="blue")
plt.title('queue-wait')
plt.xlabel('queue size')# make axis labels
plt.ylabel('wait time')
plt.savefig(path + 'queue_wait'+'.png')

# N_t 时间 t 内到达的包数
# Time = [i for i in range(1, 5000)]
lambda_avg = 0.4931904061722993
Th_Nt = [i*lambda_avg for i in create] #       N_t 理论值
fig= plt.figure(3)
plt.plot(create, Th_Nt,label = "the theoretical result",color="red")
plt.plot(create, id, label = "the simulation result",color="blue")
plt.title('N_t')
plt.xlabel('time')
plt.ylabel('N_t')
plt.legend(loc='best')
plt.savefig(path + 'N_t'+'.png')

# I_t 图
fig= plt.figure(4)
t_t = [i for i in range(1,len(I_t)+1)]
plt.plot(Th_It, label = "the theoretical result",color="red")
plt.plot(create,I_t,label = "the simulation result",color="blue")
plt.title('I_t')
plt.xlabel('time')
plt.ylabel('I_t')
plt.legend(loc='best')
plt.savefig(path + 'I_t'+'.png')

# the arrival interval
fig= plt.figure(5)
# plt.plot(create[1:],interval_2)
x_1 = np.arange(0, 30, 1)
y_1 = 0.49 * np.e ** (-0.48976 * x_1) + 0.01 * np.e ** (-1.0722 * x_1)
plt.plot(x_1,y_1,label = "the theoretical result",color="red")
# plt.plot(interval_2,label = "the simulation result")
sns.distplot(interval,kde=False,fit=stats.expon,hist=False,label = "the simulation result")
plt.title('The arrival interval distribution')
plt.xlabel('time')# make axis labels
plt.ylabel('probability')
plt.legend(loc='best')
plt.savefig(path + 'The arrival interval distribution'+'.png')

# ---------------------------------------the vartual waiting time-------------------------------------
fig= plt.figure(6)
u = 2.181162
g_1 =0.00588774 # (sigma_2*lambda_2)/(lambda_1*sigma_1+lambda_2*sigma_2)
g_2 = 0.99411226 # (sigma_1*lambda_1)/(lambda_1*sigma_1+lambda_2*sigma_2)

w = []      # vartual waiting time
w_aa = []   # the waiting time at customer arrival instants
for s in range(1, 21):
    h = -s/(s+u)
    w_1 = 0.51*s*((s-sigma_1-sigma_2)+h*(g_1*lambda_2+g_2*lambda_1))
    w_2 = s*s+(h*(lambda_1+lambda_2)-(sigma_1-sigma_2))*s+h*(h*lambda_1*lambda_2-sigma_1*lambda_2-sigma_2*lambda_1)
    w_v = w_1/w_2
    w_a = (s+u)/lambda_avg  * (w_v-0.51)
    w.append(w_v)
    w_aa.append(w_a)
x_2 = np.arange(0, 15, 1)
y_2 = 0.49 * np.e ** (-0.48976 * x_2) + 0.01 * np.e ** (-1.0722 * x_2)
plt.plot(x_2,y_2,label = "the theoretical vartual waiting time",color="red")
# plt.plot(w_aa, label = "the theoretical waiting time arrival instants")
# plt.plot(service_time_2,label = "the vartual waiting time")
sns.distplot(service_time_0,kde=False,fit=stats.expon,hist=False,label = "the simulation vartual waiting time")
# plt.plot(wait_time_2,label = "the waiting time arrival instants")
plt.title('The vartual waiting time distribution')
plt.xlabel('time')# make axis labels
plt.ylabel('probability')
plt.legend(loc='best')
plt.savefig(path + 'The vartual waiting time'+'.png')

# ----------------------------------------The served time distribution---------------------
fig= plt.figure(7)
u = 2.181162
x = np.arange(0, 8, 1)
y = (1/u)*np.exp(-x/u)
plt.plot(x,y,label = "the theoretical result",color="red")
# plt.plot(arrset,served_2,label = "the simulation result")
sns.distplot(served_0,kde=False,fit=stats.expon,hist=False,label = "the simulation result")
plt.title('The served time distribution')
plt.xlabel('time')# make axis labels
plt.ylabel('probability')
plt.legend(loc='best')
plt.savefig(path + 'The served time distribution'+'.png')

# -------------------------------------------------------the throughput--------------------------------------
Th_T = [lambda_avg]*5000
fig= plt.figure(8)
plt.plot(Th_T, label="the theoretical result",color="red")
plt.plot(create[10:],T,label="the simulation result",color="blue")
plt.title('Throughput')
plt.xlabel('time')# make axis labels
plt.ylabel('throughput')
plt.legend(loc='best')
plt.savefig(path + 'throughput'+'.png')

# ------------------------------------------------------the goodput 理论推导结果------------------------------------
a = []
P = 0.002   # 随机丢包率
q = []      # packet loss due to timeout
for i in cw:
    a.append(int(i)/1400)
for i in a:
    if i <= 3:
        q_i = 0.
    else:
        q_i = ((1-(1-P)**3)*(1+(1-P)**3-(1-P)**i)) / (1-(1-P)**i)/3
    q.append(q_i)
Th_G = []   # 理论实际吞吐量
total_loss = 0  # 临时存储总丢包
loss_timeout = []   # packet loss due to timeout average
for n, i in enumerate(q,1):
    total_loss += i
    loss_to = total_loss / n
    loss_timeout.append(loss_to)
    Gp = (1-P-loss_to-pb[-1])*lambda_avg
    Th_G.append(Gp)
fig= plt.figure(9)
Th_Gxlabel  = [i*2 for i in range(len(Th_G))]
plt.plot(Th_Gxlabel[:2500],Th_G[:2500], label="the theoretical result",color="red")
plt.plot(create,sim_G,label="the simulation result",color="blue")
plt.title('Goodput')
plt.xlabel('time')# make axis labels
plt.ylabel('goodput')
plt.legend(loc='best')
plt.savefig(path + 'goodput'+'.png')

# --------------------------------------------------the packet loss due to timeout------------------------------
fig = plt.figure(10)
q_xlabel  = [i*2 for i in range(len(q))]
plt.plot(q_xlabel[:2500],loss_timeout[:2500],label = "the theoretical result",color="red")
# plt.plot(create,pt,label = "the simulation result")
plt.plot(create,pac_loss,label = "the simulation total packet loss",color="blue")
plt.title('Packet loss')
plt.xlabel('time')# make axis labels
plt.ylabel('packet loss')
plt.legend(loc='best')
plt.savefig(path + 'Packet loss'+'.png')
# ------------------------------------------------------------队长概率分布------------------------------------------------------
fig= plt.figure(11)
# the queue size
queue_pro = []
for i in range(10):
    queue_pro.append(length.count(i)/len(length))
# sorted = np.sort(length)
# y = np.arange(len(sorted))/float(len(sorted)-1)
# plt.plot(sorted,y)
# plt.plot(np.cumsum(length))
# plt.plot([i for i in range(10)],queue_pro)
sns.distplot(length,kde=False,fit=stats.expon,label = "the queue size")
# sns.distplot(service_time_0,kde=False,fit=stats.expon,hist=False,label = "the vartual waiting time")
plt.title('queue size')
plt.xlabel('queue size')# make axis labels
plt.ylabel('cumulative distribution probability')
plt.savefig(path + 'queue size'+'.png')

# -----------------------------------------------------RTT-------------------------------------------------------------
fig = plt.figure(12)
plt.plot(create, service_time,color="blue")
plt.title('RTT')
plt.xlabel('time')# make axis labels
plt.ylabel('RTT')
plt.savefig(path + 'RTT'+'.png')

# show the figure
plt.show()
plt.close('all')
