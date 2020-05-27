import math
import numpy as np
import matplotlib.pyplot as plt

dataSet = open("C:\Users\DELL-PC\Desktop\ML\py_codes\py_codes\py_question1\iris.txt","r")

tempList = []
mainList = []

label = 1
for i in range(150):
    tempList = dataSet.readline().split(",")
    tempList = [float(x) for x in tempList[0:4]]
    if i%50 == 0 and i>0:
        label = label + 1
    tempList.append(float(label))
    mainList.append(tempList)
    


def euclidDistance(src, dest):
    distance = 0
    for i in range(0,4):
        dist = src[i]-dest[i]
        distance = dist*dist + distance
    return math.sqrt(distance)


def clustDistance(list_a, list_b):
    min_val = float('inf')
    
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            min_val = min(min_val, euclidDistance(list_a[i], list_b[j]))
    return min_val 


def findMin(list_a):
    min_val = float('inf')
    for i in range(len(list_a)):
        for j in range(len(list_a)):
            if i != j:
                temp = min_val
                min_val = min(min_val, list_a[i][j])
                if min_val != temp:
                    row = i
                    col = j
    return row,col,min_val


list_all = []

for i in range(150):
    tempList = []
    tempList.append(i)
    list_all.append(tempList) 


array = []
min_val = float('inf')

row = 0
col = 0
num = 150
for i in range(num):
    tempArray = []
    for j in range(num):
        dist = euclidDistance(mainList[i], mainList[j])
        tempArray.append(dist)
          
    array.append(tempArray)  

row,col,min_val = findMin(array)
min_idx = min(row, col)
max_idx = max(row, col)

distances = []
distances.append(min_val)

list_all[min_idx] = list_all[min_idx] + list_all[max_idx]
list_all.remove(list_all[max_idx])

array.remove(array[max_idx])

threshold = int(input("Enter the threshold value"))


while(num>0):
    num = num - 1
    
    newCluster = []
    for j in range(len(list_all[min_idx])):
        newCluster.append(mainList[list_all[min_idx][j]])
    
    tempList = []    
    for i in range(num):
        
        formedClusters = []
        for j in range(len(list_all[i])):
            formedClusters.append(mainList[list_all[i][j]])
            
    
        tempList.append(clustDistance(newCluster, formedClusters))
       
    
    array.remove(array[min_idx]) 
    array.insert(min_idx, tempList)
   
    if len(array) == 1:
        break
    row,col,min_val = findMin(array)
    min_idx = min(row, col)
    max_idx = max(row, col)
    distances.append(min_val)
    
    list_all[min_idx] = list_all[min_idx] + list_all[ max_idx]
    list_all.remove(list_all[ max_idx])
    array.remove(array[ max_idx])

    if  threshold == len(list_all):
        print("Number of clusters : ", threshold)
        for cluster in range(threshold):
            print("clusters ",(cluster+1)," : ",list_all[cluster])
        break
  
plt.plot(distances)

