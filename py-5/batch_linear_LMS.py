
import csv
import math
import matplotlib.pyplot as plt

prices = []
rows = []
trainErrors = []
testErrors = []
trainAccuracies = []
testAccuracies = []
lr = 0.001

with open("stockData_1.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    
    for row in reader:
        rows.append(row)

rows   =  reversed(rows[1: 365])
count = 0

for row in rows:
    prices.append(float(row[1]))


#Normalization
mx = -float('inf')
for i in prices:
    mx = max(mx,i)
print(mx)
for i in range(len(prices)):
    prices[i] = prices[i]/mx


windowSize = 15
w = []
avg_w = []
delta_w = []

for i in range(3):
    w.append(0)
    avg_w.append(0)
    delta_w.append(0)
    
    
trainPatterns = int((len(prices) - windowSize + 1)*0.8)
testPatterns = len(prices)-trainPatterns


for k in range(2000):
   
    avgtrainError = 0
    trainAccuracy = 0
    avgtestError = 0
    testAccuracy = 0
    

    for i in range(trainPatterns+testPatterns-windowSize):
        x = []
        sum = 0
        for j in range(i, i + windowSize):
            sum = sum + prices[j]

        act_val = prices[i + windowSize - 1]
        x.append(act_val)
        mean = sum/windowSize
        x.append(mean)

        sum = 0
        for j in range(i, i + windowSize):
            dev =  prices[j] - prices[i + windowSize - 1]
            sum =  dev*dev + sum

        variance = math.sqrt(sum/windowSize)
        x.append(variance)
        
        if i < trainPatterns:
            
            output = 0
            for idx in range(3):
                output = output + w[idx]*x[idx]
                
            error = prices[i + windowSize] - output
            
            avgtrainError = avgtrainError +error**2
            trainAccuracy = trainAccuracy + output/prices[i + windowSize]
            
            #computing change in weights
            for idx in range(3):
                delta_w[idx] = delta_w[idx] + 2*lr*error*x[idx]
            
            #computing weights
            for idx in range(3):
                w[idx] = avg_w[idx] + 2*lr*error*x[idx]
            
            #updating batch weights
            if i == trainPatterns-1:
                for idx in range(3):
                    avg_w[idx] = delta_w[idx]/trainPatterns 

        
        else:
        
            output = 0
            for idx in range(3):
                output = output + w[idx]*x[idx]
                
            error = prices[i + windowSize] - output
            
            avgtestError = avgtestError +error**2
            testAccuracy = testAccuracy + output/prices[i + windowSize]

    trainErrors.append((avgtrainError/trainPatterns))
    testErrors.append((avgtestError/testPatterns))
    trainAccuracies.append(trainAccuracy/trainPatterns)
    testAccuracies.append(testAccuracy/testPatterns)
    
plt.plot(trainAccuracies)
plt.plot(testAccuracies)
plt.plot(trainErrors)
plt.plot(testErrors)

