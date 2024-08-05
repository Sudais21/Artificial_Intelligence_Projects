import random


def MaxAttack(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


def crossover(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


def FlipMutate(x):
    n = len(x)
    c = random.randint(0, n - 1)
    x[c] = random.randint(1, n)
    return x


def print_individual(x):
    print("{},  fitness = {}".format(str(x), fitness(x)))


def fitness(x):
    n = len(x)
    max_h = MaxAttack(n)
    h = 0
    for (r1, c1) in enumerate(x):
        for (r2, c2) in enumerate(x):
            if (r1, c1) != (r2, c2):
                h += (r1 == r2 or c1 == c2 or r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2)
    return max_h - (h // 2)


def random_population(size, n):
    population = []
    while len(population) < size:
        individual = []
        for i in range(n):
            individual.append(random.randint(1, n))
        if individual not in population:
            population.append(individual)
    return population


def Selection(population, rate):
    n = len(population)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fitness(population[j]) > fitness(population[j + 1]):
                temp = population[j]
                population[j] = population[j + 1]
                population[j + 1] = temp
    s = n - int(rate * n)
    return population[s:n]


def genetic_queen(population, rate, queens):
    new_population = []
    population = Selection(population, rate)
    n = len(population)
    for i in range(n):
        p1 = random.randint(0, n - 1)
        p2 = random.randint(0, n - 1)
        x = population[p1]
        y = population[p2]
        child = crossover(x, y)
        child = FlipMutate(child)
        new_population.append(child)
        if fitness(child) == MaxAttack(queens):
            print("Solution Found")
            print_individual(child)
            break
            # end of for
    return new_population + population


# --------------Main Part-------------------------------
population_size = 10
no_queens = 6
selection_rate = 0.5
population = random_population(population_size, no_queens)
iteration = 0
while iteration < 20:
    iteration += 1
    print("Iteration ", iteration)
    for chromosome in population:  print_individual(chromosome)
    population = genetic_queen(population, selection_rate, no_queens)
