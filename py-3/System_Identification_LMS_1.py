

import csv
import math
import random
import numpy as np
import matplotlib.pyplot as plt

inputVal = []
errors = []
accuracies = []
lr = 0.00001


for row in range(100):
    rand = random.random()
    rand = rand
    inputVal.append(rand)


sysParam = [0.2,0.7,0.2]

avg_w = []
delta_w = []
estParam = []
init_input = []

#initialization

for i in range(len(sysParam)):
    avg_w.append(0)
    delta_w.append(0)
    estParam.append(0)
    init_input.append(0) 

trainPattern = int(len(inputVal))

for epoch in range(15000):
    avg_error = 0
    acc = 0
    for i in range(len(inputVal)):
        
        idx = len(init_input)-1
        while(idx > 0):
        
            init_input[idx] = init_input[idx-1]
            idx = idx -  1

        init_input[0] = inputVal[i]
        
        #actual value  
        actual_val = 0
        for j in range(len(sysParam)):
            actual_val = actual_val + sysParam[j]*init_input[j]

        #estimated value
        estimate_val = 0
        for j in range(len(estParam)):
            estimate_val = estimate_val + estParam[j]*init_input[j]

        #error
        error = actual_val - estimate_val
        acc = acc + estimate_val/actual_val
        avg_error = avg_error + error**2
    
        
           #computing weights
        for idx in range(len(sysParam)):
            estParam[idx] = avg_w[idx] +2*lr*error*init_input[idx]

         #computing change in weights
        for idx in range(len(sysParam)):
            delta_w[idx] = delta_w[idx] + 2*lr*error*init_input[idx]
            
        
            #updating batch weights
        if i == trainPattern-1:
            for idx in range(len(sysParam)):
                avg_w[idx] = delta_w[idx]/trainPattern 
        
       
    errors.append((avg_error/trainPattern))
    accuracies.append(acc/trainPattern)
    
print( "Estimated Parameters : ",estParam)
plt.plot(accuracies)
plt.plot(errors)



