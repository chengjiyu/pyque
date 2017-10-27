# **The Layer 2 buffer model between the TCP and the wireless transmission**
----
# Overview
##### 1. The MMPP/G/1 queue -- layer 2 buffer model
##### 2.  The arrival process -- the Markovian TCP source model
##### 3. The service process -- the Markovian wireless transmission model, considering HARQ and ARQ process
----
## Introduction

## I.连续参数的Markov链

$$
\mathrm{P}\{X(t_{n+1})=i_{n+1}|X(t_k)=i_k,\quad 0\le k\le n\}=\mathrm{P}\{X(t_{n+1})=i_{n+1}|X(t_n)=i_n\}
$$

## II.齐次Markov链

$$
\mathrm{P}\{X(s+t)=j|X(s)=i\}=\mathrm{P}\{X(t)=j|X(0)=i\}=p_{ij}(t)
$$
The matrix $\boldsymbol{P}(t)=\{p_{ij}\}\quad(i,j\in S)$ 是概率转移矩阵，满足C-K方程
$$
\boldsymbol{P}(s+t)=\boldsymbol{P}(s)+\boldsymbol{P}(t)\\
\boldsymbol{P}(0)=\boldsymbol{I} \quad \lim_{t\to0}\boldsymbol{P}(t)=\boldsymbol{I}
$$
由上面的C-K方程$\boldsymbol{P}(t)$可表示为
$\boldsymbol{P}(t)=\boldsymbol{I}+\sum\limits_{n=1}^{\infty}\frac{t^n}{n!}\boldsymbol{Q}^n$
显然，$\boldsymbol{P}(t)$完全由矩阵$\boldsymbol{Q}$确定，并且有
$$
\boldsymbol{P}'(0)=\lim_{t\to0}\frac{\boldsymbol{P}(t)-\boldsymbol{P}(0)}{t}=\lim_{t\to0}\frac{\boldsymbol{P}(t)-\boldsymbol{I}}{t}=\boldsymbol{Q}
$$

## III.平稳分布及其矩阵计算

由定义知：$\boldsymbol{\pi}=\boldsymbol{\pi}\boldsymbol{P}(t)$, $\boldsymbol{\pi}\boldsymbol{Q}=\boldsymbol{0}$, $\boldsymbol{\pi}\boldsymbol{e}^T=\boldsymbol{0}$. 具有m状态的连续Markov链，可计算出平稳分布为
$$
\boldsymbol{\pi}=\boldsymbol{e}(\boldsymbol{Q}+\boldsymbol{\Theta})^{-1}
$$
where $\boldsymbol{e}=(1,1,\dots,1)$, and $\boldsymbol{\Theta}$ is a $m\times m$ matrix.

## IV.The 2-state MMPP/G/1 Queue

In 2-state MMPP/G/1 queue $\boldsymbol{\pi}$ is given by
$$
\boldsymbol{\pi}=(\pi_1,\pi_2)=\frac{1}{\sigma_1+\sigma_2}(\sigma_2,\sigma_1) \quad \boldsymbol{g}=(g_1,g_2)=\frac{1}{G_1+G_2}(G_2,G_1)
$$
We write $
Q=
\begin{gather*}
\begin{bmatrix}
-\sigma_1&\sigma_1\\
\sigma_2&-\sigma_2
\end{bmatrix}
\end{gather*}
$,$
\Lambda=
\begin{gather*}
\begin{bmatrix}
\lambda_1&0\\
0&\lambda_2
\end{bmatrix}
\end{gather*}
$,$
G=
\begin{gather*}
\begin{bmatrix}
1-G_1&G_1\\
G_2&1-G_2
\end{bmatrix}
\end{gather*}
$, $
\overline{\lambda} = \boldsymbol{\pi \lambda} = \frac{\lambda_1\sigma_2+\lambda_2\sigma_1}{\sigma_1+\sigma_2}
$

In simulation experiment, we set the MMPP parameters that used in "Steady-state analysis of the MMPP/G/1/K queue"
$\Lambda=
\begin{gather*}
\begin{bmatrix}
1.0722\\
0&0.48976
\end{bmatrix}
\end{gather*}$,$
Q=
\begin{gather*}
\begin{bmatrix}
-8.4733\times 10^{-4}&8.4733\times 10^{-4}\\
5.0201\times 10^{-6}&-5.0201\times 10^{-6}
\end{bmatrix}
\end{gather*}
$,$
P=
\begin{gather*}
\begin{bmatrix}
0.99411&0.00589\\
0.99411&0.00589
\end{bmatrix}
\end{gather*}
$,$\boldsymbol{\pi}=(0.0058897,0.9941103)$,$\overline{\lambda}=0.49319$,$\mu=2.181162$

