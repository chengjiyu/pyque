syms z n Q L t x s u
% lambda_1 = 1.0722
% lambda_2 = 0.48976
% sigma_1 = 8.4733*10^(-4)
% sigma_2 = 5.0201*10^(-6)
% Q = [-sigma_1, sigma_1; sigma_2, -sigma_2]
% L = [1.0722, 0; 0, 0.48976]

Pz = u*exp(-u*x) * exp((Q-(1-z)*L)*x);
P = u*exp(-u*x) * exp(Q*x);
Pn = iztrans(Pz) 
Hx = 1-exp(-u*x)
A = laplace(P,x,s)