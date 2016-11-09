lambda_1 = 1.0722
lambda_2 = 0.48976
sigma_1 = 8.4733*10**(-4)
sigma_2 = 5.0201*10**(-6)
para = {}
para['a'] = sigma_1 + lambda_1
para['b'] = sigma_2 + lambda_2
para['c'] = sigma_1 * lambda_2
para['d'] = sigma_2 * lambda_1
para['e'] = sigma_1 * sigma_2
para['f'] = lambda_1 * lambda_2
para['k'] = (sigma_1 * lambda_2 + sigma_2 * lambda_1) * (sigma_1 * lambda_2 + sigma_2 * lambda_1 + lambda_1 * lambda_2)

a = sigma_1 * (lambda_2**2) + sigma_2 * (lambda_1**2)
b = sigma_1 * lambda_2 + sigma_2 * lambda_1
c = sigma_1 * lambda_2 + sigma_2 * lambda_1 + lambda_1 * lambda_2
d = sigma_1 + lambda_2 + sigma_2 + lambda_1

e = (2*(lambda_1-lambda_2)**2*sigma_1*sigma_2)/((sigma_1+sigma_2)**2*(sigma_1 * lambda_2 + sigma_2 * lambda_1))
f = sigma_1 + sigma_2




print(para['j'], para['k'], para['g'], para['i'], para['h'], a,b,c)