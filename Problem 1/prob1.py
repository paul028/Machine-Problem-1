# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:15:13 2019
@author: Paul Vincent Nonat
Student Number: 2018-21366
EE 214 MP #1
"""
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
#function to toss a coin
def toss_coin():
    coin=np.random.randint(2) 
#use randint function to simulate coin flip 
#toss coin returns 1 for heads, 0 for tails
    return coin; 
    
def experiment(x,no_toss): 
#Fair coin is tossed no_toss times according to the problem, 
    no_heads=0
    no_tails=0
    result=np.zeros(no_toss)
    print("Tossing Coins 100 Times Trial:"+ str(x+1))
    for x in range(0,no_toss): 
    #simulate coin toss 100 times
        result[x]=toss_coin()
    for i in result: 
    #count the number of heads and tails
        if i ==1:
            no_heads = no_heads+1
        if i==0:
            no_tails = no_tails+1            
    return no_heads,no_tails;

def sum_of_3Sk(i,j,k):
    sum_3sk = S_heads[i-1]+S_heads[j-1]+S_heads[k-1]
    return sum_3sk;

print("Begin Experiment")
no_toss=100 # Set the number of coin toss
no_repetition=1000 #Set the number of experiment repetition
# array for number of heads per experiment
heads_pr=np.zeros(no_repetition) 
# array for number of tails per experiment
tails_pr=np.zeros(no_repetition)

for x in range(0,no_repetition): # repeat the experiment 1000 times
       heads_pr[x],tails_pr[x] =experiment(x,no_toss) 
       #returns the number of heads and tails per repetition       
S_heads=np.zeros(no_toss)
#Array for storing number of heads per trial
for S_k in range(0,no_toss):
#Calculate how many trials yield n no of heads,
#where the maxinum possible number of heads per trial is 100 
#since there is 100 toss per trial
    for n in range(0,no_repetition) :
        if heads_pr[n]==S_k+1:
            S_heads[S_k] = S_heads[S_k]+1 
            #count the number of trials with S_K+1 heads            
c=33
a1=np.zeros(12)
ave1=np.zeros(12)
i=0
for x in range(0,36,3):    
    a1[i]= sum_of_3Sk(c+x,c+x+1,c+x+2) 
    ave1[i]= mean([c+x,c+x+1,c+x+2])
    print('N_1000(S_%d) + N_1000(S_%d) + N_1000(S_%d) = %d' 
          % (c+x,c+x+1,c+x+2,a1[i]))
    i=i+1
 
# Plot the bar graph
plot = plt.bar(ave1,a1) 
# Add the data value on head of the bar
for value in plot:
    height = value.get_height()
    plt.text(value.get_x() + value.get_width()/2.,
             1.002*height,'%d' % int(height), ha='center', va='bottom') 
# Add labels and title
plt.title("Average Number of Heads vs k")
plt.xlabel("Average Number of Heads")
plt.ylabel("k")
plt.savefig('result1.1.png')
# Display the graph on the screen
plt.show()

#1.3 -Probability, Expected value, 
print("Calculate probability for 20 trials")
p=np.zeros(20)
E_X=np.zeros(20)
std_X=np.zeros(20)
print("p    E(X)    STD")
for i in range(20):
    p[i]=heads_pr[i]/no_toss
    E_X[i]=no_toss*p[i]
    std_X[i]=np.sqrt(n*p[i]*(1-p[i]))
    print(str(p[i])+"    "+str(E_X[i])+"    "+str(std_X[i]))