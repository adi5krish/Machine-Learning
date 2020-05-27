
import random

popSize = int(input("Enter population size"))
numParamm = int(input("Enter number of parameters"))
numGenes = int(input("Enter the num of genes"))
F = int(input("Enter value of F"))

population = []

bound = 10.24

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

def evaluation(parent,num_of_param):
    #Sphere function
    eval_val = 0
    for i in range(num_of_param):
        eval_val = eval_val + parent[i]**2
    return eval_val


min_val = float('inf')

for i in range(popSize):
    min_val = min(min_val, evaluation(decimal(population[i], bound), numParam))
print(min_val)


def sorting(lst,bound, numParam):
    for i in range(len(lst)):
        j = i
        while (j < len(lst) - i-1):
            if(evaluation(decimal(lst[j], bound), numParam) > evaluation(decimal(lst[j+1], bound), numParam)):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
            j = j+1
    return lst


count = 0
new_min = float('inf')

while min_val != new_min:
    #selection
    min_val = new_min
    selectPop = []
    for i in range(popSize):
    
        firstPop = int(random.random()*popSize)
        secondPop = int(random.random()*popSize)
    
        
        if (evaluation(decimal(population[firstPop],bound), numParam) <= evaluation(decimal(population[secondPop],bound),numParam)):
            selectPop.append(population[firstPop])
        else:
            selectPop.append(population[secondPop])

    #crossover
    children = []
    crossProb = 0.8
    i = 0
    while i < int(popSize*crossProb):
        firstChild = []
        secondChild = []
        for j in range(numParam):
            rand_num = int(random.random()*numParam)
        
            firstChild.append(selectPop[i][j][:rand_num]+selectPop[i+1][j][rand_num:])
            secondChild.append(selectPop[i+1][j][:rand_num]+selectPop[i][j][rand_num:])
        
        i = i + 2
        children.append(firstChild)
        children.append(secondChild)
     
    #print(selectPop)
    update_pop = []
    update_pop = update_pop+selectPop
    update_pop = update_pop+children
      
    #Mutation
    new_popSize = popSize + len(children)
    
    mutationProb = 0.2
    
    for i in range(int(new_popSize*0.2)):
        rand_num = random.random()
        index = int(rand_num*len(update_pop))
        ran_idx = int(random.random()*numParam)
        for j in range(numParam):
            update_pop[index][j] = update_pop[index][j][:ran_idx]+str(1 - int(update_pop[index][j][ran_idx]))+update_pop[index][j][ran_idx + 1:]
        
    new_pop = []
    
    update_pop = sorting(update_pop, bound, numParam)

    new_pop = update_pop[0:popSize]
   
    new_min = evaluation(decimal(new_pop[0],bound), numParam)

    population = new_pop
    eval_values = []
    
    count = count + 1
    print("Population : ",count)
    print("Population Min:", new_min)

