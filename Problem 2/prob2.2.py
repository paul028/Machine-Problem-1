# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:36:51 2019

@author: Paul Vincent Nonat
"""
#brute force
#on the report i will also tell that we can achieve the result of this brute force by searching in B only
import numpy as np
from itertools import combinations
q=0.275 #default failure probability per component

def series1_40(w):
    prob_series=pow((1-q),40-w)*pow((1-(q/10)),w)
    return prob_series;
    
def parallel41_50(x):
    prob_parallel=1-pow(q,(10-x))*pow((q/10),x)
    return prob_parallel;

def series51_80(y):
    prob_series=pow((1-q),30-y)*pow((1-(q/10)),y)
    return prob_series;

def parallel81_100(z):
    prob_parallel=1-pow(q,(20-z))*pow((q/10),z)
    return prob_parallel;

def system_operational(w,x,y,z):
  
    p_a=series1_40(w)*parallel41_50(x) #condition A
    
    p_b=series51_80(y)*parallel81_100(z) #condition B
    
    p_system=1-((1-p_a)*(1-p_b))
    print(p_system)
    return p_system;
    
def component_replacementlist(): #generate all 20 combinations of components replacement such that a+b+c+d=20 such that a - component 1-40, b - component 41-50, c - component 51-80, d - component 81-100
        replaced_components = list()
        len([replaced_components.append((a,b,c,d)) for a in range(21) for b in range(21) for c in range(21) 
        for d in range (21) if a + b + c+d == 20 and b<=10]) ##generate combination of components to be replaced
        
        return replaced_components;


print("Begin Experiment")    
replacements = component_replacementlist()
result_list= list()
print("Calculating All possible working probability")
i=1
for x in range(len(replacements)):
   print(i+x)
   result_list.append(system_operational(replacements[x][0],
   replacements[x][1],replacements[x][2],replacements[x][3]))
print("--------------------------------------------")
m = max(result_list) # get the maximum probability
print("Maximum Possible Operational Probability: "+str(m))
m_index=[i for i, j in enumerate(result_list) if j == m]
replacements[m_index[0]]
print("Components Replaced: \nComponents 1-40: "+str(replacements[m_index[0]][0])+"\nComponents 41-50: "+str(replacements[m_index[0]][1])+"\nComponents 51-80: "+str(replacements[m_index[0]][2])+" \nComponents 81-100: "
      +str(replacements[m_index[0]][3])+"\nNumber of trials performed :"+str(len(result_list)))

