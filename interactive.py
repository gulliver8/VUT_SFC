def print_matrix(matrix, message):
    # print matrix in a proper matrix format
    print(message)
    for row in matrix:
        print("\t".join(f"{value:.2f}" for value in row))

def get_place_names(tabu_list, place_list):
    place_name_list = []
    #lookup dictionary of place names
    place_lookup = {item['place_num']: item['place'] for item in place_list}
    # Extract names of places in the order of place_nums_to_find
    place_name_list = [place_lookup[num] for num in tabu_list if num in place_lookup]
    return place_name_list


def display_places(list):
    #display places as a path with arrows
    print(" -> ".join(list))

