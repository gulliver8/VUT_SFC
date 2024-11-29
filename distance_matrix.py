import math
import numpy as np

def create_distance_matrix(places_list):
    num_places = len(places_list)
    #initialize a matrix with zeros
    distance_matrix = [[0] * num_places for _ in range(num_places)]

    #calculate distances between each pair of places
    for i in range(num_places):
        for j in range(i, num_places):  #calculate only for upper triangle (matrix is symmetric)
            if i != j:
                distance = haversine_distance(places_list[i], places_list[j])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance  #symmetric

    return distance_matrix

def euclid_distance(place1,place2):
    lat1, lon1 = place1['y'], place1['x']
    lat2, lon2 = place2['y'], place2['x']

    lat_diff = (lat1-lat2)
    long_diff = (lon1-lon2)

    total_dist =  math.sqrt((lat_diff**2)+(long_diff**2)) #sqrt((x1-x2)^2+(y1-y2)^2)
    return round(total_dist,2)


def haversine_distance(place1, place2):
    lat1, lon1 = place1['y'], place1['x']
    lat2, lon2 = place2['y'], place2['x']

    #convert from degrees to radians
    lat1, lon1 = math.radians(lat1), math.radians(lon1)
    lat2, lon2 = math.radians(lat2), math.radians(lon2)

    #calculate haversine distance
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    #convert to km
    radius_of_earth_km = 6371.0
    distance = radius_of_earth_km * c
    return round(distance, 2)