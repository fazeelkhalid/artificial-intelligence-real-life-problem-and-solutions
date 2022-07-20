import numpy as np
import random

population = []
TOTAL_SIZE = 8
population_size = 10


def calculate_fitness_right_diagnol(point, arr):
    row = point[0] + 1
    col = point[1] + 1
    count = 0
    while row < TOTAL_SIZE and col < TOTAL_SIZE:
        if (row, col) in arr:
            count = count + 1
        row = row + 1
        col = col + 1
    return count


def calculate_fitness_left_diagnol(point, arr):
    row = point[0] - 1
    col = point[1] - 1
    count = 0
    while row >= 0 and col <= 0:
        if (row, col) in arr:
            count = count + 1
        row = row - 1
        col = col - 1
    return count


def calculate_fitness_right(point, arr):
    row = point[0]
    col = point[1]
    count = 0
    for i in range(col + 1, 8):
        if (row, i) in arr:
            count = count + 1
    return count


def calculate_fitness_left(point, arr):
    row = point[0]
    col = point[1]
    count = 0
    for i in range(col - 1, -1, -1):
        if (row, i) in arr:
            count = count + 1
    return count


def calculate_fitness_down(point, arr):
    row = point[0]
    col = point[1]
    count = 0
    for i in range(row + 1, 8):
        if (i, col) in arr:
            count = count + 1
    return count


def calculate_fitness_up(point, arr):
    row = point[0]
    col = point[1]
    count = 0
    for i in range(row - 1, -1, -1):
        if (i, col) in arr:
            count = count + 1
    return count


def calculate_fitness(point):
    count = 0
    for row in point:
        count += calculate_fitness_up(row, list(point))
        count += calculate_fitness_down(row, list(point))
        count += calculate_fitness_left(row, list(point))
        count += calculate_fitness_right(row, list(point))
        count += calculate_fitness_left_diagnol(row, list(point))
        count += calculate_fitness_right_diagnol(row, list(point))
    return count


def generate_population():
    global population

    for i in range(population_size):
        checkdup = []
        for j in range(8):
            row = np.random.randint(0, 8)
            col = np.random.randint(0, 8)
            while (row, col) in checkdup:
                row = np.random.randint(0, 8)
                col = np.random.randint(0, 8)
            checkdup.append((row, col))
            population[i][j] = (row, col)


def mutation(offsprings):
    for i in range(0, 8):
        curr = offsprings[i]
        curr = list(curr)
        ran = random.randint(0, 7)
        ind = random.randint(0, 1)
        curr[ind] = ran
        curr = tuple(curr)
        offsprings[i] = curr

    return offsprings


def crossover(p1, p2):
    # 2 point crossover
    point = random.randint(4, 6)
    anotherpoint = random.randint(1, 3)
    offspring = np.empty((2, 8), dtype=tuple)
    parent1 = p1[1]
    parent2 = p2[1]
    offspring[0][0:anotherpoint] = parent1[0:anotherpoint]
    offspring[0][anotherpoint:point] = parent2[anotherpoint:point]
    offspring[0][point:] = parent1[point:]

    offspring[1][0:anotherpoint] = parent2[0:anotherpoint]
    offspring[1][anotherpoint:point] = parent1[anotherpoint:point]
    offspring[1][point:] = parent2[point:]
    return offspring[0], offspring[1]


def remove_duplicates(array):
    checkArray = list(array)
    for i in range(len(array)):
        while checkArray.count(array[i]) > 1:
            array[i] = (random.randint(0, 7), random.randint(0, 7))
    return array


population = np.empty((population_size, 8), dtype=tuple)
generate_population()

itr = 0

while True:
    new_gene = []
    for i in population:
        i = remove_duplicates(i)
        new_gene.append((calculate_fitness(i), i))

    new_gene.sort(key=lambda x: x[0])
    if new_gene[0][0] == 0:
        break
    print(f"Fitness in iteration {itr} is: {new_gene[0][0]}")

    parents = new_gene[0:4]
    offsprings = []
    parentindex = 0
    for p in range(2):
        offspring1, offspring2 = crossover(
            parents[parentindex], parents[parentindex + 1])
        parentindex = parentindex + 2
        offsprings.append(offspring1)
        offsprings.append(offspring2)

    offsprings_fitness = []
    k = 0
    for i in offsprings:
        i = mutation(i)
        i = remove_duplicates(i)
        offsprings_fitness.append((calculate_fitness(i), i))
        new_gene.append(offsprings_fitness[k])
        k = k + 1

    new_gene.sort(key=lambda x: x[0])
    population = np.empty((population_size, 8), dtype=tuple)
    for l in range(population_size):
        population[l] = new_gene[l][1]
    itr = itr + 1

print(f"Solution is {new_gene[0][1]} and it took {itr} iterations to find it")
