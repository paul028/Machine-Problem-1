# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:36:51 2019

@author: Paul Vincent Nonat
"""
#brute force
#on the report i will also tell that we can achieve the result of this brute force by searching in B only
import numpy as np

q=0.275 #default failure probability per component
p=1-q #default success probability per component
components=np.full(100,p)#initialize component with default probability
components_failure=np.full(100,q)


def series1_40():
    print("1-40 Series")
    prob_series=1
    for x in range(40):
        print(x)
        prob_series=prob_series*(1-components_failure[x])
    
    return prob_series;
    
def parallel41_50():
    print("41-50 Parallel")
    prob_parallelfail=1
    for x in range(40,50):
        print(x)    
        prob_parallelfail=prob_parallelfail*components_failure[x]
        
    prob_parallel=1-prob_parallelfail
    
    return prob_parallel;

def series51_80():
    print("51-80 Series")
    prob_series=1
    for x in range(50,80):
        print(x)  
        prob_series=prob_series*(1-components_failure[x])
        
    return prob_series;

def parallel81_100():
    print("81-100 Parallel")
    prob_parallelfail=1
    for x in range(80,100):
        print(x)  
        prob_parallelfail=prob_parallelfail*components_failure[x]
    
    prob_parallel=1-prob_parallelfail
    
    return prob_parallel;

def system_operational(components_failure):
  
    p_a=series1_40()*parallel41_50() #condition A
    
    p_b=series51_80()*parallel81_100() #condition B
    
    p_system=1-((1-p_a)*(1-p_b))
    return p_a,p_b,p_system;

print(system_operational(components_failure))