# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:35:00 2019

@author: Paul Vincent Nonat
"""
import numpy as np
import time
import matplotlib.pyplot as plt
start_time = time.time()
n=20
k=5
p=0.5


def ln_factorial(n):
    ln_fac=0
    print("Calculating  ln("+str(n)+"!) from the sum of ln(x) from 1 to"+str(n))
    for x in range(n):
        log_x=np.log(x+1)
        print("ln("+str(x+1)+") ="+str(log_x))
        ln_fac= ln_fac + log_x
    
    print("ln("+str(n)+"!) ="+str(ln_fac))
    return ln_fac;

def binpmf(n,p,k):
    p_X_k=np.zeros(n-k+1)
    print("Calculating ln("+str(n)+")")
    ln_n_fac=ln_factorial(n)
    z=0
    for k in range(k,n+1,1):
        
        ln_k_fac=ln_factorial(k)
        ln_nk_fac=ln_factorial(n-k)
        ln_X_p_k= ln_n_fac - ln_k_fac - ln_nk_fac + (k*np.log(p)) + ((n-k)*np.log(1-p))
        print(ln_X_p_k)
        print("Calculating PMF at k="+str(k))
        p_X_k[z]= np.exp(ln_X_p_k)
        print(p_X_k[z])
        z=z+1
        
    return p_X_k;

prob_X_K=binpmf(n,p,k)
print("Calculation Time: %s seconds " %(time.time() - start_time))

plt.plot(prob_X_K)
plt.ylabel(r'$\P_k(K)$')
plt.xlabel('k')
plt.title('Probability Curve')

plt.savefig('result3.1.png')
plt.show()