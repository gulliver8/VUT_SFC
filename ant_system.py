import math
import os
import sys
import numpy as np
from distance_matrix import *
from process_input import *
from aco_functions import *
from interactive import *

def main():
    # parse arguments
    args = parse()
    # process file given as argument
    places_list = process_file(args.start_lat, args.start_lon, args.filename)
    if not places_list:
        exit("There was a problem with extracting data from the file, please check the file format.\n")
    else:
        print("Places data successfully extracted! List contains %d places\n" % len(places_list))
    num_places = len(places_list)
    place_nums = range(num_places)

    # create the distance matrix
    distance_matrix = create_distance_matrix(places_list)
    print_matrix(distance_matrix, "Distance matrix:")

    # dictionary of lists for each ant
    tabu_list = {}
    for ant in range(args.ants):
        list_name = f"ant_{ant}"
        tabu_list[list_name] = list()

    # cycle counter
    cycle = 0
    # create pheromone matrix with constant pheromone intensity between places
    pheromone_matrix = np.full((num_places,num_places),args.start)
    # create value and list of best path
    tabu_list["ant_best"] = list()
    best_cost = 0
    # create matrix for pheromone additions
    pheromone_addition_matrix = np.zeros((num_places, num_places), dtype='f')
    # create matrix for elitist aditions
    elite_matrix = np.zeros((num_places, num_places), dtype='f')
    while cycle < args.cycles:
        input("\nPress enter to start the next cycle\n")
        # reset list of each ant (add starting position) and matrices
        for ant in range(args.ants):
            list_name = f"ant_{ant}"
            tabu_list[list_name].clear()
            tabu_list[list_name].append(0)
        pheromone_addition_matrix.fill(0)
        if(args.mode == 'elite'):
            elite_matrix.fill(0)

        # construct the path for each ant
        for i in range(len(places_list) - 1):
            for ant in range(args.ants):
                # choose next place for and to visit based on pheromone matrix
                next_place = pick_next_place(tabu_list[f"ant_{ant}"], pheromone_matrix, place_nums)
                # add the place to list of visited places
                tabu_list[f"ant_{ant}"].append(next_place)

        # count the total cost of path for each ant (counting also way from end to start)
        for ant in range(args.ants):
            # calculate cost
            cost = count_path_cost(tabu_list[f"ant_{ant}"], distance_matrix, elite_matrix)
            print("Cost of ant %d in %d. cycle  is %.2f."% (ant+1, cycle+1, cost))
            print("Path of the ant:", tabu_list[f"ant_{ant}"])
            # calculate pheromone additions
            calculate_pheromones(pheromone_addition_matrix, distance_matrix, cost, tabu_list[f"ant_{ant}"], args.total, args.mode)
            # set new best solution if better was found
            if cost < best_cost or best_cost == 0:
                print("Solution improved: %.2f -> %.2f"% (best_cost, cost))
                best_cost = cost
                tabu_list["ant_best"] = tabu_list[f"ant_{ant}"].copy()

        # calculate the elitist matrix according to the best solution
        if(args.mode == "elite"):
            elite_matrix = update_elite(elite_matrix, tabu_list["ant_best"])
        # update pheromone matrix
        pheromone_matrix = update_pheromone_matrix(pheromone_matrix, pheromone_addition_matrix, elite_matrix, len(places_list), best_cost, args)
        print_matrix(pheromone_matrix,"Pheromone matrix")
        cycle += 1
    # show the final solution
    input("\nOptimization done, press enter to show the results.\n")
    print("Final solution is: ", tabu_list["ant_best"])
    print("With the cost %.2f "% best_cost)
    display_places(get_place_names(tabu_list["ant_best"], places_list))

main()



