from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def calc_distance(city_from, city_to):
    geolocator = Nominatim(user_agent="Distance calc")
    location1 = geolocator.geocode(city_from)
    location2 = geolocator.geocode(city_to)
    coords1 = (location1.latitude, location1.longitude)
    coords2 = (location2.latitude, location2.longitude)
    print(f"{location1}, coordinates: {coords1}")
    print(f"{location2}, coordinates: {coords2}")
    return geodesic(coords1, coords2)


def main():
    city_from = input("Enter city from: ")
    city_to = input("Enter city to: ")
    print(f"Distance: {calc_distance(city_from, city_to)}")


if __name__ == "__main__":
    main()