According to the LST (Laplac-Stieltjies Transform) $L[\boldsymbol{f}(x)]$, we know:
$$
\begin{align}
L[\boldsymbol{f}(x)]&=\left\{\begin{bmatrix} s&0\\0&s \end{bmatrix}-\begin{bmatrix} -\sigma_1&\sigma_1\\-\sigma_2&\sigma_2 \end{bmatrix}+\begin{bmatrix} \lambda_1&0\\0&\lambda_2 \end{bmatrix}\right\}^{-1}\begin{bmatrix} \lambda_1&0\\0&\lambda_2 \end{bmatrix}\\
&=\frac{1}{\mathrm{det}A}\begin{bmatrix} s+\sigma_2+\lambda_2&\sigma_1 \\ \sigma_2&s+\sigma_1\lambda_1 \end{bmatrix}\begin{bmatrix} \lambda_1&0 \\ 0&\lambda_2 \end{bmatrix}\\
&=\frac{1}{\mathrm{det}A}\begin{bmatrix} (s+\sigma_2+\lambda_2)\lambda_1&\lambda_2\sigma_1 \\ \lambda_1\sigma_2&(s+\sigma_1+\lambda_1)\lambda_2
\end{bmatrix}
\end{align}
$$
where $\mathrm{det}A=(s+\sigma_1+\lambda_1)(s+\sigma_2+\lambda_2)-\sigma_1\sigma_2$
不失一般性，我们假设 MMPP 从一到达时刻开始，在到达时刻嵌入的马尔可夫链的稳态分布是：
$$
\boldsymbol{\psi}=\frac{\boldsymbol{\pi \Lambda}}{\boldsymbol{\pi \lambda}}=\frac{1}{\sigma_2\lambda_1+\sigma_1\lambda_2}[\sigma_2\lambda_1 \quad \sigma_1\lambda_2]
$$
so, the LST of the arrival interval:
$$
\begin{align}
L&=\boldsymbol{\psi}\left\{\frac{1}{\mathrm{det}A}\begin{bmatrix} (s+\sigma_2+\lambda_2)\lambda_1&\lambda_2\sigma_1 \\ \lambda_1\sigma_2&(s+\sigma_1+\lambda_1)\lambda_2 \end{bmatrix}\right\}\boldsymbol{e} \\
&=\frac{s(\sigma_1\lambda_2^2+\sigma_2\lambda_1^2)+(\sigma_1\lambda_2+\sigma_2\lambda_1)(\sigma_1\lambda_2+\lambda_1\lambda_2+\sigma_2\lambda_1)}{(\sigma_1\lambda_2+\sigma_2\lambda_1)[s^2+(\sigma_1+\sigma_2+\lambda_1+\lambda_2)s+(\sigma_1\lambda_2+\lambda_1\lambda_2+\sigma_2\lambda_1)]}\\
&=\frac{0.21s+0.22}{0.42(s^2+1.56s+0.53)}
\end{align}
$$
We derive the ILST (Inverse Laplace-Stieltjes Transform) of $L[X]$
$$
l[t]=0.49e^{-0.5t}+0.01e^{-1.06t}
$$

### A.The number of arrivals over the interval

If $N_t$ is the number of arrivals over the interval $(0,t]$, then the mean of $N_t$ is shown in 
$$
E(N_t)=\boldsymbol{\pi \lambda}t=\frac{\lambda_1\sigma_2+\lambda_2\sigma_1}{\sigma_1+\sigma_2}t
$$
$$
Var(N_t)=E(N_t^2)-{[E(N_t)]}^2=\boldsymbol{\pi \lambda}t+2t[(\boldsymbol{\pi \lambda})^2-\boldsymbol{\pi \Lambda}(Q+\boldsymbol{e \pi})^{-1}]+2\boldsymbol{\pi \Lambda}(e^{Qt}-\boldsymbol{I})(Q+\boldsymbol{e \pi})^{-2}\boldsymbol{\lambda}
$$
In "A Markov Modulated Characterization of Packetized Voice and Data Traffic and Related Statistical Multiplexer Performance", it defines the limiting index of dispersion 
$$I(t) = \frac{Var[N_t]}{E[N_t]}=1+A-\frac{A}{B}(1-e^{-B})$$
where $A=\frac{2(\lambda_1-\lambda_2)^2\sigma_1\sigma_2}{(\sigma_1+\sigma_2)^2(\lambda_1\sigma_2+\lambda_2\sigma_1)}$, $B=(\sigma_1+\sigma_2)t$, $A=9.449931582763375$, $B=0.00085235t$

### B.The vartual waiting time distribution

In 2-state MMPP/G/1 queue the LST of the vartual waiting time, can be derive as follow:
$w_v(s)=\frac{s(1-\rho)[(s-\sigma_1-\sigma_2)+(H(s)-1)(g_1\lambda_2+g_2\lambda_1)]}{s^2+[(H(s)-1)(\lambda_1+\lambda_2)-(\sigma_1+\sigma_2)]s+(H(s)-1)[(H(s)-1)\lambda_1\lambda_2-\sigma_1\lambda_2-\sigma_2\lambda_1]}$
$$
w_v(s)=\frac{s(1-\rho)[(s-\sigma_1-\sigma_2)+(H(s)-1)(g_1\lambda_2+g_2\lambda_1)]}{[s+\lambda_1(H(s)-1)-\sigma_1][s+\lambda_2(H(s)-1)-\sigma_2]-\sigma_1\sigma_2}
$$
where $\rho$ is the traffic intensity, $\rho=h\overline{\lambda}\le 1$; and $H(s)$ is the LST of $\widetilde{H}(x)$
and the transform of the waiting time at customer arrival instants $w_a(s)$ can either be calculated from the general relationship
$$
\begin{align}
w_a(s) &= \frac{sh}{\rho (1-H(s))}\cdot(w_v(s)+\rho - 1) = \frac{1}{\overline{\lambda}}\cdot \boldsymbol{W}_v(s)\boldsymbol{\lambda} \\
&= \frac{s^2h(1-\rho)[\lambda_1(1-g_2-\sigma_2)+\lambda_2(1-g_1-\sigma_1)+(H(s)-1)\lambda_1\lambda_2]}{\rho([s+\lambda_1(H(s)-1)-\sigma_1][s+\lambda_2(H(s)-1)-\sigma_2]-\sigma_1\sigma_2)}
\end{align}
$$

$$
w_v = \frac{1}{2(1-\rho)}[2\rho + \overline{\lambda}h^{(2)}-2h((1-\rho)\boldsymbol{g}+h\boldsymbol{\pi}\Lambda)(Q+\boldsymbol{e\pi})^{-1}\boldsymbol{\lambda}]
$$

$$
w_a = \frac{1}{\rho}\Big(w_v - \frac{1}{2}\overline{\lambda}h^{(2)}\Big)
$$

The steady-state vector of $G$ satisfies 
$$
G = \int_0^\infty e^{(Q-\Lambda+\Lambda G)x}\mathrm{d}\widetilde{H}(x) \\
\boldsymbol{g}G=\boldsymbol{g},\quad \boldsymbol{ge = 1}
$$
Using *Newtow-Raphson* method to get the numerical result
$$
G = \boldsymbol\Lambda^{-1}(2\mu \boldsymbol{I+\Lambda-Q}),\quad g=(g_1,g_2)=\frac{1}{\sigma_1\lambda_1+\sigma_2\lambda_2}(\sigma_2\lambda_2,\sigma_1\lambda_1)\\
g = (0.00588774, 0.99411226)
$$

### C.The aggregate probability of packet loss

