# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:35:00 2019

@author: Paul Vincent Nonat
"""
import numpy as np
import time
start_time = time.time()
n=60000
k=12489
p=0.5


def ln_factorial(n):
    ln_fac=0
    for x in range(n):
        print(x+1)
        ln_fac= ln_fac + np.log(x+1)
    
    return ln_fac;

def binpmf(n,p,k)
    p_X_k=np.zeros(n-k)
    ln_n_fac=ln_factorial(n)
    z=0
    for k in range(k,n+1,1):
        
        print("Calculating natural logarithm of "+str(k)+"!")
        ln_k_fac=ln_factorial(k)
        print("Calculating natural logarithm of "+str(n-k)+"!")
        ln_n-k_fac=ln_factorial(n-k)
        ln_X_p_k= ln_n_fac - ln_k_fac - ln_n-k_fac + (k*np.log(p)) + ((n-k)*np.log(1-p))
        
        print("Calculating PMF at k="+str(k))
        p_x_k[z]= np.exp(ln_X_p_k)
        z=z+1
        
    return p_X_k;

prob_X_K=binpmf(n,p,k)
print("Calculation Time: %s seconds "(time.time() - start_time))