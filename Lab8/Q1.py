import random


def evaluateExpression(x, y, z):
    return 6*x**3+9*y**2+90*z-25


def fitness(x, y, z):
    ans = evaluateExpression(x, y, z)
    if ans == 0:
        return 99999
    else:
        return abs(1 / ans)


def fitness(x, y, z):
    ans = evaluateExpression(x, y, z)
    if ans == 0:
        return 99999
    else:
        return abs(1/ans)


solutions = []
for counter in range(1000):
    solutions.append((random.uniform(0, 1000), random.uniform(
        0, 1000), random.uniform(0, 1000)))

for generation_count in range(10000):
    rankedSolutions = []
    # fitness step

    for solution in solutions:
        rankedSolutions.append(
            (fitness(solution[0], solution[1], solution[2]), solution))

    rankedSolutions.sort()
    rankedSolutions.reverse()
    print(f"=== Generation {generation_count} best solutions ====")
    print(rankedSolutions[0])
    if rankedSolutions[0][0] > 999:
        break
    bestSolution = rankedSolutions[:100]
    # print(bestSolution)
    # selection step
    variables = []

    for solution in bestSolution:
        variables.append(solution[1][0])  #  variable x
        variables.append(solution[1][1])  #  variable y
        variables.append(solution[1][2])  #  variable z

    newGeneration = []

    # mutation step
    for counter in range(1000):
        x = random.choice(variables) * random.uniform(0.99, 1.01)
        y = random.choice(variables) * random.uniform(0.99, 1.01)
        z = random.choice(variables) * random.uniform(0.99, 1.01)
        newGeneration.append((x, y, z))

    solutions = newGeneration
