# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:16:14 2019

@author: Paul Vincent Nonat
"""

import numpy as np
import matplotlib.pyplot as plt

def constant_set(n):
    reciprocal_cn=0 #reciprocal of cn
    for i in range(n):
        reciprocal_cn= reciprocal_cn+ (1/(i+1))
    
    cn = 1/reciprocal_cn
    return cn;

