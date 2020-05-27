
import math
import random

dataset = open("C:\Users\DELL-PC\Desktop\ML\py_codes\py_codes\py_question1\iris.txt","r")

tempList = []
mainList = []
class1 = []
class2 = []
class3 = []


label = 1

for i in range(150):
    tempList = dataset.readline().split(",")
    tempList = [float(x) for x in tempList[0:4]]

    if i%50 == 0 and i>0:
        label = label + 1
    tempList.append(float(label))
    mainList.append(tempList)
    
initCenter = []

for i in range(3):
    initCenter.append(int(random.random()*150))


def euclidDist(src, dest):
    sums = 0
    for i in range(0,4):
        dist = src[i]-dest[i]
        sums = dist*dist + sums
    return math.sqrt(sums)

def average(class_list):
    center = []
    for j in range(4):
        val = 0 
        for i in range(len(class_list)):
            val = class_list[i][j] + val
        val = val/len(class_list)
        center.append(val)
    return center

for i in range(0,150):
    dist = []
    for j in range(3):
        dist.append(euclidDist(mainList[i], mainList[initCenter[j]]))
        
    minVal = min(dist[0], dist[1], dist[2])
    
    if minVal == dist[0]:
        class1.append(mainList[i])
    elif minVal == dist[1]:
        class2.append(mainList[i])
    else:
        class3.append(mainList[i])

print("Number of flowers in class 1 : ",len(class1))
print("Number of flowers in class 2 : ",len(class2))
print("Number of flowers in class 3 : ",len(class3))

oldCenter = []
for i in range(3):
    oldCenter.append(mainList[initCenter[i]])

print("oldCenter : ",oldCenter)


    
newCenter = []
while True:
    newCenter = []

    newCenter.append(average(class1))
    newCenter.append(average(class2))
    newCenter.append(average(class3))
    
    
    if oldCenter == newCenter :
        break
    
    class1 = []
    class2 = []
    class3 = []

    for i in range(0,150):
        
        for j in range(3):
            dist[j] = euclidDist(mainList[i], newCenter[j])
        
        minVal = min(dist[0], dist[1], dist[2])
        
        if minVal == dist[0]:
            class1.append(mainList[i])
        elif minVal == dist[1]:
            class2.append(mainList[i])
        else:
            class3.append(mainList[i])   
   
    oldCenter = newCenter  

print("After convergence")

print("Flowers in class-1 : ",len(class1))
print("Flowers in class-2 : ",len(class2))
print("Flowers in class-3 : ",len(class3))

