# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:16:14 2019

@author: Paul Vincent Nonat
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
def constant_set(n):
    reciprocal_cn=0 #reciprocal of cn
    for i in range(n):
        reciprocal_cn= reciprocal_cn+ (1/(i+1))
    
    cn = 1/reciprocal_cn
    return cn;

def zipfunc(n,p):
    k=np.zeros(n)
    for m in range (n):
        k_prime=1
        print("Calculating K at n="+str(m+1))
        a= 1/constant_set(k_prime)
        b=p/constant_set(m+1)
        while a < b:
            print("k = "+str(k_prime)+" at n = "+str(m+1))
            print("%f < %f " % (a,b))
            k_prime = k_prime + 1
            k[m] =1+k_prime      
            a= 1/constant_set(k_prime)
            b=p/constant_set(m+1)
    return k;

w=list()
for q in range(1000):
    w.append(constant_set(q+1))

plt.plot(w)
plt.ylabel('c(n)')
plt.xlabel('n')
plt.title(' c(n) Function Graph')
plt.savefig('c_nFunction.png')
plt.show()

n=1000

p1=0.7
k1=zipfunc(n,p1)

p2=0.8
k2=zipfunc(n,p2)

p3=0.9
k3=zipfunc(n,p3)

line_chart1 = plt.plot(k1)
line_chart2 = plt.plot(k2)
line_chart4 = plt.plot(k3)
plt.title(r'$\:k\, for 1 \leq\ n \leq\ %d $' %(n))
plt.ylabel('k')
plt.xlabel('n')
plt.legend(['p='+str(p1),'p='+str(p2),'p='+str(p3)],loc=2)

plt.savefig('Result_4.png')
plt.show()
print("Calculation Time: %s seconds " % (time.time() - start_time))

