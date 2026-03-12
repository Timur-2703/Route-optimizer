import random
import matplotlib.pyplot as plt
from graph import City, total_distance
from algorithms.genetic import create_population, genetic
from algorithms.greedy import greedy
from visualizer import draw_on_ax
from map_visualizer import get_coordinates, city_from_name, draw_route_on_map


#city_names = ["Алматы","Астана","Шымкент","Семей","Караганда"]
#real_cities = [city_from_name(name) for name in city_names]
#real_cities = [c for c in real_cities if c is not None]

#print([c.name for c in real_cities])

#greedy_route = greedy(real_cities)
#draw_route_on_map(real_cities, greedy_route, "route.html")

test_cities = [City(random.randint(0, 100), random.randint(0, 100), f"City_{i}") for i in range(20)]
test_route, test_history = genetic(test_cities)

plt.figure(figsize=(10, 5))
plt.plot(test_history)
plt.title("Сходимость генетического алгоритма")
plt.xlabel("Поколение")
plt.ylabel("Длина маршрута")
plt.grid(True)
plt.show()