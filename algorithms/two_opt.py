import math

def distance(city_a, city_b):
    return math.sqrt((city_b.x - city_a.x)**2 + (city_b.y- city_a.y)**2)


def swap_reduces_distance(route,i,j):
    old = distance(route[i-1], route[i]) + distance(route[j], route[j+1])
    new = distance(route[i-1], route[j])+ distance(route[i], route[j+1])
    if new < old:
        return new < old
    return False


def two_opt(route):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-1):
            for j in range(i+1, len(route)-1):
                if swap_reduces_distance(route,i,j):
                    route[i:j+1] = (route[i:j+1][::-1])
                    improved =True

    return route
