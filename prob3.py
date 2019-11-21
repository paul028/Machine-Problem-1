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


#def ln_factorial(n):
#    ln_fac=0
##    print("Calculating  ln("+str(n)+"!) from the sum of ln(x) from 1 to"+str(n))
#    for x in range(n):
#        log_x=math.log(x+1)
#        print("ln("+str(x+1)+") ="+str(log_x))
#        ln_fac= ln_fac + log_x
#    
#    print("ln("+str(n)+"!) ="+str(ln_fac))
#    return ln_fac;

def binpmf_org(n,p,k):
    p_x_k=np.zeros(n-k+1)
    n_fac=math.factorial(n)
    print(n_fac)
    z=0
    for k in range(k,n+1,1):
        print('---')
        print(k)
        k_fac=math.factorial(k)
        print(k_fac)
        n_k_fac=math.factorial(n-k)
        print(n_k_fac)
        p_x_k[z] = (n_fac/(k_fac*n_k_fac))*pow(p,k)*pow((1-p),(n-k))
        print(p_x_k[z])
        z=z+1
    
    return p_x_k;    
def binpmf(n,p,k):
    p_X_k=np.zeros(n-k+1)
    print("Calculating ln("+str(n)+")")
    ln_n_fac=ln_factorial(n)
    z=0
    for j in range(k,n+1,1):
        
        ln_k_fac=ln_factorial(j)
        ln_nk_fac=ln_factorial(n-j)
        ln_X_p_k= ln_n_fac - ln_k_fac - ln_nk_fac + (j*math.log(p)) + ((n-j)*math.log(1-p))

        p_X_k[z]= math.exp(ln_X_p_k)
        print(p_X_k[z])
        z=z+1
    return p_X_k;

prob_X_K=binpmf(n,p,k)
    
print("Calculation Time: %s seconds " %(time.time() - start_time))

plt.plot(prob_X_K)
plt.ylabel(r'$\P_k(K)$')
plt.xlabel('k')
plt.title('Probability Curve')

#plt.savefig('result3.1.png')
plt.show()