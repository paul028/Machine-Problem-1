# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:35:00 2019

@author: Paul Vincent Nonat
"""
import numpy as np

n=60000
k=12489
p=0.5
def ln_factorial(n):
    ln_fac=0
    for x in range(n):
        print(x+1)
        ln_fac= ln_fac + np.log(x+1)
    
    return ln_fac;


p_X_k=0
ln_n_fac=ln_factorial(n)
for k in range(k,n+1,1):
    
    ln_k_fac=ln_factorial(k)
    ln_n-k_fac=ln_factorial(n-k)
    ln_X_p_k= ln_n_fac - ln_k_fac - ln_n-k_fac + (k*np.log(p)) + ((n-k)*np.log(1-p))
    
#    ln_X_p_k= ln_n_fac - ln_factorial(k) - ln_factorial(n-k) + (k*np.log(p)) + ((n-k)*np.log(1-p))
    p_X_k = p_X_k + np.exp(ln_X_p_k)
    print(k)

print("Probability: "+str(p_X_k))