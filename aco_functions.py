import random

def create_pheromone_matrix(place_nums, start_pheromones):
    num_places =len(place_nums)
    #initialize a matrix with zeros
    pheromone_matrix = [[start_pheromones] * num_places for _ in range(num_places)]
    return pheromone_matrix


def calculate_pheromones(pheromone_addition_matrix, distance_matrix, cost, tabu_list, total_pheromones, mode):
    #add to each path which the ant pased based on tabu
    for a, b in zip(tabu_list, tabu_list[1:] + tabu_list[:1]):
        if(mode == "density"):
            pheromone_addition_matrix[a][b] += total_pheromones
        elif(mode == "quantity"):
            pheromone_addition_matrix[a][b] += total_pheromones/distance_matrix[a][b]
        else:
            pheromone_addition_matrix[a][b] += (total_pheromones / cost)
    return 0

def update_pheromone_matrix(pheromone_matrix, pheromone_addition_matrix, pher_evap_intensity, num_places):
    for a in range(num_places):
        for b in range(num_places):
            pheromone_matrix[a][b] = (1-pher_evap_intensity)*pheromone_matrix[a][b] + pheromone_addition_matrix[a][b]
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

