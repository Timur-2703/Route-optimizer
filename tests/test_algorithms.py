import pytest
from graph import City, total_distance
from algorithms.greedy import greedy
from algorithms.genetic import genetic
from algorithms.two_opt import two_opt
from algorithms.simulated_annealing import simulated_annealing
from algorithms.ant_colony import ant_colony


# Подготовка — создаём города один раз, используем во всех тестах
@pytest.fixture
def cities():
    return [
        City(0, 0, "A"),
        City(10, 0, "B"),
        City(10, 10, "C"),
        City(0, 10, "D"),
        City(5, 5, "E"),
    ]


# ========== GREEDY ==========

def test_greedy_visits_all_cities(cities):
    route = greedy(cities)
    assert len(route) == len(cities)


def test_greedy_no_duplicates(cities):
    route = greedy(cities)
    assert len(route) == len(set(map(id, route)))


def test_greedy_positive_distance(cities):
    route = greedy(cities)
    assert total_distance(route) > 0


# ========== GENETIC ==========

def test_genetic_visits_all_cities(cities):
    route, history = genetic(cities)
    assert len(route) == len(cities)


def test_genetic_returns_history(cities):
    route, history = genetic(cities)
    assert len(history) > 0


# ========== 2-OPT ==========

def test_two_opt_improves_or_equal(cities):
    start_route = greedy(cities)
    before = total_distance(start_route)
    optimized = two_opt(start_route.copy())
    after = total_distance(optimized)
    assert after <= before


def test_two_opt_visits_all_cities(cities):
    start_route = greedy(cities)
    optimized = two_opt(start_route.copy())
    assert len(optimized) == len(cities)


# ========== SIMULATED ANNEALING ==========

def test_sa_visits_all_cities(cities):
    start_route = greedy(cities)
    route = simulated_annealing(start_route.copy())
    assert len(route) == len(cities)


def test_sa_positive_distance(cities):
    start_route = greedy(cities)
    route = simulated_annealing(start_route.copy())
    assert total_distance(route) > 0


# ========== ANT COLONY ==========

def test_aco_visits_all_cities(cities):
    route = ant_colony(cities)
    assert len(route) == len(cities)


def test_aco_positive_distance(cities):
    route = ant_colony(cities)
    assert total_distance(route) > 0