##### Compute $q_i$
We assume that losses only occur in the direction from the sender to the receiver (no loss of ACKs) and that any segment has a fixed probability $p$ to get lost. More precisely, the random variable defined by the number of consecutive segments that are transmitted before loss has a geometric distribution with parameter $1 − p$
The probability $q_i$ that a loss is due to TO when $W^{c}=i$ is given by:
$$
q_i = 1\quad \text{if} \ i\leq 2b+1\\
$$
and
$$
q_i = \frac{[1-(1-p)^{2b+1}][1+(1-p)^{2b+1}-(1-p)^i]}{1-(1-p)^i}
\ \text{if} \ i \geq 2b+1
$$

### D.The mean throughput of the continous time finite capacity queue

We define the long-term steady-state TCP throughput $Tp$ to be
$$
Tp=\lim_{t \to \infty}Tp_t=\lim_{t \to \infty}\frac{N_t}{t}
$$
Because $Tp$ is the number of packets sent per unit of time regardless of loss, $Tp_t$ represents the throughput of the connection, distinguished with goodput. 
- The goodput of TCP connection is defined as 
$$
Gp=\lim_{t \to \infty}Gp_t=\lim_{t \to \infty}\frac{(1-q_i-p)N_t}{t}
$$
The goodput is computed as the mean number of segments successfully transmitted during a cycle over the mean duration of a cycle.

## 1. The MMPP/G/1 queue

### 1.1 The arrival process -- Markov-Modulated Poisson Process(MMPP)
The MMPP is a doubly stochastic process and the arrival rate is $\lambda^*[J(t)]$.

The arrival rate of MMPP depends on the state of the source. The state of the source $J(t)$ is a $m$-states irreducible Markov process, and when the source is in state $i$, i.e. $J(t)=i$. the arrival rate is $\lambda_i$

The MMPP is parameterized by the m-state continuous Markov process with infinitesimal generator $Q$ and the $m$ Poisson arrival rate $\lambda_1,\lambda_2,\dots,\lambda_m$:

$$
Q=
\begin{gather*}
\begin{bmatrix}
-\sigma_1&\sigma_{12}&\cdots&\sigma_{1m}\\
\sigma_{21}&-\sigma_2&\cdots&\sigma_{2m}\\
\vdots&\vdots&\ddots&\vdots\\
\sigma_{m1}&\sigma_{m2}&\cdots&-\sigma_{m}
\end{bmatrix}
\end{gather*}
$$
$$
\sigma_i = \sum_{j=1,\ j\neq i}^m \sigma_{ij}
$$
$$
\Lambda = \mathrm{diag}(\lambda_1,\lambda_2,\dots,\lambda_m)
$$
$$
\boldsymbol{\lambda} =(\lambda_1,\lambda_2,\dots,\lambda_m)^T
$$
In our analysis, we assume that $\boldsymbol{Q}$ is homogeneous and steady-state vector of the Markov chain is $\boldsymbol{\pi}$:
$$
\boldsymbol{\pi} Q = 0, \quad \boldsymbol{\pi e} = 1
$$
where $\boldsymbol{e} = (1,1,\dots,1)^T$. And the
mean steady-state arrival rate generated by the mean steady-state arrival rate generated by the MMPP is $\overline{\lambda} = \boldsymbol{\pi \lambda}$
MMPP的初始状态（初始概率矢量），即$\psi=P[J_0=i]$ and $\sum\limits_{i}\psi_i=1$. 根据所选的初始矢量的不同，有：
(a)一个从任意到达时刻开始、间隔稳定的MMPP，可以证明其初始矢量是：
$$
\boldsymbol{\psi}=\boldsymbol{\pi \Lambda}/{\overline{\lambda}}
$$
(b)一个环境稳定的MMPP，初始概率矢量是 $\boldsymbol{Q}$ 的稳态矢量 $\boldsymbol{\pi}$. 时间起点不是一个到达时刻，而是按确保环境马尔可夫过程是稳态的原则来选取。
依据上述模型，我们来分析 MMPP 的到达间隔时间分布。设 $X_n$ 表示第 (n-1) 个包和第 n 个包之间的到达间隔时间，and $J_n$ be the state of the Markov process at the $$th arrival. So the sequence ${(J_n,X_n),n\ge 0}$ is a Markov renewal process, and state transition probability matrix is given by
$$
\begin{align}
\boldsymbol{F}(x)&=\int_0^x{exp[(\boldsymbol{Q-\Lambda})\tau]d\tau\boldsymbol{\Lambda}} \\
&=\left.[e^{(\boldsymbol{Q-\Lambda})\tau}]\right|_0^x(\boldsymbol{Q-\Lambda})^{-1}\boldsymbol{\Lambda} \\
&=\left\{e^{(\boldsymbol{Q-\Lambda})x}-\boldsymbol{I}\right\}(\boldsymbol{Q-\Lambda})^{-1}\boldsymbol{\Lambda}
\end{align}
$$
矩阵元素 $F_{ij}(x)$ 是条件概率：$F_{ij}=P\{J_n=j,X_n\ge x|J_{n-1}=i\}$
$\boldsymbol{F}(x)$ 对 x 进行微分，可以求得状态转移概率密度矩阵：
$$
\boldsymbol{f}(x)=\frac{d}{dx}\boldsymbol{F}(x)=\left\{e^{(\boldsymbol{Q-\Lambda})x}(\boldsymbol{Q-\Lambda})\right\}(\boldsymbol{Q-\Lambda})^{-1}\boldsymbol{\Lambda}=e^{(\boldsymbol{Q-\Lambda})x}\boldsymbol{\Lambda}
$$
对上式进行拉普拉斯变换有：
$$
\begin{align}
L[\boldsymbol{f}(x)]&=\int_0^\infty {e^{(\boldsymbol{Q-\Lambda})x}e^{-sx}dx\boldsymbol{\Lambda}} \\
&=\left.[-(s\boldsymbol{I-Q+\Lambda})^{-1}e^{-(s\boldsymbol{I-Q+\Lambda})x}]\right|^{\infty}_0\boldsymbol{\Lambda} \\
&=(s\boldsymbol{I-Q+\Lambda})^{-1}\boldsymbol{\Lambda}
\end{align}
$$

