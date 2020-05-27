
import random

popSize = int(input("Enter population size"))
numParamm = int(input("Enter number of parameters"))
numGenes = int(input("Enter the num of genes"))
F = int(input("Enter value of F"))

population = []

bound = 4.096

for i in range(popSize):
    chromosomes = []
    for k in range(numParam):
        chromosome = ''
        for j in range(numGenes):
            num = random.random()
            num = num - 0.5
            if num > 0 :
                gene = 1
            else:
                gene = 0
            chromosome = chromosome+str(gene)
        chromosomes.append(chromosome) 
    population.append(chromosomes)

    

def decimal(chromosome, bound):
    
    chromList = []
    for i in range(len(chromosome)):
        dec_val = 0
        for j in range(len(chromosome[i])):
            dec_val = dec_val + int(chromosome[i][j])*(2**(len(chromosome[i]) - j - 1))
        chromList.append(dec_val%bound)  
    return chromList


def binary(chromosome):
    chromosome = int(chromosome)
    bin_val = '';
    while(chromosome > 0):
        bin_val =   str(chromosome%2) + bin_val
        chromosome = int(chromosome/2)
        
    return bin_val
     

def evaluation(parent,num_of_param):
    #Sphere function
    evalVal = 0
    for i in range(num_of_param):
        evalVal = evalVal + parent[i]**2
    return evalVal


minVal = float('inf')

for i in range(popSize):
    minVal = min(minVal, evaluation(decimal(population[i], bound), numParam))
print(minVal)


count = 0
newMin = float('inf')


while float(minVal) != float(newMin):
    #selection
    minVal = newMin
    
    #Mutation
    mutantVector = []
    childVector = []
    newPopulation = []
    
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
       
        vect1 = decimal(population[var_a],bound)
        vect2 = decimal(population[var_b],bound)
        vect3 = decimal(population[var_c],bound)
        
        for j in range(numParam):   
            diff = vect2[j] - vect3[j]
            mutant.append(binary(vect1[j] + diff))

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
        parent = evaluation(decimal(population[i],bound ), numParam)
        child = evaluation(decimal(childVector[i], bound), numParam)

        if parent <= child :
            newPopulation.append(population[i])
        else:
            newPopulation.append(childVector[i])
    
    
    
    for i in range(popSize):
        newMin = min(newMin, evaluation(decimal(population[i],bound), numParam))
    
    count = count + 1
    population = newPopulation
    
    print("Population : ",count)
    print("Population Minimum : ",newMin)
    

