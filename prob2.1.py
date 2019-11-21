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
components_failure=np.full(100,q)


def series1_40():
    prob_series=pow((1-q),40)
    return prob_series;
    
def parallel41_50():
    prob_parallel=1-pow(q,(10))
    return prob_parallel;

def series51_80():
    prob_series=pow((1-q),30)
    return prob_series;

def parallel81_100():
    prob_parallel=1-pow(q,(20))
    return prob_parallel;

def system_operational(components_failure):
  
    p_a=series1_40()*parallel41_50() #condition A
    
    p_b=series51_80()*parallel81_100() #condition B
    
    p_system=1-((1-p_a)*(1-p_b))
    return p_system;

print(system_operational(components_failure))