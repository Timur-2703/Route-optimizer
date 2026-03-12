import random
from graph import City, total_distance

def create_population(cities, size):
    population = []
    for i in range(size):
        route = cities.copy()
        random.shuffle(route)
        population.append(route)

    return population

def select_best(population,k):
    sorted_pop = sorted(population, key = total_distance)
    return sorted_pop[:k]

def ox_crossover(parent1,parent2):
    size = len(parent1)

    start = random.randint(0, size-1)
    end = random.randint(start + 1, size)

    child = [None] * size
    child[start:end] = parent1[start:end]

    remaining = [city for city in parent2 if city not in child]

    j = 0
    for i in range(size):
        if child[i] is None:
            child[i] = remaining[j]
            j += 1
    return child

def mutate(route, mutation_rate = 0.1):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

    return route

def genetic(cities, pop_size = 200, generations = 1000):
    population = create_population(cities, pop_size)
    history =[]


    for generation in range(generations):
        best = select_best(population, pop_size//2)

        history.append(total_distance(best[0]))

        new_population = best.copy()

        while len(new_population) < pop_size:
            parent1 = random.choice(best)
            parent2 = random.choice(best)
            child = ox_crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    return select_best(population, 1)[0], history


