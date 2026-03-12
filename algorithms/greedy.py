def greedy(cities):
    unvisited = cities.copy()
    route = []
    current = unvisited.pop(0)
    route.append(current)

    while unvisited:
        nearest = None
        min_dist = float('inf')

        for city in unvisited:
            dist = current.distance_to(city)
            if dist < min_dist:
                min_dist = dist
                nearest = city
                pass

        route.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    return route