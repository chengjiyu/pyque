import random
import simpy
import numpy as np
from models import source, msg_queue, server
from models import source_model, channel
from models import gol
RANDOM_SEED = 42
SIM_TIME = 20       # Simulation time

def session1():
    env = simpy.Environment()

    # 参数定义
    s_1 = 8.4733 * 10 ** (-4)
    s_2 = 5.0201 * 10 ** (-6)
    pi = np.mat(np.array([0.0058897, 0.9941103]))
    e = np.mat(np.ones((2, 1)))
    In = np.mat(np.eye(2))
    L = np.mat(np.array([[1.0722, 0], [0, 0.48976]]))
    Q_th = np.mat(np.array([[-s_1, s_1], [s_2, -s_2]]))
    fai = pi * L / (pi * L * e)
    l = np.mat(np.array([1.0722, 0.48976]))
    v = 0.182
    d = gol.gol().get_value("d")       # d 的取值范围是 0 - 1, d 由全局变量 _global_dict 获得
    b = v * fai * (
    (Q_th - L).I ** 2 * L * (1 - d) * (In - (1 - d) * (Q_th - L).I * L).I * (Q_th - L).I ** 2 * L - (Q_th - L).I ** 3 * L) * e
    print("----------------------------", (b * l).tolist())
    Q = np.array([[1-0.260364857303, 0.260364857303], [0.43, 0.57]])      # [[1.0 - 0.4567804514083193434060809550457*z,0.4567804514083193434060809550457*z], [z,1-z]]
    # Lambda = np.array((b * l).tolist()[0])   # [1.0722,0.48976]
    Lambda = np.array([1.0722, 0.48976])
    mmpp = source_model.MMPPModel(Q, Lambda)
    # tcp = source_model.TcpSourceModel(7000.)
    src = source.BaseSource(env, mmpp)
    mq = msg_queue.MsgQueue(env)
    src.dst = mq
    ch = channel.ErrorChannel()
    mq.server.set_channel(ch)

    random.seed(RANDOM_SEED)        # This helps reproducing the results
    env.run(until = 5000)

def main():
    session1()

if __name__ == "__main__":
    main()
