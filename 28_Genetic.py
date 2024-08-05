# Genetic 8 Queen
import math,random
def Max_Attacks(n):
    sum=0
    for i in range(n):
        sum+=i  # it will return attacks
    return sum

def flipMutation(state):
    n=len(state)
    loc=random.randint(0,n-1)
    state[loc]=random.randint(0,n-1)
    return state
def Crossover(x,y):
    n=len(x)
    loc=random.randint(0,n-1)
    return x[0:loc]+y[loc:n]

def fitness(state):
    n=len(state)
    max_fitnesss=Max_Attacks(n)
    h=0
    for (r1,c1) in enumerate(state):
        for(r2,c2) in enumerate(state):
            if(r1,c1)!=(r2,c2):
                h +=(r1==r2 or c1==c2 or r1-c1==r2-c2 or r1+c1==r2+c2)
    return max_fitnesss-(h/2)

print(Max_Attacks(6))
print(Max_Attacks(5))

print(flipMutation([0,2,0,1]))
print(Crossover([0,1,1,2],[2,1,0,2]))
print(fitness([0,1,0,1]))