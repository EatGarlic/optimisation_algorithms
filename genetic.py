import random, matplotlib.pyplot as plt
from context import *
from objective import print_scenario, randomScenario, calculate_cost as fitness


POP_SIZE = 100
GENERATIONS = 500

MUTATION_PROB = 0.05




def mutate(child):
    new_child = child[:]

    new_child[random.randint(0, len(new_child) - 1)] = random.randint(1, len(STAFF_LIST))

    return new_child


def crossover(parent_a, parent_b):
    cross_point = random.randint(1, len(parent_a) - 1)

    return parent_a[:cross_point] + parent_b[cross_point:]


def tournament_selection(population, size=5):
    sample = random.sample(population, size)

    parents = sorted(sample, key=lambda x: fitness(x))[:2]

    return [p[:] for p in parents]


def genetic_algorithm():
    population = [randomScenario() for _ in range(POP_SIZE)]

    avg_costs = []
    best_costs = []

    for _ in range(GENERATIONS):
        # for graphing
        costs = [fitness(i) for i in population]
        avg_costs.append(sum(costs) / len(costs))
        best_costs.append(min(costs))

        new_population = []

        # ensure the best still goes on        
        new_population += [min(population, key=lambda x: fitness(x))[:]]

        for _ in range(POP_SIZE - 1):
            p_a, p_b = tournament_selection(population)
            child = crossover(p_a, p_b)

            if random.random() <= MUTATION_PROB:
                child = mutate(child)

            new_population += [child]

        population = new_population


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

    print_scenario(genetic_algorithm(), True)
    
    global_timer.end()
    print(global_timer)