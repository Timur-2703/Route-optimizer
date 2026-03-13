import random
import math
from graph import total_distance

def get_neighbor(route):
    route_copy = route.copy()
    a = random.randint(0, len(route)-1)
    b = random.randint(0, len(route)-1)

    if a>b:
        a,b = b,a

    route_copy[a:b+1] = route_copy[a:b+1][::-1]

    return route_copy

def accept_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return True
    elif new_cost >= old_cost:
        return math.exp((-(new_cost - old_cost) / temperature)) >= random.random()

def cool_down(temperature, cooling_rate):
    return temperature * cooling_rate


def simulated_annealing(route):
    temperature = 100
    cooling_rate = 0.9999

    while temperature > 1:
        new_route = get_neighbor(route)
        old_cost = total_distance(route)
        new_cost = total_distance(new_route)


        if accept_probability(old_cost, new_cost, temperature):
            route = new_route

        temperature = cool_down(temperature, cooling_rate)
    return route
    