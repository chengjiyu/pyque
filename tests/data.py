import re
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
import math

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
create_inter = []
service_time = []   # 保存结束服务 packet 的 服务时间
served = []     # 保存服务结束的时间
buffer = []     # 保存过滤得到的 buffer size 行
length = []     # 保存队列长度
success = []    # 成功接收的包
failure = []    # 接收失败的包
cwnd_time = []  # 窗口反馈时间

match = ['cwnd']
match1 = ['ssth']
match2 = ['server finish serving pdu at']
match3 = ['finish serve Packet	id=']
match4 = ['Buffer size']
match5 = ['The source received feedback for successful delivering']
match6 = ['The source received feedback for transmission failure']

with open ('data.txt', 'r') as d:
    for line in d:
        data.append(line)

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
    if match5 == re.findall(r'The source received feedback for successful delivering', data[i]):
        success.append(data[i])
    if match6 == re.findall(r'The source received feedback for transmission failure', data[i]):
        failure.append(data[i])
# 丢包率
P = len(failure)/(len(success)+(len(failure)))
print('丢包率 ： %f %%' %(P*100))
# 吞吐量
th = (len(success)+(len(failure)))/5000
print('吞吐量 ： %f' %th)

# 找到cwnd的值           
for i in range(len(cwnd)):
    m = re.findall(r'\d+\.?\d*',cwnd[i])
    cw.append(m[0])
print('cwnd: {0}'.format(cw))

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
    create_inter.append(float(m[1]))
    service_time.append(float(m[-1]))
    served.append(float(m[-2]))
print('ID: {0}'.format(id))
print('create: {0}'.format(create))
print('service_time: {0}'.format(service_time))
print('served_time: {0}'.format(served))
print(len(ss[:len(served)]),len(cw[:len(served)]),len(served))
# 计算超时的丢包率
t = 5       # 4.75
j = 0
pkl = []

for i in range(len(service_time)):
    if service_time[i] > t:
        j += 1
        loss = j/(i+1)
        pkl.append(loss)
    else:
        loss = j/(i+1)
        if loss == 0:
            loss += 1
        pkl.append(loss)
print('由于超时的丢包率：{0}'.format(pkl))

# 计算吞吐量
T = []
G = []
for i in range(10,len(id)):
    Tp = id[i]/create[i]
    T.append(Tp)

for i in pkl:
    if i == 1:
        Gp = 0
    else:
        Gp = (1-P-i)*th
    G.append(Gp)
print('Throughput: {}'.format(T))
print('Goopput: {}'.format(G))

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

print('interval: {0}'.format(interval_2))
# the vartual waiting time
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

# 找到队列长度值
for i in range(len(buffer)):
    m = re.findall(r'\d+\.?\d*',buffer[i])
    length.append(int(m[0]))
length = length[0:len(service_time)]
print(len(length),'queue size: {0}'.format(length))

# 计算I = Var（X）/E(X)
N = []
N_t = []
I_t = []
V = []
var_2 = []
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
print('var: {0}'.format(var_2))

with open ('cwnd.txt', 'w') as c:
    c.writelines(cw)
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

print('queue & wait: {0} {1}'.format(queue,wait))

    
# declare a figure object to plot
fig = plt.figure(1)

# plot tps
plt.plot(served,cw[:len(served)], 'b')
plt.plot(served,ss[:len(served)], 'r')

# advance settings
plt.title('time-cwnd')
# plt.xticks(range(len(time), time))

fig= plt.figure(2)
plt.plot(queue,wait)
plt.title('queue-wait')

fig= plt.figure(3)
t_t = [i for i in range(1,len(I_t)+1)]
plt.plot(create,I_t)
plt.title('I_t')

# the arrival interval
fig= plt.figure(4)
# plt.plot(create[1:],interval_2)
plt.plot(interval_2)
plt.title('The arrival interval')

# N_t
fig= plt.figure(5)
plt.plot(create,id)
plt.title('N_t')

# the vartual waiting time
fig= plt.figure(6)
plt.plot(service_time_2)
plt.title('The vartual waiting time')

# the packet loss due to timeout
fig= plt.figure(7)
plt.plot(create,pkl)
plt.title('Packet loss')

# the goodput
fig= plt.figure(8)
plt.plot(create,G,'r')
plt.plot(create[10:],T,'b')
plt.title('Goodput & Throughput')

# the queue size
sorted = np.sort(length)
y = np.arange(len(sorted))/float(len(sorted)-1)

fig= plt.figure(9)
plt.plot(sorted,y)
plt.title('queue size')
# show the figure
plt.show()