----

Let $N_t$ be the number of arrivals in $(0,t]$
and $J_t$ be the state of the Markov process at time $t$
$$
P_{ij}(n,t) = \mathrm{Pr}\{N_t = n, J_t = j|N_0=0,J_0=i\}
$$
$P_{ij}(n,t)$ is the $(i,j)$ element of matrix $\boldsymbol{P}(n,t)$, the matrices satisfy the forward Chapman-Kolmogorov equations:
$$
\begin{cases}
P'(0,t)=P(0,t)(Q-\Lambda) \\
P'(n,t)=P(n,t)(Q-\Lambda)+P(n-1,t)\Lambda,\quad n\geq 1,t\geq 0
\end{cases}
$$
the matrix generating function $P^*(z,t)=\sum_{n=0}^\infty P(n,t)z^n=e^{(\boldsymbol{Q}-(1-z)\boldsymbol{\Lambda})t}$ then satisfies
$$
\frac{\mathrm{d}}{\mathrm{d}t}P^*(z,t) = P^*(z,t)(Q-\Lambda)+zP^*(z,t)\Lambda,\\
P^*(z,0) = I
$$
so that
$$
P^*(z,t) = e^{(Q-(1-z)\Lambda)t}, \quad |z|\le 1
$$
And, we derive that the generating function of the number of arrivals is $g(z,t)=\boldsymbol{\pi}\{e^{(\boldsymbol{Q}-(1-z)\boldsymbol{\Lambda})t}\}\boldsymbol{e}$
where $\boldsymbol{\pi}$ is the steady-state probability vector of Markov chain and $\boldsymbol{e}=(1,1,\dots,1)^T$ 
Then for the time-stationary version of the MMPP $E[N_t]=g'(1,t)=\boldsymbol{\pi}\{e^{(\boldsymbol{Q}-(1-z)\boldsymbol{\Lambda})t}\Lambda t\}\boldsymbol{e}|_{z=1}=\boldsymbol{\pi \lambda}t$


### 1.2 The service process -- general distribution
The service time distribution is notated as $\widetilde{H}(x)$ with finite mean $h$, second and third moments $h^{(2)}$ and $h^{(3)}$ and LST (Laplac-Stieltjies Transform) $H(s)$
$$
H(s)= E[e^{-sx}] = \int^\infty_0e^{-sx}\ \mathrm{d}\widetilde{H}(x)
$$
$$
h^{(m)} = E[x^m] = (-1)^m H^{(m)}(s)\ \big |\ _{s=0}
$$

#### A.The negative exponential distribution
The probability density function is 
$$
h(x)=
\begin{cases}
\mu e^{-\mu x}, &x \ge 0 \\
0, &x \lt 0
\end{cases}
$$
The cumulative distribution function is $\widetilde{H}(x)=1-e^{-\mu x}$. The LST $H(s)$ is given by
$$
H(s)= E[e^{-sx}] = \int^\infty_0e^{-sx}\ \mathrm{d}\widetilde{H}(x)=\frac{\mu}{s+\mu} \\
h = E(x)=\frac{1}{\mu} \\
h^{(2)} = E(x^2) = \frac{2}{\mu^2} \\
h^{(3)} = E(x^3) = \frac{6}{\mu^3}
$$
The steady-state vector of $G$ satisfies 
$$
G = \int_0^\infty e^{(Q-\Lambda+\Lambda G)x}\mathrm{d}\widetilde{H}(x) \\
\boldsymbol{g}G=\boldsymbol{g},\quad \boldsymbol{ge = 1}
$$


#### B.The geometric distribution

The probability density function is 
$$
h(x)=p(1-p)^{x-1}, \quad x=1,2,3,\dots
$$
The cumulative distribution function is 
$$
\widetilde{H}(x)=\sum^\infty_{x=1}{h(x)}=1-(1-p)^x
$$
The LST $H(s)$ is given by
$$
H(s)= E[e^{-sx}] = \int^\infty_0e^{-sx}\ \mathrm{d}\widetilde{H}(x)=\frac{1}{s-\ln(1-p)} \\
h = E(x)=\frac{1}{p}
$$

### 1.3 Queue model analyze
The arrival process is described as 1.1 and the service process is described as 1.2

