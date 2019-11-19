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
    return coin; 
#toss coin returns 1 for heads, 0 for tails

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
    
    sum_3sk = S_heads[i-1]+S_heads[j-1]+S_he ads[k-1]
    return sum_3sk;

no_toss=100 # Set the number of toss according to the problem
no_repetition=1000 #Set the number of experiment repetition according to the problem
heads_per_repetition=np.zeros(no_repetition) # initialize numpy array for containing number of heads per experiment
tails_per_repetition=np.zeros(no_repetition) # initialize numpy array for containing number of tails per experiment

for x in range(0,no_repetition): # repeat the experiment 1000 times
       heads_per_repetition[x],tails_per_repetition[x] =experiment(x,no_toss) #returns the number of heads and tails per repetition
       

N_no_repetition=np.zeros(no_repetition)
S_heads=np.zeros(no_toss)
S_tails=np.zeros(no_toss)

for S_k in range(0,no_toss):#Calculate how many trials yield n no of heads, 
    #where the maxinum possible number of heads per trial is 100 since there is 100 toss per trial
    for n in range(0,N_no_repetition.size) :
        if heads_per_repetition[n]==S_k+1:
            S_heads[S_k] = S_heads[S_k]+1 #count the number of trials with S_K+1 heads


c=33
a1=np.zeros(12)
ave1=np.zeros(12)
i=0
for x in range(0,36,3):    
    a1[i]= sum_of_3Sk(c+x,c+x+1,c+x+2) 
    ave1[i]= mean([c+x,c+x+1,c+x+2])
    print('N_1000(S_%d) + N_1000(S_%d) + N_1000(S_%d) = %d' % (c+x,c+x+1,c+x+2,a1[i]))
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
plt.savefig('result1.1.png)
# Display the graph on the screen
plt.show()