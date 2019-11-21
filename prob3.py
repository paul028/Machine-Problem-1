# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:35:00 2019

@author: Paul Vincent Nonat
"""
import numpy as np
import time
import matplotlib.pyplot as plt
import math
start_time = time.time()
n=60000
k=12489
p=0.2

def ln_factorial(n):
    ln_fac=0
    ln_fac=math.lgamma(n+1)
    
    return ln_fac
 
def binpmf(n,p,k):
    p_X_k=np.zeros(((n-k+1),2))
    print("Calculating ln("+str(n)+")")
    ln_n_fac=ln_factorial(n)
    z=0
    for j in range(k,n+1,1):
        
        ln_k_fac=ln_factorial(j)
        ln_nk_fac=ln_factorial(n-j)
        ln_X_p_k= ln_n_fac - ln_k_fac - ln_nk_fac + (j*math.log(p)) + ((n-j)*math.log(1-p))
        
        if j==0:
            p_X_k[z][0]= math.exp(ln_X_p_k)
        else:
            p_X_k[z][0]=  p_X_k[z-1][0]+math.exp(ln_X_p_k)
        print(p_X_k[z])
        p_X_k[z][1]=k+z
        z=z+1
    
    return p_X_k;

prob_X_K=binpmf(n,p,k)

print("Calculation Time: %s seconds " %(time.time() - start_time))
y=prob_X_K[:,0]
x=prob_X_K[:,1]
plt.plot(x,y)
plt.ylabel('P_k(K)')
plt.xlabel('k')
plt.title('Probability Curve')

plt.savefig('result3.1.png')
plt.show()