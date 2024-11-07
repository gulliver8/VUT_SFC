def create_feromone_matrix(places_list, start_feromones):
    num_places = len(places_list)
    #initialize a matrix with zeros
    feromone_matrix = [[start_feromones] * num_places for _ in range(num_places)]
    return feromone_matrix

#TODO
def update_feromones(feromone_matrix, cost, tabu_list):
    #count the quality of solution ]
    #add to each path which the ant pased based on tabu
    return 0
#TODO
def count_path_cost():
    cost = 0
    return cost
#TODO
def pick_next_place(tabu_list, feromone_matrix):
    place = 0
    return place