Let  $\{\tau_n:n\geq 0\}$ denote the successive epochs of departure (with $\tau_0=0$), and define $X_n$ and $J_n$ to be the number of customers in the system and the state of MMPP at time $\tau_n^{+}$. The sequence $\{(X_n,J_n,\tau_{n+1}-\tau_{n}):\ n\geq 0\}$ forms a semi-Markov sequence on the state space $\{0,1,\dots\}\times\{1,\dots,m\}$. The semi-Markov process is _positive recurrent_ when traffic intensity $\rho = h\lambda_{tot} < 1$. The transition probability matrix is
$$
\widetilde{Q}(x) =
\begin{gather*}
\begin{bmatrix}
\widetilde{B}_0(x)&\widetilde{B}_1(x)&\widetilde{B}_2(x)&\cdots\\
\widetilde{A}_0(x)&\widetilde{A}_1(x)&\widetilde{A}_2(x)&\cdots\\
0&\widetilde{A}_0(x)&\widetilde{A}_1(x)&\cdots\\
0&0&\widetilde{A}_0(x)&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{bmatrix}
\end{gather*}
$$
For $n\geq 0$ , $\widetilde{A}_n(x)$ and $\widetilde{B}_n(x)$ are the $m\times m$ matrices of mass function defined by:
$$
\begin{align}
[\widetilde{A}_n(x)]_{ij} = \mathrm{Pr}\{&\text{Given a departure at time 0, which left at least one customer in the system and the arrival}\\&\text{ process is at state $i$, the next departure occurs no later than time $x$ with the arrival process}\\&\text{ in state $j$,and during that service time there were $n$ arrivals}\}
\end{align}
$$
$$
\begin{align}
[\widetilde{B}_n(x)]_{ij} = \mathrm{Pr}\{&\text{Given a departure at time 0, which left the system empty and the arrival process in state $i$,}\\&\text{the next departure occurs no later than $x$ with arrival process in state $j$,}\\&\text{leaving $n$ customers at system}\}
\end{align}
$$
Review $P(n,t)$ the counting function , it is clear that
$$
\widetilde{A}_n(x) = \int^x_0P(n,t)\ \mathrm{d}\widetilde{H}(t),\ n\geq 0,x\geq 0
$$
define the LST and z-transform:
$$
A_n(s) = \int^\infty_0e^{-sx}\ \mathrm{d}\widetilde{A}_n(x),\quad
B_s(s)=\int^\infty_0e^{-sx}\mathrm{d}\widetilde{B}_n(x)\\
A(z,s) = \sum_{n=0}^\infty A_n(s)z^n,\quad B(z,s) = \sum_{n=0}^\infty B_n(s)z^n\\
A_n = A_n(0) = \widetilde{A}_n(\infty),\quad B_n = B_n(0) = \widetilde{B}_n(\infty)\\
A = A(1,0), \quad B = B(1,0)
$$
$$
A(z,s) = \int^\infty_0 e^{-sx}e^{[(Q-\Lambda)+z\Lambda]x}\mathrm{d} \widetilde{H}(x)\\
A = \int^\infty_0e^{Qt}\mathrm{d}\widetilde{H}(t)
$$
$A_{ij}$ is the probability that a service ends with the MMPP in state $j$ given that the  service began in state $i$. We note that the matrix $A$ is stochastic, and the stationary vector $\boldsymbol{\pi}$ also satisfies $\boldsymbol{\pi}A=\boldsymbol{\pi},\ \boldsymbol{\pi e}=1$
Define the vector $\boldsymbol{\beta}$, and the $j^{th}$ element is $\beta_j$, is the conditional number of arrivals during a service which starts with the arrival process is at state $j$
$$
\boldsymbol{\beta} = \sum^\infty_{k=0}kA_k=\frac{\mathrm{d}}{\mathrm{d}z}A(z,0)|_{z=1}\boldsymbol{e} = \rho \boldsymbol{e}+(Q+\boldsymbol{e\pi})^{-1}(A-I)\boldsymbol{\lambda}
$$

And the matrices $\widetilde{B}_n(x)$ are related to the matrices  $\widetilde{A}_n(x)$ by
$$
\widetilde{B}_n(x)=\int^x_0\mathrm{d}\widetilde{U}(t)\widetilde{A}_n(x-t) = \widetilde{U}(x)\circledast\widetilde{A}_n(x)
$$
where
$$
\widetilde{U}(x)=\int^x_0e^{(Q-A)t} \Lambda\mathrm{d}t
$$
So that
$$
B_n = (\Lambda-Q)^{-1}\Lambda A_n
$$

#### 1.3.1 The queue length distribution at departure instants
The embedded Markov chain at departures which has transition probability matrix $\widetilde{Q}(\infty)$, write the stationary vector of $\widetilde{Q}(\infty)$ as $\boldsymbol{x}=(x_0,x_1,\cdots)$. We obtain the system of equations
$$
\boldsymbol{x\widetilde{Q}(\infty)=x}\\
\boldsymbol{x_i} = \boldsymbol{x_0B_i}+\sum^i_{v=1}\boldsymbol{x_vA_{i+1-v}} , i \geq 0
$$
where $\boldsymbol{x_i} = (x_{i,1},x_{i,2},\cdots)$ is vector and
$$
x_{ij} =\\
\mathrm{Pr}\{\text{a departure leaves the system behind}  \text{ with i customers and the MMPP in state j}\}
$$
the quantities $x_i$ can be determined once $x_0$ is known using the method described in the section below. The vector $x_0$ can be obtained by studying the downward transition of $\widetilde{Q}(\infty)$. In order to reach level $0$ from level $i$, each level in between must be visited, which is knowns as the *left skip-free property*. Moreover, the chance mechanism governing the first passage from levle $i+1$ to level $i$ is the same for all levels with $i\geq 0$, because of the spatial homogeneity of the Markovian chain. Therefore, the first passage time distributions from level $i+1$ to level $i,\ i\geq 0$, play a crucial role in the study of the return time distribution to level $0$.

