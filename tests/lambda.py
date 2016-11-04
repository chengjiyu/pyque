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
k = []
for t in range(1, 10000):
    c = (sigma_1+sigma_2)**3*(lambda_1*sigma_2+lambda_2*sigma_1)*t
    d = 1 - np.e ** ((-sigma_1 + sigma_2) * t)
    K = J - a/c*d
    k.append(K)

T = [i for i in range(1, 10000)]
fig= plt.figure(1)
plt.plot(T,k)

v = []
for t in range(1,10000):
    s = (lambda_1*sigma_2+lambda_2*sigma_1)/(sigma_1+sigma_2)*t
    v.append(s)
fig= plt.figure(2)
plt.plot(T,v)

def p(x, y):
    return x*y
s = list(map(p,k,v))
print(s)
fig= plt.figure(3)

plt.plot(T,s)

# show the figure
plt.show()
