# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 00:33:43 2019

@author: Paul Vincent Nonat
"""

import numpy as np
import time
import matplotlib.pyplot as plt

start_time = time.time()
n=60000
k=12489
p=0.5

def ln_factorial(n):
    ln_n_fac = (n* np.log(n)) - n + 0.5*np.log(2*np.pi*n)
    
    return ln_n_fac;

def binpmf(n,p,k):
    p_X_k = np.zeros(n-k+1)
    z=0
    n_fac = ln_factorial(n)
    for k in range(k,n+1,1):

        ln_X_p_k= n_fac -ln_factorial(k) -ln_factorial(n-k)+ (k*np.log(p)) + ((n-k)*np.log(1-p))
        
        print("Calculating PMF at k="+str(k))
        p_X_k[z]= np.exp(ln_X_p_k)
        print(ln_X_p_k)
        z=z+1
    return p_X_k;

prob_X_K=binpmf(n,p,k)
print("Calculation Time: %s seconds " % (time.time() - start_time))

plt.plot(prob_X_K)
plt.ylabel(r'$\P_k(K)$')
plt.xlabel('k')
plt.title('Probability Curve')

plt.savefig('result3.1.png')
plt.show()