# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:35:00 2019

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
    ln_fac = np.zeros(n)
    for k in range(n):
        ln_fac[k]=np.log(k+1)
        print("ln("+str(k+1)+") ="+str(ln_fac[k]))
    return ln_fac;




#def binpmf(n,p,k):
print("Calculate all ln from 1 to n")
ln_n_fac = ln_factorial(n)

p_X_k = np.zeros(n-k+1)
z=0
for k in range(k,n+1,1):
    
    ln_k_fac=0
    
    for l in range(k):
        ln_k_fac= ln_k_fac+ln_n_fac[l]
     
    ln_nk_fac=0
    for l in range(n-k):
        ln_nk_fac = ln_nk_fac+ln_n_fac[l]
        
    
    ln_X_p_k= ln_n_fac.sum() - ln_k_fac - ln_nk_fac + (k*np.log(p)) + ((n-k)*np.log(1-p))
    
    print("Calculating PMF at k="+str(k))
    p_X_k[z]= np.exp(ln_X_p_k)
    z=z+1
        
#    return p_X_k;

#prob_X_K=binpmf(n,p,k)
print("Calculation Time: %s seconds " % (time.time() - start_time))

plt.plot(prob_X_K)
plt.ylabel(r'$\P_k(K)$')
plt.xlabel('k')
plt.title('Probability Curve')

plt.savefig('result3.1.png')
plt.show()