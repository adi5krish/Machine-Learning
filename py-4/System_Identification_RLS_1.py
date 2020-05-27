
import csv
import math
import random
import numpy as np
import matplotlib.pyplot as plt

inputStockValue = []
rows = []

sysParam = [0.2, 0.7, 0.2]

#initialization 
estParam = [0, 0, 0]
initInput = [0, 0, 0]

for row in range(100):
    rand = random.random()
    rand = rand - 0.5
    inputStockValue.append(rand)


R = (10**(5))*np.identity(3,float)

training = int(len(inputStockValue)*0.8)
test = int(len(inputStockValue))- training
errors = []
accuracies = []

for epoch in range(5):
    acc = 0
    avg_error = 0
    count = 0
    for i in range(len(inputStockValue)):
        
        idx = len(initInput)-1
        while(idx > 0):
        
            initInput[idx] = initInput[idx-1]
            idx = idx -1

        initInput[0] = inputStockValue[i]
     
          
        w = estParam
        x = initInput
        
        actual_val = np.matmul(np.transpose(sysParam) , x)
        
        y0 = np.matmul(np.transpose(w),x)

        
        error =  (actual_val - y0)
        acc = acc + y0/actual_val
        avg_error = avg_error + error
        
        z = np.matmul(R, x)
        q = np.matmul(np.transpose(x),z)

        v= 1/(1+q)
        z_n = v*z

        w = np.add(w, error*z_n) 

        estParam = w
        R = R - np.matmul(z_n,np.transpose(z_n))
            
    errors.append((avg_error/len(inputStockValue))**2)    
    accuracies.append(acc/(len(inputStockValue)+1))

print(estParam)
plt.plot(errors)
plt.plot(accuracies)

