import xml.etree.ElementTree as ET
##TODO check input

def get_user_input():
    file = input("Enter input file name. It can be gpx or txt file.")
    start_y = input("Input starting place latitude (leave blank for first place from file to be start)")
    start_x = input("Input starting place longitude (leave blank for first place from file to be start)")
    n_ants = int(input("Input number of ants"))
    start_feromone = 0.1
    max_cycles = 20
    return file, start_y, start_x, n_ants, start_feromone, max_cycles

def process_file(start_y, start_x, file_path):
    # initialize an empty list to store the data and add start
    place_num = 0
    places_list = []
    if start_y != "":
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

