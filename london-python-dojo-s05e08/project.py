import collections
from haversine import haversine
from itertools import combinations
import requests

Friend = collections.namedtuple('Friend', ('name', 'coords', 'city_name'))

def get_coords(city_name):
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={city_name}".format(city_name=city_name))
    data = response.json()
    coords = data['results'][0]['geometry']['location']
    return (coords['lat'], coords['lng'])

def generate_friend(name, city_name):
    return Friend(
        name=name,
        coords=get_coords(city_name),
        city_name=city_name,
    )

list_of_friends = map(lambda x: generate_friend(*x), [
    ('John Doe', 'London'), 
    ('Peter Dojo', 'Bristol'), 
    ('Julius Dojo', 'Vilnius'), 
    ('Kane Dojo', 'Paris'), 
    ('Tom Dojo', 'Hanover'), 
    ('Pawel Dojo', 'Krakow'),
])

def distance_between(friend1, friend2):
    distance = haversine(friend1.coords, friend2.coords)
    return distance

def test_distance():
    print distance_between(list_of_friends[0], list_of_friends[1])

def distance_all(listofnames):
    distances = []
    for friend1, friend2 in combinations(listofnames, 2):
        distances.append(
            (
                "{friend1.name} ({friend1.city_name}) => {friend2.name} ({friend2.city_name})".format(friend1=friend2, friend2=friend1), 
                distance_between(friend1, friend2)
            )
        )
    return distances
    
def test_distance_all():
    assert len(distance_all(list_of_friends)) == len(list(combinations(list_of_friends, 2)))
    
def prtn(distances):
    distances.sort(key=lambda x:x[1])
    for dist in distances:
        print dist
        
distances = distance_all(list_of_friends)
prtn(distances)
