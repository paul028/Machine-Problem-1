1# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:36:51 2019

@author: Paul Vincent Nonat
"""
#brute force
#on the report i will also tell that we can achieve the result of this brute force by searching in B only
def series1_40():
    prob_series=pow((1-q),40)
    return prob_series;
    
def parallel41_50():
    prob_parallel=1-pow(q,10)
    return prob_parallel;

def series51_80(y):
    prob_series=pow((1-q),30-y)*pow((1-(q/10)),y)
    return prob_series;

def parallel81_100(z):
    prob_parallel=1-pow(q,(20-z))*pow((q/10),z)
    return prob_parallel;

def system_operational(y,z):
  
    p_a=series1_40()*parallel41_50() #condition A
    
    p_b=series51_80(y)*parallel81_100(z) #condition B
    
    p_system=1-((1-p_a)*(1-p_b))
    print(p_system)
    return p_system;
    
def component_replacementlist():
        print("Generating Replacement Combinations")
        replaced_components = list()
        len([replaced_components.append((c,d)) for c in range(21) 
        for d in range (21) if c+d == 20])
        
        return replaced_components;

q=0.275 #default failure probability per component
print("Begin Experiment")    
replacements = component_replacementlist()
result_list= list()
print("Calculating All possible working probability")
i=1
for x in range(len(replacements)):
   print(i+x)
   result_list.append(system_operational(replacements[x][0],replacements[x][1]))
print("--------------------------------------------")
m = max(result_list) # get the maximum probability
print("Maximum Possible Operational Probability: "+str(m))
m_index=[i for i, j in enumerate(result_list) if j == m]
replacements[m_index[0]]
print("Components Replaced: \nComponents 51-80: "+str(replacements[m_index[0]][0])+"\nComponents 81-100: "+str(replacements[m_index[0]][1])
      +"\nNumber of trials performed :"+str(len(result_list)))

