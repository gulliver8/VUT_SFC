import xml.etree.ElementTree as ET
import argparse

def parse():
    parser = argparse.ArgumentParser(description="Parse arguments for ACO")

    #add arguments
    parser.add_argument("filename", help="Txt or gpx file to process.")
    parser.add_argument("--ants", type=int, default=10, help="Number of ants.")
    parser.add_argument("--start_lat", type=float, default=None,help="Number of ants.")
    parser.add_argument("--start_lon", type=float, default=None, help="Number of ants.")
    parser.add_argument("--cycles", type=int, default=10, help="Number of ants.")
    parser.add_argument("--intensity", type=float, default=0.1, help="Intensity of evaporation of the pheromones.")
    parser.add_argument("--total", type=int, default=100, help="Total amount of pheromones for an ant.")
    parser.add_argument("--start", type=float, default=1, help="Starting value for pheromone matrix.")

    return parser.parse_args()

def process_file(start_y, start_x, file_path):
    # initialize an empty list to store the data and add start
    place_num = 0
    places_list = []
    if start_y is not None:
        places_list.append({
            'place_num': 0,
            'place': 'start',
            'y': float(start_y.strip()),
            'x': float(start_x.strip())
        })
        place_num += 0;
    #check if the file is gpx or txt
    if file_path.endswith(".gpx"):
        tree = ET.parse(file_path)
        root = tree.getroot()
        for place in root:
            lat = float(place.get('lat'))
            lon = float(place.get('lon'))
            for place_name in place:
                name = place_name.text

            places_list.append({
                'place_num': place_num,
                'place': name.strip()[:20] ,
                'y': lat,
                'x': lon
            })
            place_num += 1
        return places_list
    elif file_path.endswith(".txt"):
        with open(file_path, 'r') as file:
            for line in file:
                # strip any extra whitespace and split the line by tabs
                parts = line.strip().split('\t')
                # check if line contains the expected four parts
                if len(parts) == 3:
                    # extract and parse the data
                    lat_coord = float(parts[0].strip())
                    long_coord = float(parts[1].strip())
                    name = parts[2].strip()[:20]

                    # add the parsed data as a dictionary to the list
                    places_list.append({
                        'place_num': place_num,
                        'place': name,
                        'y': lat_coord,
                        'x': long_coord
                    })
                place_num += 1
        return places_list
    else:
        return []

