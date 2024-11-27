import random

def create_pheromone_matrix(place_nums, start_pheromones):
    num_places =len(place_nums)
    #initialize a matrix with zeros
    pheromone_matrix = [[start_pheromones] * num_places for _ in range(num_places)]
    return pheromone_matrix

def update_pheromones(pheromone_matrix, cost, tabu_list):
    #count the quality of solution
    cost_per_move = cost/len(tabu_list)
    #add to each path which the ant pased based on tabu
    for a, b in zip(tabu_list, tabu_list[1:] + tabu_list[:1]):
        pheromone_matrix[a][b] += (1/cost_per_move)
    return 0

def count_path_cost(tabu_list, distance_matrix):
    cost = 0
    for a, b in zip(tabu_list, tabu_list[1:] + tabu_list[:1]):
        distance = distance_matrix[a][b]
        cost += distance
    return cost

def pick_next_place(tabu_list, pheromone_matrix, place_nums):
    place = 0
    unvisited = []
    current_place = tabu_list[-1]

    #create list of unvisited places
    for place in place_nums:
        if place not in tabu_list:
            unvisited.append(place)
    pheromones = []

    #create pheromone association list
    for place in unvisited:
        pheromones.append(pheromone_matrix[current_place][place])
    total = sum(pheromones)

    #convert pheromones into probability
    probability = []
    for pheromone in pheromones:
        probability.append(pheromone/total)
    #print(probability)

    #pick next place randomly with given probability
    next_place = random.choices(unvisited, weights=probability, k=1)[0]


    return next_place

def get_place_names(tabu_list, place_list):
    place_name_list = []
    #lookup dictionary of place names
    place_lookup = {item['place_num']: item['place'] for item in place_list}

    # Extract names of places in the order of place_nums_to_find
    place_name_list = [place_lookup[num] for num in tabu_list if num in place_lookup]

    return place_name_list
