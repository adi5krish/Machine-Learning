
import csv
import math
import matplotlib.pyplot as plt

prices = []
rows = []
trainErrors = []
testErrors = []
trainAccuracies = []
testAccuracies = []

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
w1 = 0
w2 = 0
w3 = 0
lr = 0.001

trainPatterns = int((len(prices) - windowSize + 1)*0.8)
testPatterns = len(prices)-trainPatterns

#iteration over 10 times
for k in range(10):
    
    for i in range(trainPatterns+testPatterns-windowSize):

        sum = 0
        for j in range(i, i + windowSize):
            sum = sum + prices[j]

        act_val = prices[i + windowSize - 1]
        mean = sum/windowSize

        sum = 0
        for j in range(i, i + windowSize):
            dev =  prices[j] - prices[i + windowSize - 1]
            sum =  dev*dev + sum

        variance = math.sqrt(sum/windowSize)

        if i < patterns_train:

            output = w1*act_val + w2*mean + w3* variance

            error = prices[i + windowSize] - output
            
            acc = output/prices[i + windowSize]
            errors_train.append(error**2)
            accuracies_train.append(acc)
           
            w1 = w1 + 2*lr*error*act_val

            w2 = w2 + 2*lr*error*mean

            w3 = w3 + 2*lr*error*variance
        
        else:
            
            output = w1*act_val + w2*mean + w3* variance

            error = prices[i + windowSize] - output
            
            acc = output/prices[i + windowSize]
            errors_test.append(error**2)
            accuracies_test.append(acc)

plt.plot(accuracies_train)

plt.plot(accuracies_test)

plt.plot(errors_train)

plt.plot(errors_test)

