import re
import matplotlib.pyplot as plt
data = []       # 生成的原始数据
cwnd = []       # 保存过滤得到含有 cwnd 的行
cw = []         # 保存 cwnd 的值
ssth = []       # 保存过滤得到含有 ssth 的行
ss = []         # 保存 ssth 的值
time = []
ti = []
finish = []     # 保存过滤得到完成服务 packet 信息
id = []         # 保存结束服务 packet 的 id
service_time = []   # 保存结束服务 packet 的 服务时间
buffer = []     # 保存过滤得到的 buffer size 行
length = []     # 保存队列长度
success = []    # 成功接收的包
failure = []    # 接收失败的包

match = ['cwnd']
match1 = ['ssth']
match2 = ['server finish serving pdu at']
match3 = ['finish serve Packet	id=']
match4 = ['Buffer size:']
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
    if match4 == re.findall(r'Buffer size:', data[i]):
        buffer.append(data[i])
    if match5 == re.findall(r'The source received feedback for successful delivering', data[i]):
        success.append(data[i])
    if match6 == re.findall(r'The source received feedback for transmission failure', data[i]):
        failure.append(data[i])
# 丢包率
loss = len(failure)/(len(success)+(len(failure)))
print('丢包率 ： %f' %(loss*100))
# 吞吐量
th = len(success)*1400/1000
print('吞吐量 ： %f' %th)

# 找到cwnd的值           
for i in range(len(cwnd)):
    m = re.findall(r'\d+\.?\d*',cwnd[i])
    cw.append(m[0])
print(len(cw))

# 找到ssth的值           
for i in range(len(ssth)):
    m = re.findall(r'\d+\.?\d*',ssth[i])
    ss.append(m[1])
print(len(ss))

# 找到time的值
for i in range(len(time)):
    m = re.findall(r'\d+\.?\d*',time[i])
    ti.append(m[0])
print(len(ti))

# 找到finsih serve Packet id and service_time
for i in range(len(finish)):
    m = re.findall(r'\d+\.?\d*',finish[i])
    id.append(m[0])
    service_time.append(float(m[-1]))
print(service_time)

# 找到队列长度值
for i in range(len(buffer)):
    m = re.findall(r'\d+\.?\d*',buffer[i])
    length.append(int(m[0]))
length = length[0:len(service_time)]
print(length)

with open ('cwnd.txt', 'w') as c:
    c.writelines(cw)
# 队长和等待时间
c = []
queue = []      # 保存队列长度
for j in range(max(length)+1):       # j 是队长列表中的值
    queue.append(j)
    b = [i for i, a in enumerate(length) if a == j]      # b 是不同队长对应的索引值
    c.append(b)
wait = []
for k in range(len(c)):
    s = 0
    for l in range(len(c[k])):
        s += service_time[c[k][l]]     # [c[k][l]] 是队长列表相同队长对应等待时间的索引值
    wait.append(s/len(c[k]))

print(queue,wait)

    
# declare a figure object to plot
fig = plt.figure(1)

# plot tps
plt.plot(cw, 'b')
plt.plot(ss, 'r')

# advance settings
plt.title('time-cwnd')
# plt.xticks(range(len(time), time))

fig= plt.figure(2)
plt.plot(queue,wait)

# show the figure
plt.show()
