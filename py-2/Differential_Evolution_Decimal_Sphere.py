import random

popSize = int(input("Enter population size"))
numParamm = int(input("Enter number of parameters"))
numGenes = int(input("Enter the num of genes"))
F = int(input("Enter value of F"))

population = []

bound = 10.24

# initialization
for i in range(popSize):
    parent = []
    for j in range(numParamm):
        num = random.random()
        num = num - 0.5
    
        realVal = num*bound
        
        parent.append(realVal)
    population.append(parent)
    

def evaluation(parent,numParamm):
    #Sphere function
    evalValue = 0
    for i in range(numParamm):
        evalValue = evalValue + parent[i]**2
    return evalValue


minVal = float('inf')

for i in range(popSize):
    minVal = min(minVal, evaluation(population[i], numParam))
print(minVal)


count = 0
newMinimum = float('inf')

error = 1

while error > 0.0001:
    #selection
    minVal = newMinimum
    
    #Mutation
    
    newPopulation = []
    childVector = []
    mutantVector = []
    
    for i in range(popSize):
        var_a = i
        while var_a == i:
            var_a = int(random.random()*popSize)
        var_b = var_a
        
        while var_b == var_a:
            var_b = int(random.random()*popSize)
        var_c = var_b
        
        while var_c == var_a or var_c == var_b:
            var_c = int(random.random()*popSize)

        mutant = []   
        for j in range(numParam):   
            mutant.append(population[var_a][j] + F*(population[var_b][j] - population[var_c][j]))

        mutantVector.append(mutant)

    #crossover
    CR = 0.5
    for i in range(popSize):
        child = []

        for j in range(numParam):
            prob = random.random()
            if prob >= CR :
                    child.append(population[i][j])
            else:
                    child.append(mutantVector[i][j])

        childVector.append(child)
    
    #Selection
    for i in range(popSize):
        parent = evaluation(population[i], numParam)
        child = evaluation(childVector[i], numParam)

        if parent <= child :
            newPopulation.append(population[i])
        else:
            newPopulation.append(childVector[i])
    
    
    
    for i in range(popSize):
        newMinimum = min(newMinimum, evaluation(population[i], numParam))
    
    count = count + 1
    population = newPopulation
    
    error = abs(minVal - newMinimum)
    print("Population : ",count)
    print("Population Min: ",newMinimum)

