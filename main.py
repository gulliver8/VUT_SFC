import math
import os
import sys
from distance_matrix import *
from process_input import *
from aco_functions import *
from interactive import *

def main():
    args = parse()

    places_list = process_file(args.start_lat, args.start_lon, args.filename)
    if not places_list:
        exit("There was a problem with extracting data from the file, please check the file format.\n")
    else:
        print("Places data successfully extracted! List contains %d places\n" % len(places_list))
    place_nums = range(len(places_list))
    # Create the distance matrix
    distance_matrix = create_distance_matrix(places_list)
    print_matrix(distance_matrix, "Distance matrix:")

    # dictionary of lists for each ant
    tabu_list = {}
    for ant in range(args.ants):
        list_name = f"ant_{ant}"
        tabu_list[list_name] = list()

    # cycle counter
    cycle = 0
    # set beggining pheromone intesity between places -new matrix
    pheromone_matrix = create_pheromone_matrix(places_list, args.start)
    # reset value and list of best path
    tabu_list["ant_best"] = list()
    best_cost = 0
    # init cycle
    while cycle < args.cycles:
        input("\nPress enter to start the next cycle\n")
        # reset list of each ant (add starting position)
        for ant in range(args.ants):
            list_name = f"ant_{ant}"
            tabu_list[list_name].clear()
            tabu_list[list_name].append(0)
        #create matreix to store pheromone additions
        pheromone_addition_matrix = create_pheromone_matrix(places_list, float(0))


        for i in range(len(places_list) - 1):
            for ant in range(args.ants):
                # choose next place for and to visit based on pheromone matrix
                next_place = pick_next_place(tabu_list[f"ant_{ant}"], pheromone_matrix, place_nums)
                tabu_list[f"ant_{ant}"].append(next_place)

        # for each ant count the total path cost (counting also end to start path)
        for ant in range(args.ants):
            # count cost of path the ant has chosen
            cost = count_path_cost(tabu_list[f"ant_{ant}"], distance_matrix)
            print("Cost of ant %d in %d. cycle  is %.2f."% (ant+1, cycle+1, cost))
            print("Path of the ant:", tabu_list[f"ant_{ant}"])
            # update pheromone values
            calculate_pheromones(pheromone_addition_matrix, cost, tabu_list[f"ant_{ant}"], args.total)
            # set new shortest path and length (compare with old one)
            if cost < best_cost or best_cost == 0:
                print("Solution improved: %.2f -> %.2f"% (best_cost, cost))
                best_cost = cost
                tabu_list["ant_best"] = tabu_list[f"ant_{ant}"].copy()
        update_pheromone_matrix(pheromone_matrix,pheromone_addition_matrix,args.intensity,len(places_list))
        print_matrix(pheromone_matrix,"Pheromone matrix")
        cycle += 1
    input("\nOptimization done, press enter to show the results.\n")
    print("Final solution is: ", tabu_list["ant_best"])
    print("With the cost %.2f "% best_cost)
    display_places(get_place_names(tabu_list["ant_best"], places_list))

main()



