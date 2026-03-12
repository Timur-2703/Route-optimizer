import math 

class City:
    def __init__(self,x,y,name,lat=None,lon=None):
        self.x = x
        self.y = y
        self.name = name
        self.lat = lat
        self.lon = lon

    def distance_to(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
     
def total_distance(route):
    total = 0
    for i in range(len(route)):
        current = route[i]
        next_city = route[(i+1) % len(route)]
        total += current.distance_to(next_city)
    return total