Define $G_{ij}$ as the probability that a busy period starting with the MMPP in state $i$ and ends in state $j$ (equivalently, the probability that the first passage from $(k+1,i)$ to $(k,j)$ ). The matrix $G$ is the root of
$$
G = \int_0^\infty e^{(Q-\Lambda+\Lambda G)x}\mathrm{d}\widetilde{H}(x)
$$
The steady-state vector of $G$ satisfies
$$
\boldsymbol{g}G=\boldsymbol{g},\quad \boldsymbol{ge = 1}
$$
And $x_0$ is explicitly given by:
$$
\boldsymbol{x_0} = \frac{1-\rho}{\lambda_{tot}}\cdot \boldsymbol{g}(\Lambda -Q)
$$
## 先不考虑
Conceptually, the recursion of $x_i$ can be used to determine the quantities $\boldsymbol{x}_i$.
Set
$$
\boldsymbol{X}(z) = \sum_0^\infty \boldsymbol{x_i}z^i
$$
The moments of the queue length at the departures can be obtained by differentiating $\boldsymbol{X}(x)$. It can be shown that
$$
\boldsymbol{X}(z)[z\boldsymbol{I}-A(z)] = -\boldsymbol{x_0}(Q-\Lambda)^{-1}D(z)A(z)
$$
where $D(z)=(Q-\Lambda) + z\Lambda$, from which it can be shown that
$$
\boldsymbol{X'e} = \frac{1}{2(1-\rho)}\cdot \{\boldsymbol{X}A^{(2)}\boldsymbol{e}+U^{(2)}\boldsymbol{e}+2\{-U^{(1)}-\boldsymbol{X}[\boldsymbol{I} - A^{(1)} ]\}(I-A+\boldsymbol{e\pi})^{-1}\boldsymbol{\beta}\}
$$
and
$$
\begin{align*}
\boldsymbol{X''e} = \frac{1}{3(1-\rho)}&\cdot \{3\boldsymbol{X}^{(1)}A^{(2)}\boldsymbol{e} + \boldsymbol{X}A^{(3)}\boldsymbol{e}+U^{(3)}\boldsymbol{e} +\\
&3\{U^{(2)}+\boldsymbol{X}A^{(2)}-2\boldsymbol{X}^{(1)}[I-A^{(1)}]\}(I-A+\boldsymbol{e\pi}^{-1}\boldsymbol{\beta}\}
\end{align*}
$$
where $U(z) = -\boldsymbol{x_0}(Q-\Lambda)^{-1}D(z)A(z)$ and
$$
\boldsymbol{X}^{(i)} = \boldsymbol{X}^{(i)}(1),\ \boldsymbol{U}^{(i)} = \boldsymbol{U}^{(i)}(1),\ \boldsymbol{A}^{(i)} = \boldsymbol{A}^{(i)}(1)
$$
and we can explicitly write
$$
U(z) = -\boldsymbol{x_0}(Q-\Lambda)^{-1}D(z)A(z),\\
U'(z) = -\boldsymbol{x_0}(Q-\Lambda)^{-1}[D(z)A'(z)+\Lambda A(z)],\\
U''(z) = - \boldsymbol{x_0}(Q-\Lambda)^{-1}[D(z)A''(z)+2\Lambda A'(z)],\\
U^{(3)}(z) = -\boldsymbol{x_0}(Q-\Lambda)^{-1}[D(z)A^{(3)}+3\Lambda A''(z)]
$$

#### 1.3.2 The queue length distribution at an arbitrary time
In this section we derive the formulas for the stationary queue length distribution at an arbitrary time. We define the following stationary probabilities:
$$
y_{i,j}=\mathrm{Pr}\{\text{at an arbitrary time there are } i \text{ customers in the system and the MMPP is in state } j \}
$$
and
$$
\boldsymbol{y_i} = (y_{i,1},y_{i,2},\dots ,y_{i,m})
$$
and it can be shown that
$$
\boldsymbol{y_0}=(1-\rho)\boldsymbol{g}
$$
and
$$
\boldsymbol{y_i} = (\boldsymbol{y_{i-1}}\Lambda-\lambda_{tot}(\boldsymbol{x_{i-1}-x_{i}}))(\Lambda-Q)^{-1}
$$
the unconditional system size distribution at an arbitary time is given by
$$
p_i=\boldsymbol{y_i e}
$$
Finally, it can be shown that the unconditional system size distribution at customer arrival instants, $z_i$, which is identical to the queue length distribution at customer departure instant is
$$
z_i = \boldsymbol{x_ie} = \frac{1}{\lambda_{tot}}\cdot \boldsymbol{y_i\lambda}
$$

Set
$$
\boldsymbol{Y}(z)=\sum^\infty_{i=0}\boldsymbol{y_i}z^i
$$
The moments of the system size at an arbitrary time are given by
$$
\boldsymbol{Y}^{(1)}\boldsymbol{e} = \boldsymbol{X}^{(1)}\boldsymbol{e}+\Big[ \frac{1}{\lambda_{tot}}\boldsymbol{\pi}\Lambda-\boldsymbol{X}\Big](\boldsymbol{e\pi}+Q)^{-1}\Lambda\boldsymbol{e}
$$
and
$$
\boldsymbol{Y}^{(2)}\boldsymbol{e}=\boldsymbol{X}^{(2)}\boldsymbol{e}-2\Big[\boldsymbol{X}^{(1)}-\frac{1}{\lambda_{tot}}\boldsymbol{Y}^{(1)}\Lambda\Big](\boldsymbol{e\pi}+Q)^{-1}\Lambda\boldsymbol{e}
$$

#### 1.3.3 The waiting time distribution
In this section, we calculate the vartual waiting time. Furthermore we introduce the following notation:
$$
\begin{align}
\widetilde{\boldsymbol{W}}(x)=&\{\widetilde{W}_1(x),\widetilde{W}_2(x),\dots,\widetilde{W}_m(x)\}, \text{where $\widetilde{W}_j(x)$ is the joint probability that at}\\ &\text{an arbitrary timeand the system is in state $j$ and a virtual customer who}\\ &\text{arrives at that time the waiting  time at most $x$ before starting service.}
\end{align}
$$
Then the LST of the virtual waiting time distribution is given by:
$$
\boldsymbol{W}_v(s)=\int^\infty_0 e^{-sx}d\widetilde{\boldsymbol{W}}(x), \quad w_v(s)=\boldsymbol{W}_v(s)\boldsymbol{e}
$$
The notation $\widetilde{H}(u)$ is service time distribution, and joint distribution of the virtual waiting time and the state of the MMPP satisfies the Volterra integral equation.
$$
\boldsymbol{\widetilde{W}}(x) = \boldsymbol{y_0}-\int^x_0\boldsymbol{\widetilde{W}}(u)\mathrm{d}uQ+\int^x_0\boldsymbol{\widetilde{W}}(x-u)[1-\widetilde{H}(u)]\matrix{d}u\Lambda
$$


we derive that the joint LST transform of the virtual waiting time and the MMPP's state is shown as follow:
$$
\boldsymbol{W}_v(s)=
\begin{cases}
    s\boldsymbol{y_0}[sI+Q-\Lambda(1-H(s))]^{-1}, &\text{for}\ s>0,\\
    \boldsymbol{\pi}, &\text{for}\ s=0
\end{cases}
$$
The transform of the virtual waiting time $\boldsymbol{W}_v(s)$ satisfies
$$
w_v(s) = \boldsymbol{W}_v(x)\boldsymbol{e}=s\boldsymbol{y_0}[sI+Q-\Lambda(1-H(s))]^{-1}\boldsymbol{e}
$$

## 先不考虑
and the transform of the waiting time at customer arrival instants $w_a(s)$ can either be calculated from the general relationship
$$
w_a(s) = \frac{sh}{\rho (1-H(s))}\cdot(w_v(s)+\rho - 1) = \frac{1}{\overline{\lambda}}\cdot \boldsymbol{W}_v(s)\boldsymbol{\lambda}
$$

$$
w_v = \frac{1}{2(1-\rho)}[2\rho + \overline{\lambda}h^{(2)}-2h((1-\rho)\boldsymbol{g}+h\boldsymbol{\pi}\Lambda)(Q+\boldsymbol{e\pi})^{-1}\boldsymbol{\lambda}]
$$
$$
\begin{align}
w_v^{(2)} = \frac{1}{3(1-\rho)}[3 h(2W'(0)(h\Lambda - I) &- h^{(2)}\boldsymbol{\pi}\Lambda)(Q+\boldsymbol{e\pi})^{-1}\\
&-3h^{(2)}W'(0)\boldsymbol{\lambda} + \overline{\lambda}h^{(3)}]
\end{align}
$$
with
$$
W'(0) = (h\boldsymbol{\pi}\Lambda+(1-\rho)\boldsymbol{g})(Q+\boldsymbol{e\pi})^{-1}-\boldsymbol{\pi}(1+w_v)
$$
$$
W''(0) = (2W'(0)(h\Lambda - I) - h^{(2)}\boldsymbol{\pi}\Lambda) (Q+\boldsymbol{e\pi}) ^ {-1} + w_v^{(2)}\boldsymbol{\pi}
$$
$$
w_a = \frac{1}{\rho}\Big(w_v - \frac{1}{2}\overline{\lambda}h^{(2)}\Big)
$$
$$
w_a^{(2)} = \frac{1}{\rho}\Big(w_v^{(2)}- \frac{\overline{\lambda}h^{(3)}}{3} - \overline{\lambda}w_ah^{(2)}\Big)
$$

#### 1.3.4 Numerical Solution
##### Step.1 Compute the matrix $G$
solve the equation：
$$
G = \int_0^\infty e^{(Q-\Lambda+\Lambda G)x}\mathrm{d}\widetilde{H}(x)
$$
Using *Newtow-Raphson* method to get the numerical result

**Initial Step.** Define
$$
G_0 = 0, H_{0,k} = I, k = 0,1,2,\dots
$$
$$
\Theta = \max_{i}((\Lambda - Q)_{ii}),\\
\gamma_n = \int^\infty_0e^{-\Theta x}\frac{(\Theta x)^n}{n!}\mathrm{d}\widetilde{H}(x), \ n = 0,1,\dots,n^*
$$
where $n^*$ is chosen such that $\sum^{n^*}_{k=1}\gamma_k > 1- \epsilon_1, \ \epsilon_1 \ll 1.$

**Recursion.** For $k = 0,1,2,\dots$, compute
$$
H_{n+1,k} = \Big[I + \frac{1}{\Theta}(Q-\Lambda + \Lambda G_k)\Big]H_{n,k},\quad n = 0,1,2,\dots,n^{*}\\
G_{k+1} = \sum^{n^*}_{n=0}\gamma_n H_{n,k}
$$

**Stop criterion**
$$
||G_{k-1} - G_{k} || < \epsilon_2 \ll 1.
$$
Set
$$
G = G_{k+1}
$$

##### Step 2. Compute the steady state vector $\boldsymbol{g}$ which satisfies
$$
\boldsymbol{g}G=\boldsymbol{g},\quad \boldsymbol{ge} =1
$$

##### Step 3. Compute:
$$
\boldsymbol{x_0} = \frac{1-\rho}{\lambda_{tot}}\boldsymbol{g}(\Lambda - Q)
$$

##### Step 4. Compute the system size distribution  at departures and the moments of the queue length distribution at departures (See 1.3.1)

##### Step 5. Compute
$$
\boldsymbol{y_0} = (1-\rho)\boldsymbol{g}
$$

##### Step 6. Compute the queue length distributiuon at an arbitrary time using the queue length distributions at departures
$$
\boldsymbol{y_i} = (\boldsymbol{y_{i-1}}\Lambda-\lambda_{tot}(\boldsymbol{x_{i-1}-x_{i}}))(\Lambda-Q)^{-1}
$$

##### Step 7. Compute waiting time distributions transform and/or moments (See 1.3.3)

----

## 2. The arrival process - Markovian TCP source model

### 2.1 Defs
1. Delayed ACK : acknowledge $b$ pacekt once
2. Timer : $T_S$, Reset after receive an ACK，until a newer ACK is received（@sender）
3. Time-out $T_O$ : no more data is sent until the expect byte is ACKed
4. Dup-ACK $T_D$ :
5. Current window (in segment) : $W^c$
6. Slow start threshold(SSTH): $W^{ss}$
7. Max allowed window size $W_{max}$

### 2.2 The Model
#### 2.2.1 The State Space
The evolution of the CWND of TCP is described by a homogeneous discrete time Markov chain(DTMC)：$X_n = (W^c_n,W^{ss}_n)$, where $W^c_n$ is the CNWD in the $n^{th}$ round, and $W^{ss}_n$ is the SSTH. When time out occurs, $W^c_n = 0$, the maximum CNWD is $W_{max}$.

The state space is:
1. $X_n = (i,j),\quad i \in \{1,2,\dots,W_{max}\}\  \text{and} \ j\in\{2,\dots,\lfloor W_{max}/2\rfloor\}$，not in the TO state.
2. $X_n = (0,j), \quad j\in\{2,\dots,\lfloor W_{max}/2\rfloor\}$ , in the TO state  

As long as $W^c_n > 1$, the DTMC transit from a state to another state every round
In order to make the mean duration(in seconds) of a time-out period $E[T_{to}]$ equal to RTT times the mean number of successive visits to state $(0,j)$, the following transitions are defined:
- $(0,j) \rightarrow (1,j)$ with probability $p_0$ at the end of a time-out period
- $(0,j) \rightarrow (0,j)$ with probability otherwise.
- $p_0 = RTT/E[T_{to}]$

The state space of this DTMC is the subset of $E'=\{0,\dots,W_{max}\}\times \{2,\dots,\lfloor W_{max}\rfloor\}$, because some states will never be reached. The state space is:

$E = E^0 \bigcup A \bigcup B$   
$E^0 = \{(0,j)\ |\ 2\leq j\leq \lfloor W_{max}/2\rfloor\}$
$B = \{(i,j)\ |\ 2 \leq j \leq i \leq W_{max}\ \text{and}\ j\leq\lfloor W_{max}/2\rfloor\}$
$A = \{(i,j)\ |\ 1\leq i < j \leq \lfloor W_{max}/2\rfloor \ \text{and}\ \exists n\geq 0 \ \text{such  that}\ i=f^{[n]}(1)\}$ where $f(w) = w + \lceil w/b\rceil, \ f^{[0]}(w)=w,\ f^{[n]}=f^{[n-1]}\circ f,\ \text{for} \ n\geq 1$  


The arrival rate of the TCP source depends on the current state. The instant send rate of the TCP source is $W_n^c\lambda_0$, where $\lambda_0$ is the send rate when  $W^c_n = 1$.


#### 2.2.2 Notations in the model
- $T_{to}$ : duration of to period, $T_{ss}$: slow start phase, $T_{ca}$ congestion avoidance phase
- $d_{to},d{ss}\  \text{and}\  d_{ca}$:segments sent during the $T_{to}, T_{ss}, T_{ca}$
- $T^{back}_{E^0}$:the time between time out recovery and the next TO loss
- $d^{back}_{E^0}$:the segments sent during  $T^{back}_{E^0}$
- $N_{loss}$:the mean number of loss detection per cycle
- $\rho$ : throughput, send rate, distinguished with goodput
- $$\rho = \frac{E[d^{back}_{E^0}]+E[d_{to}]}{E[T^{back}_{E^0}]+E[T_{to}]}$$

#### 2.2.3 State transition
##### 2.2.3.1 Slow start
condition： $1\leq i < j \leq \lfloor W_{max}/2\rfloor$
1. $P_{(i,j)(\lceil \gamma i\rceil,j)} = (1-p)^i$ -> no loss
2. $P_{(i,j)(0,\text{max}(\lfloor i/2\rfloor,2))}=[1-(1-p)^i]q_i$ -> time out
3. $P_{(i,j)(\text{max}(\lfloor i/2\rfloor,1),\text{max}(\lfloor i/2\rfloor,2))}=[1-(1-p)^i](1-q_i)$ -> Dup ack

##### 2.2.3.2 Congestion avoidance
condition: $1\leq j \leq i < W_{max}$

CWND is increased by $1/b$ every round
1. $P_{(i,j)(i,j)} = （1-p)^i(1-1/b)$ -> no loss
2. $P_{(i,j)(i+1,j)} = (1-p)^i(1/b)$ -> no loss
3. $P_{(i,j)(0,\text{max}(\lfloor i/2\rfloor,2))}=[1-(1-p)^i]q_i$ -> time out
4. $P_{(i,j)(\text{max}(\lfloor i/2\rfloor,1),\text{max}(\lfloor i/2\rfloor,2))}=[1-(1-p)^i](1-q_i)$ -> Dup ack

##### 2.2.3.3 max window
condition $i=W_{max}$
1. $P_{(W_{max},j)(W_{max},j)}=（1-p)^{W_{max}}$ -> No loss
2. $P_{(W_{max},j)(0,\text{max}(\lfloor W_{max} /2\rfloor,2))} = [1-(1-p)^{W_max}]q_{W_{max}}$ -> TO
3. $P_{(W_{max},j)(\text{max}(\lfloor W_{max}/2\rfloor,1),\text{max}(\lfloor W_{max}/2\rfloor,2))} = [1-(1-p)^{W_{max}}](1-q_{W_{max}})$ -> Dup

##### 2.2.3.4 Time out
for each $j$
1. $P_{(0,j)(0,j)} = 1-(RTT/E[T_{to}])$ -> no acknowledge yet
2. $P_{(0,j)(1,j)} = RTT/E[T_{to}]$ -> ack received

##### 2.2.3.5 Compute $q_i$
We assume that losses only occur in the direction from the sender to the receiver (no loss of ACKs) and that any segment has a fixed probability $p$ to get lost. More precisely, the random variable defined by the number of consecutive segments that are transmitted before loss has a geometric distribution with parameter $1 − p$
The probability $q_i$ that a loss is due to TO when $W^{c}=i$ is given by:
$$
q_i = 1\quad \text{if} \ i\leq 2b+1\\
$$
and
$$
q_i = \frac{[1-(1-p)^{2b+1}][1+(1-p)^{2b+1}-(1-p)^i]}{1-(1-p)^i}
\ \text{if} \ i \leq 2b+1
$$
*proof*
- if $i\leq 2b+1$ then $k\leq 2b$, dup is no possible to happen (no enough segment trigger dup ack) thus the the loss must due to TO
- if $i \geq 2b+1$ then:
	- if $k\leq 2b$, only TO is possible
	- if $k\geq 2b+1$, only less than $2b+1$ segments are received in the next residual round arriving at the receiver （the first $2B+1$ packets in the residual round are not received all）,i.e. the $l^{th}$ segment from the residual round get lost $1\leq l\leq 2b+1$

  denote $L_{k+1}$ as the event corresponding to the loss of the $(k+1)^{th}$ segment is loss, then
  $$
  q_i = p(TO|W^c = i\  \text{and}\ loss) = \sum^{i-1}_{k=0}q_{i,k}P(L_{k+1}|W^c = i\  \text{and}\ loss)
  $$
  where
  $$
  \begin{align}
  q_{i,k} = P(TO|W^c = i\  \text{and}\ L_{k+1}) = \left\{
  \begin{array}{lr}
  1, &  k\leq 2b \\
  1-(1-p)^{2b+1}, & k \geq 2b+1
  \end{array}
  \right.
  \end{align}
  $$
  and
  $$
  P(L_{k+1}|W^c=i\ \& \ L_{k+1})=((1-p)^kp）/(1-(1-p)^i)
  $$

#### 2.2.4 The transition probability matrix
In the section 1, the infinitesimal generator of the Markovian chain is notated as $Q$. And we now have the state transition probability matrix $P$, indeed the relationship between $P$ and $Q$ is simply:
$$
Q = P-I
$$

The state of the DTMC is represented by a tuple $X_n = (W_n^c,W_n^{th})$, we arrange the states in a single line as the $W_n^c$ order. For example, the one-line state is $X'_1,X'_2,X'_3,\dots, X'_n = (0,2),(0,3),(0,4),\dots,(W_{max},\lfloor W_{max} / 2\rfloor)$
The state probability transition matrix 
