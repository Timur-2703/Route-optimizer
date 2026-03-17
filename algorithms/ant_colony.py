from algorithms.two_opt import distance
from graph import total_distance
import random

def init_pheromones(num_cities):
    cities = []
    for i in range(num_cities):
        cities.append([1.0]*num_cities)
    return cities
            
def calculate_attractiveness(pheromones, current_city, next_city, cities):
    attract = pheromones[current_city][next_city] * (1/ distance(cities[current_city],cities[next_city]))

    return attract


def choose_next_city(pheromones, currents_city, visited,cities):
    attract = []
    for i in range(len(cities)):
        if i in visited:
            continue
        else:
            attract.append((i, calculate_attractiveness(pheromones, currents_city, i, cities)))

    total = 0
    for city, value in attract:
        total += value
    
    r = random.random()
    cumulative = 0
    for city, value in attract:
        cumulative += value/total
        if cumulative >= r:
            return city
        

def build_route(pheromones, cities):
    start = random.randint(0, len(cities) - 1)
    visited = [start]

    for i in range(len(cities) - 1):
        next_city = choose_next_city(pheromones, visited[-1], visited, cities)
        visited.append(next_city)
    route = [cities[i] for i in visited]
    return route
    

def update_pheromones(pheromones, all_routes, cities):
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j] *= 0.9
    
    for route in all_routes:
        dist = total_distance(route) 
        for k in range(len(route)-1):
            a = cities.index(route[k])
            b = cities.index(route[k+1])
            pheromones[a][b] += 1/dist


def ant_colony(cities):
    pheromones = init_pheromones(len(cities))
    best_route = None
    best_distance = float('inf')

    for generation in range(100):
        all_routes = []
        for ant in range(20):
            route = build_route(pheromones,cities)
            all_routes.append(route)

            dist = total_distance(route)
            if dist < best_distance:
                best_distance = dist
                best_route = route

        update_pheromones(pheromones, all_routes, cities)

    return best_route
    

    

