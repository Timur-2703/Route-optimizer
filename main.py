import random
import matplotlib.pyplot as plt
from graph import City, total_distance
from algorithms.genetic import create_population, genetic
from algorithms.greedy import greedy
from visualizer import draw_on_ax
from map_visualizer import get_coordinates, city_from_name, draw_route_on_map
from algorithms.two_opt import distance, swap_reduces_distance, two_opt
from algorithms.simulated_annealing import simulated_annealing
from algorithms.ant_colony import ant_colony

import time

def run_benchmark(cities):
    results = []
    start = time.time()
    greedy_route = greedy(cities)
    elapsed = time.time() - start
    results.append(("Greedy", total_distance(greedy_route), elapsed))

    start = time.time()
    genetic_route, _ = genetic(cities)
    elapsed = time.time() - start
    results.append(("Genetic", total_distance(genetic_route), elapsed))

    start = time.time()
    two_opt_route = two_opt(greedy_route.copy())
    elapsed = time.time() - start
    results.append(("Two_opt", total_distance(two_opt_route), elapsed))

    start = time.time()
    sa_route = simulated_annealing(greedy_route.copy())
    elapsed = time.time() - start
    results.append(("Simulated_ann", total_distance(sa_route), elapsed))

    start = time.time()
    ant_colony_route = ant_colony(cities)
    elapsed = time.time() - start
    results.append(("Ant_colony", total_distance(ant_colony_route), elapsed))

    print(f"{'Алгоритм':<20} {'Длина':<15} {'Время (сек)':<15}")
    print("-" * 50)
    for name, dist, t in results:
        print(f"{name:<20} {dist:<15.2f} {t:<15.4f}")

    return results



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--cities", type = int, default = 20)
parser.add_argument("--algorithm", type = str, default = "all")
parser.add_argument("--benchmark", action = "store_true")
args = parser.parse_args()

test_cities = [City(random.randint(0, 100), random.randint(0, 100), f"City_{i}") for i in range(args.cities)]

if args.benchmark:
    run_benchmark(test_cities)


