
import random
numParam = 2

popSize = int(input("Enter population size"))
numParam = int(input("Enter number of parameters"))
mu = int(input("Enter value of mu"))
eta = int(input("Enter value of eta"))


population = []
bound = 4.096
    
# initialization
for i in range(popSize):
    parent = []
    for j in range(numParam):
        num = random.random()
        num = num - 0.5
    
        real_val = num*bound
        
        parent.append(real_val)
    population.append(parent)


print(population)


def evaluation(parent, numParam):
    #Rosenbrock function
    i = 0
    eval_val = 0
    while(i < numParam):
        eval_val = eval_val +  100*(parent[i]**2 - parent[i+1])**2 + (1 - parent[i])**2
        i = i+2
    return eval_val

min_val = float('inf')

for i in range(popSize):
    min_val = min(min_val, evaluation(population[i], numParam))
print(min_val)


def sorting(lst, numParam):
    for i in range(len(lst)):
            j = i
            while (j < len(lst) - i-1):
                if(evaluation(lst[j], numParam) > evaluation(lst[j+1], numParam)):
                    temp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = temp
                j = j+1 
        
    return lst

new_min = 0
error = 1
count = 0


while error > 0.01:
    #selection
    min_val = new_min
    select_pop = []
    for i in range(popSize):
    
        firstPop = int(random.random()*popSize)
        secondPop = int(random.random()*popSize)
    
        
        evalfirstPop = evaluation(population[firstPop], numParam)
        evalsecondPop = evaluation(population[secondPop], numParam)
        
        if evalfirstPop <= evalsecondPop:
            select_pop.append(population[firstPop])
        else:
            select_pop.append(population[secondPop])
    #crossover
    children = []
    crossProb = 0.8
    i = 0
   
    
    while i < int(popSize*crossProb):
        rand_num = random.random()
        
        b= 0 
        if rand_num <= 0.5:
            b = (2*rand_num)**(1/(mu+1))
        else:
            b = (1/(2*(1-rand_num)))**(1/(mu+1))
        
        firstChild = []
        secondChild = []
        for j in range(numParam):
            
            firstChild.append(1/2*((1+b)*select_pop[i][j] + (1-b)*select_pop[i+1][j]))
            secondChild.append(1/2*((1-b)*select_pop[i][j] + (1+b)*select_pop[i+1][j]))
        
        i = i + 2
        children.append(firstChild)
        children.append(secondChild)
     

    update_pop = []
    update_pop = update_pop+select_pop
    update_pop = update_pop+children
    
    #Mutation
    new_popSize = popSize + len(children)
    
    mut_prob = 0.2
    
    for index in range(int(new_popSize*0.2)):
        rand_num = random.random()
        
        d = 0
        if rand_num <= 0.5:
            d = (2*rand_num)**(1/(1+eta)) - 1
        else:
            d = 1 - (2*(1-rand_num))**(1/(1+eta))
        
                                                       
        for j in range(numParam):
            update_pop[index][j] = update_pop[index][j] + d
        
    new_pop = []
    
    update_pop = sorting(update_pop, numParam)

    new_pop = update_pop[0:popSize]
    new_min = evaluation(new_pop[0], numParam)
    
    population = new_pop
    count = count + 1
    print("Population : ", count)
    error =  abs(min_val - new_min)
    print("Error Rate :", error)
    
    

