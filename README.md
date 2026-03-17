# 🗺️ Route Optimizer v2

> TSP solver comparing 5 optimization algorithms with benchmarks and interactive maps

[![Tests](https://github.com/Timur-2703/Route-optimizer/actions/workflows/tests.yml/badge.svg)](https://github.com/Timur-2703/Route-optimizer/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)

## Problem

The **Traveling Salesman Problem (TSP)** asks: given a list of cities, what is the shortest route that visits each city exactly once and returns to the starting city? It's an NP-hard problem — no known algorithm can solve it optimally in polynomial time. This makes it one of the most studied problems in computer science and operations research.

Real-world applications include logistics (Amazon delivery routes), chip design (circuit board wiring), DNA sequencing, and navigation (Google Maps).

## Approach

This project implements and compares **5 different algorithms**, each using a fundamentally different strategy:

| Algorithm | Strategy | Type |
|-----------|----------|------|
| **Greedy** | Always go to the nearest unvisited city | Constructive heuristic |
| **Genetic** | Evolve a population of routes through selection, crossover, and mutation | Evolutionary metaheuristic |
| **2-opt** | Iteratively remove crossing edges by reversing route segments | Local search |
| **Simulated Annealing** | Accept worse solutions with decreasing probability (inspired by metal cooling) | Probabilistic metaheuristic |
| **Ant Colony** | Simulate ants leaving pheromones on shorter paths | Swarm intelligence |

## Results

Benchmark on **50 random cities** (coordinates 0-100):

```
$ python3 main.py --benchmark --cities 50

Algorithm            Distance        Time (sec)
--------------------------------------------------
Greedy               733.43          0.0002
Genetic              1148.33         3.7337
Greedy + 2-opt       692.48          0.0017
Simulated Annealing  615.26          0.7318
Ant Colony           751.25          1.0682
```

### Key Findings

- **Simulated Annealing** produces the best routes — its ability to accept worse solutions early helps escape local minima
- **Greedy + 2-opt** offers the best speed/quality tradeoff — near-optimal results in milliseconds
- **Genetic algorithm** struggles with 50+ cities due to the enormous search space
- **Ant Colony** shows competitive results but requires parameter tuning
- **2-opt improves any starting route** — it reduced Greedy's distance by ~15% consistently

## Tech Stack

- **Python 3.12** — all algorithms implemented from scratch
- **matplotlib** — convergence graphs and route visualization
- **folium** — interactive maps with real city coordinates
- **geopy** — geocoding city names to coordinates
- **pytest** — unit tests for all algorithms
- **GitHub Actions** — CI/CD pipeline running tests on every push

## Project Structure

```
route_optimizer/
├── main.py                          # CLI with argparse + benchmark mode
├── graph.py                         # City class and distance calculations
├── visualizer.py                    # Route plotting with matplotlib
├── map_visualizer.py                # Interactive maps with folium
├── algorithms/
│   ├── greedy.py                    # Nearest neighbor heuristic
│   ├── genetic.py                   # Genetic algorithm with OX crossover
│   ├── two_opt.py                   # 2-opt local search optimization
│   ├── simulated_annealing.py       # SA with adaptive cooling
│   └── ant_colony.py                # ACO with pheromone trails
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py           # 11 tests covering all algorithms
├── conftest.py                      # pytest configuration
└── .github/workflows/tests.yml      # CI pipeline
```

## Getting Started

### Installation

```bash
git clone https://github.com/Timur-2703/Route-optimizer.git
cd Route-optimizer
pip install matplotlib folium geopy pytest
```

### Usage

**Run benchmark** (compare all algorithms):
```bash
python3 main.py --benchmark --cities 50
```

**Change city count:**
```bash
python3 main.py --benchmark --cities 100
```

**Run tests:**
```bash
pytest tests/ -v
```

## How Each Algorithm Works

### Greedy (Nearest Neighbor)
Starts at a random city and always moves to the closest unvisited city. Fast but produces suboptimal routes with many crossing edges.

### Genetic Algorithm
Creates a population of random routes. Each generation: the best routes are selected as parents, offspring are created through ordered crossover (OX), and random mutations shuffle the gene pool. Over 1000 generations, routes converge toward an optimum.

### 2-opt Local Search
Takes an existing route and improves it by finding pairs of edges that cross each other. When found, the segment between them is reversed, eliminating the crossing. Repeats until no more improvements exist.

### Simulated Annealing
Inspired by metallurgy — heating metal and cooling it slowly allows atoms to find optimal crystal positions. The algorithm starts "hot" (accepting many worse solutions to explore broadly) and "cools down" (gradually only accepting improvements). This prevents getting trapped in local minima.

### Ant Colony Optimization
Simulates how real ants find shortest paths using pheromone trails. Each ant builds a route probabilistically, preferring edges with more pheromones and shorter distances. After each generation, pheromones are deposited on good routes and evaporate from bad ones.

## Future Improvements

- [ ] C++ optimization module via pybind11 for critical paths
- [ ] Visualization of algorithm convergence comparison
- [ ] Support for real-world distances via OSRM API
- [ ] Web interface with interactive algorithm comparison

## License

MIT

## Author

**Timur** — CS student passionate about optimization and backend development.

- GitHub: [@Timur-2703](https://github.com/Timur-2703)