# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:15:13 2019

@author: Paul Vincent Nonat
Student Number: 2018-21366

EE 214 MP 1.1

"""

import numpy as np
import matplotlib.pyplot as plt

def toss_coin(): #function to toss a coin
    
    coin=np.random.randint(2) #use randint function to simulate coin flip 
    
    return coin; #toss coin returns 1 for heads, 0 for tails

def experiment(): #Fair coin is tossed no_toss times according to the problem, 
    no_heads=0
    no_tails=0
    result=np.zeros(no_toss)
    print("Tossing Coins 100 Times")
    for x in range(0,no_toss): #simulate coin toss 100 times
        result[x]=toss_coin()

    for i in result: #count the number of heads and tails
        if i ==1:
            no_heads = no_heads+1
        if i==0:
            no_tails = no_tails+1
            
    return no_heads,no_tails;

no_toss=100 # Set the number of toss according to the problem
no_repetition=1000 #Set the number of experiment repetition according to the problem

heads_per_repetition=np.zeros(no_repetition) # initialize numpy array for containing number of heads per experiment
tails_per_repetition=np.zeros(no_repetition) # initialize numpy array for containing number of tails per experiment

for x in range(0,no_repetition): # repeat the experiment 1000 times
       heads_per_repetition[x],tails_per_repetition[x] =experiment() #returns the number of heads and tails per repetition
       

N_no_repetition=np.zeros(no_repetition)
S_heads=np.zeros(no_toss)
S_tails=np.zeros(no_toss)

for S_k in range(0,no_toss):#Calculate how many trials yield n no of heads, 
    #where the maxinum possible number of heads per trial is 100 since there is 100 toss per trial
    for n in range(0,N_no_repetition.size) :
        if heads_per_repetition[n]==S_k+1:
            S_heads[S_k] = S_heads[S_k]+1 #count the number of trials with S_K+1 heads

#a
        
def sum_of_3Sk(i,j,k):
    
    sum_3sk = S_heads[i-1]+S_heads[j-1]+S_heads[k-1]
    return sum_3sk;


G1=sum_of_3Sk(33,34,35)
G2=sum_of_3Sk(33,34,35)
G3=sum_of_3Sk(33,34,35)
G4=sum_of_3Sk(33,34,35)
G5=sum_of_3Sk(33,34,35)
G6=sum_of_3Sk(33,34,35)
G7=sum_of_3Sk(33,34,35)
G8=sum_of_3Sk(33,34,35)
G9=sum_of_3Sk(33,34,35)
G10=sum_of_3Sk(33,34,35)
G11=sum_of_3Sk(33,34,35)
G12=sum_of_3Sk(33,34,35)
