from geopy.geocoders import Nominatim
import folium
from graph import City

geolocator = Nominatim(user_agent ="route_optimazer")

def get_coordinates(city_name):
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None
    
def draw_route_on_map(cities, route, filename ="route.html"):
    start = cities[0]
    m = folium.Map(location =[start.lat, start.lon], zoom_start=6)

    for city in route:
        folium.Marker(
            location =[city.lat, city.lon],
            popup = city.name
        ).add_to(m)

    coords = [(city.lat, city.lon) for city in route]
    coords.append(coords[0])
    folium.PolyLine(coords, color = "blue", weight = 2.5).add_to(m)

    m.save(filename)
    print(f"Карта сохранена в {filename}")

def city_from_name(name):
    coords = get_coordinates(name)
    if coords:
        lat,lon = coords
        return City(x=lon, y=lat, name=name, lat=lat, lon=lon)
    return None
