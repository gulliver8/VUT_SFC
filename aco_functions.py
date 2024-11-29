import random
import numpy as np

def calculate_pheromones(pheromone_addition_matrix, distance_matrix, cost, tabu_list, total_pheromones, mode):
    # add to each part of path which the ant passed
    for a, b in zip(tabu_list, tabu_list[1:] + tabu_list[:1]):
        # calculate based on selected mode
        if(mode == "density"):
            pheromone_addition_matrix[a,b] += total_pheromones
        elif(mode == "quantity"):
            pheromone_addition_matrix[a,b] += total_pheromones / distance_matrix[a,b]
        else:
            pheromone_addition_matrix[a,b] += (total_pheromones / cost)
    return 0

def update_pheromone_matrix(pheromone_matrix, pheromone_addition_matrix, elite_matrix, num_places, best, args):
    elite_const = args.total / best
    # add calculated pheromone additions to the total pheromone matrix
    result = (1-args.intensity)*pheromone_matrix + pheromone_addition_matrix
    if (args.mode == "elite"):
        result += elite_matrix * elite_const
    return result

def count_path_cost(tabu_list, distance_matrix, elite_matrix):
    cost = 0
    # count the cost of the ant's path handling succesive pairs of places from the list
    for a, b in zip(tabu_list, tabu_list[1:] + tabu_list[:1]):
        cost += distance_matrix[a,b]
        elite_matrix[a,b] += 1
    return cost

def pick_next_place(tabu_list, pheromone_matrix, place_nums):
    unvisited = []
    current_place = tabu_list[-1]
    pheromones = []
    # create list of unvisited places and list of their pheromone values
    for place in place_nums:
        if place not in tabu_list:
            unvisited.append(place)
            pheromones.append(pheromone_matrix[current_place][place])

    total = sum(pheromones)
    # convert pheromones into probability
    probability = []
    for pheromone in pheromones:
        probability.append(pheromone/total)

    # pick next place randomly with given probability
    next_place = random.choices(unvisited, weights=probability, k=1)[0]

    return next_place

def update_elite(elite_matrix, tabu_list):
    path_matrix = np.zeros_like(elite_matrix)
    # on the path of the solution add 1 to the matrix
    for a, b in zip(tabu_list, tabu_list[1:] + tabu_list[:1]):
        path_matrix[a,b] += 1

    #element-wise product of the elite_matrix and path_matrix -which marks the path of tabu_list
    product_matrix = path_matrix * elite_matrix
    return product_matrix


