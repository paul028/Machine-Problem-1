# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:36:51 2019

@author: Paul Vincent Nonat
"""
import matplotlib.pyplot as plt
q=0.275 #default failure probability per component
qa=0.275 #qb= qa/0.67
def series1_40(w):
    prob_series=pow((1-qa),40-w)*pow((1-(0.20*qa)),w)
    return prob_series;
    
def parallel41_50(x):
    prob_parallel=1-pow(qa,(10-x))*pow((0.20*qa),x)
    return prob_parallel;

def series51_80(y):
    prob_series=pow((1-(qa/0.67)),30-y)*pow((1-(0.20*qa)),y)
    return prob_series;

def parallel81_100(z):
    prob_parallel=1-pow((qa/0.67),(20-z))*pow((0.20*qa),z)
    return prob_parallel;

def system_operational(w,x,y,z):
  
    p_a=series1_40(w)*parallel41_50(x) #condition A
    
    p_b=series51_80(y)*parallel81_100(z) #condition B
    
    p_system=1-((1-p_a)*(1-p_b))
    return p_system;
    
def component_replacementlist(n): #generate all 20 combinations of components replacement such that a+b+c+d=20 such that a - component 1-40, b - component 41-50, c - component 51-80, d - component 81-100
        print("Generating Replacement Combinations for n="+str(n))
        replaced_components = list()
        len([replaced_components.append((a,b,c,d)) for a in range(41) for b in range(11) for c in range(31) for d in range (21) if a + b + c+d == n]) ##generate combination of components to be replaced
        
        return replaced_components;


print("Begin Experiment")    

replacements=list()
for i in range(101):
    replacements.append(component_replacementlist(i))

print("Calculating All possible working probability")

results=list()
for n in range(101):
    
    result_list= list()
    
    for x in range(len(replacements[n])):
       result_list.append(system_operational(replacements[n][x][0],replacements[n][x][1],replacements[n][x][2],replacements[n][x][3]))
       
    results.append(result_list)

prob_n=list()
for m in range (len(results)):
    prob_n.append(max(results[m]))

plt.plot(prob_n)
plt.ylabel('Operational Probability P[W]')
plt.xlabel('No. of Ultra Reliable Component (n)')
plt.title('System Operational Probability')

plt.annotate('n = 30',
            xy=(30, prob_n[30]), xycoords='data',
            xytext=(0.2, 0.35), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
plt.annotate('n = 70',
            xy=(70, prob_n[70]), xycoords='data',
            xytext=(0.90, 0.55), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
plt.savefig('system2.3.png')
plt.show()