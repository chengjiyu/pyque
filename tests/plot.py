import matplotlib.pyplot as plt
def plotLoss(loss, goodput, pb, pt):
    path = 'E:\chengjiyu\研究生毕设\结果图\仿真结果tcpmodel\\'
    plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
    fig = plt.figure(0)
    plt.plot(loss, goodput, label="平均吞吐量", color="red")
    plt.title('不同无线丢包下的实际平均吞吐量')
    plt.xlabel('无线丢包率[%]')  # make axis labels
    plt.ylabel('平均吞吐量')
    plt.legend(loc='best')
    plt.savefig(path + '平均吞吐量' + '.png')

    fig = plt.figure(1)
    plt.plot(loss, pb, label="平均拥塞丢包率", color="red")
    plt.title('不同无线丢包下的平均拥塞丢包率')
    plt.xlabel('无线丢包率[%]')  # make axis labels
    plt.ylabel('平均拥塞丢包率[%]')
    plt.legend(loc='best')
    plt.savefig(path + '平均拥塞丢包率' + '.png')

    fig = plt.figure(2)
    plt.plot(loss, pt, label="平均超时丢包率", color="red")
    plt.title('不同无线丢包下的实际平均超时丢包率')
    plt.xlabel('无线丢包率[%]')  # make axis labels
    plt.ylabel('平均超时丢包率')
    plt.legend(loc='best')
    plt.savefig(path + '平均超时丢包率' + '.png')
    # show the figure
    plt.show()
    plt.close('all')
if __name__ == "__main__":
    loss = [i*0.1 for i in range(6)]
    goodput = [0.431729]
    pb = [0.191205]
    pt = [6.596558]
    plotLoss(loss, goodput, pb, pt)
