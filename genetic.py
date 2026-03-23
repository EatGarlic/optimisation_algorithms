import random, matplotlib.pyplot as plt
from context import *
from vector import printVector, randomVector, cloneVector, vectorCost as fitness


POP_SIZE = 200
GENERATIONS = 200

MUTATION_PROB = 0.05


def mutate(child):
    # flip a random staff assignment for a random project row
    new_child = cloneVector(child)
    
    projectId = random.randint(0, len(new_child) - 1)
    row = [0] * len(STAFF_LIST)
    row[random.randint(0, len(STAFF_LIST) - 1)] = 1
    new_child[projectId] = row

    return new_child


def crossover(parent_a, parent_b):
    cross_point = random.randint(1, len(parent_a) - 1)

    return cloneVector(parent_a[:cross_point]) + cloneVector(parent_b[cross_point:])


def tournament_selection(population, size=5):
    """takes a random selection of the population (equal to size) and selects the best 2 (random shuffles outputing parents)"""
    sample = random.sample(population, size)

    parents = sorted(sample, key=lambda x: fitness(x))[:2]
    parents = [cloneVector(p) for p in parents]

    random.shuffle(parents)

    return parents


def genetic_algorithm(quickFinish=True, quiet=False):
    '''
    main genetic algorithm function. This returns the best solution found using global constant variables POP_SIZE and GENERATIONS. 
    If quickFinish is enabled this will output when/if it reaches an optimal answer.
    '''
    population = [randomVector() for _ in range(POP_SIZE)]

    avg_costs = []
    best_costs = []

    
    gen = 0
    finish = False
    while gen < GENERATIONS and not finish:
        # for graphing
        costs = [fitness(i) for i in population]
        avg_costs += [sum(costs) / len(costs)]
        best_costs += [min(costs)]

        new_population = []

        # ensure the best solution still goes on
        best = min(population, key=lambda x: fitness(x))
        new_population += [cloneVector(best)]

        for _ in range(POP_SIZE - 1):
            p_a, p_b = tournament_selection(population)
            child = crossover(p_a, p_b)

            if random.random() <= MUTATION_PROB:
                child = mutate(child)

            new_population += [child]

        
        population = new_population

        if quickFinish:
            if fitness(min(population, key=lambda x: fitness(x))) == 0:
                finish = True
                if not quiet:
                    print(f'Quick finish after {gen} generations')

        gen += 1

            


    plt.figure(figsize=(9, 5), dpi=400)
    plt.plot(avg_costs, label="avg fitness")
    plt.plot(best_costs, label="best fitness")
    plt.title("Genetic algorithm")
    plt.xlabel("generation")
    plt.ylabel("fitness")
    plt.legend()
    plt.figtext(0.01, 0.015, f"({POP_SIZE=}, {GENERATIONS=})", fontsize=8, fontstyle="italic", color="dimgrey")
    plt.savefig("genetic_graph.png")

    return min(population, key=lambda x: fitness(x))



if __name__ == "__main__":
    from simple_timer import global_timer

    global_timer.start()

    printVector(genetic_algorithm(), True)

    global_timer.end()
    print(global_timer)