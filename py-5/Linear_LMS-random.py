
import csv
import math
import numpy as np
import random



total_window_size = 15
wind1 = 0
wind2 = 0
wind3  = 0
lr = 0.001
costs = []
rw = []






with open("stockData_1.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    
    for row in reader:
        rw.append(row)




rw   =  reversed(rw[1: 365])
cnt = 0
for row in rw:
    costs.append(float(row[1]))



mx = -float('inf')
for i in costs:
    mx = max(mx,i)
print(mx)
for i in range(len(costs)):
    costs[i] = costs[i]/mx




trainPatt = int((len(costs) - total_window_size + 1)*0.8)
testingpatterns = len(costs)-trainPatt


r_wind = []
err_train = []
err_testing = []

training_Accuracies = []
testing_Accuracies = []

for k in range(100):
    accu= 0
    for i in range(trainPatt+testingpatterns-total_window_size):
        
        r_wind = []
        for x in range(total_window_size):
            index = int(random.random()*len(costs)*0.8)
            r_wind.append(index)
               
 
        sum = 0
        for j in r_wind:
            sum = sum + costs[j]

        actualValue = costs[r_wind[total_window_size - 1]]
        mean = sum/total_window_size

        sum = 0
        for j in r_wind:
            dev =  costs[j] - actualValue
            sum =  dev*dev + sum

        var = math.sqrt(sum/total_window_size)

        if i < trainPatt:
            output = wind1*actualValue + wind2*mean + wind3* var
            #print(output,"---",costs[i + total_window_size])
            error = costs[i + total_window_size] - output
            #print(error)
            wind1 = wind1 + 2*lr*error*actualValue

            wind2 = wind2 + 2*lr*error*mean

            wind3 = wind3 + 2*lr*error*var
           # print(wind1,wind2,wind3)
        
        else:
        
            output = wind1*actualValue + wind2*mean + wind3* var

            error = costs[i + total_window_size] - output
            
            accu = accu + output/costs[i + total_window_size]
            #print(error)
        


total_window_size = 15
w = []
avg_w = []
delta_w = []

for i in range(3):
    w.append(0)
    avg_w.append(0)
    delta_w.append(0)
    
    
lr = 0.001

trainPatt = int((len(costs) - total_window_size + 1)*0.8)
testingpatterns = len(costs)-trainPatt

err_train = []
err_testing = []

training_Accuracies = []
testing_Accuracies = []

for k in range(2000):
   
    avgtesterror = 0
    testaccuracy = 0
    avg_error_train = 0
    trainaccuracy = 0
    for i in range(trainPatt+testingpatterns-total_window_size):
        
        r_wind = []
        for x in range(total_window_size):
            index = int(random.random()*len(costs)*0.8)
            r_wind.append(index)
            
        sum = 0
        for j in r_wind:
            sum = sum + costs[j]
            
        x = []
        actualValue = costs[i + total_window_size - 1]
        x.append(actualValue)
        mean = sum/total_window_size
        x.append(mean)

        sum = 0
        for j in r_wind:
            dev =  costs[j] - costs[i + total_window_size - 1]
            sum =  dev*dev + sum

        var = math.sqrt(sum/total_window_size)
        x.append(var)
        
        if i < trainPatt:
            
            output = 0
            for idx in range(3):
                output = output + w[idx]*x[idx]
                
            error = costs[i + total_window_size] - output
            
            avg_error_train = avg_error_train +error**2
            trainaccuracy = trainaccuracy + output/costs[i + total_window_size]
            
            #computing change in weights
            for idx in range(3):
                delta_w[idx] = delta_w[idx] + 2*lr*error*x[idx]
            
            #computing weights
            for idx in range(3):
                w[idx] = avg_w[idx] + 2*lr*error*x[idx]
            
            
            if i == trainPatt-1:
                for idx in range(3):
                    avg_w[idx] = delta_w[idx]/trainPatt 

           
        
        else:
        
            output = 0
            for idx in range(3):
                output = output + w[idx]*x[idx]
                
            error = costs[i + total_window_size] - output
            
            avgtesterror = avgtesterror +error**2
            testaccuracy = testaccuracy + output/costs[i + total_window_size]
            
    err_train.append((avg_error_train/trainPatt))
    err_testing.append((avgtesterror/testingpatterns))
    training_Accuracies.append(trainaccuracy/trainPatt)
    testing_Accuracies.append(testaccuracy/testingpatterns)

import matplotlib.pyplot as plt

plt.plot(training_Accuracies)
plt.plot(testing_Accuracies)
plt.plot(err_train)
plt.plot(err_testing)

