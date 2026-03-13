import random
import matplotlib.pyplot as plt
from graph import City, total_distance
from algorithms.genetic import create_population, genetic
from algorithms.greedy import greedy
from visualizer import draw_on_ax
from map_visualizer import get_coordinates, city_from_name, draw_route_on_map
from algorithms.two_opt import distance, swap_reduces_distance, two_opt
from algorithms.simulated_annealing import simulated_annealing


#city_names = ["Алматы","Астана","Шымкент","Семей","Караганда"]
#real_cities = [city_from_name(name) for name in city_names]
#real_cities = [c for c in real_cities if c is not None]

#print([c.name for c in real_cities])

#greedy_route = greedy(real_cities)
#draw_route_on_map(real_cities, greedy_route, "route.html")

test_cities = [City(random.randint(0, 100), random.randint(0, 100), f"City_{i}") for i in range(50)]
test_route, test_history = genetic(test_cities)

test_total_route = total_distance(test_route)
test_two_opt = two_opt(test_route)
test_total_dist = total_distance(test_two_opt)
print("До 2-opt:", test_total_route)
print("После 2-opt:", test_total_dist)

#test_simul_route = total_distance(test_route)
#test_sim_ann = simulated_annealing(test_route)
#test_total_dist_sim = total_distance(test_sim_ann)
#print("До Sim_ann", test_total_route)
#print("После Sim_ann", test_total_dist_sim)



greedy_route = greedy(test_cities)
print("Greedy:", total_distance(greedy_route))

sa_route = simulated_annealing(greedy_route.copy())
print("SA:", total_distance(sa_route))

greedy_optimized = two_opt(greedy_route)
print("Greedy + 2-opt:", total_distance(greedy_optimized))





plt.figure(figsize=(10, 5))
plt.plot(test_history)
plt.title("Сходимость генетического алгоритма")
plt.xlabel("Поколение")
plt.ylabel("Длина маршрута")
plt.grid(True)
plt.show()