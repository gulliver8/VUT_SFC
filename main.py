import math
from distance_matrix import *
from process_input import *
from helping_functions import *

start_y, start_x, n_ants, start_feromone, max_cycles = get_user_input()

places_list = process_file(start_y, start_x)
if not places_list:
    exit("There was a problem wit extracting data from the file.")
else:
    print("Places data successfully extracted!")

# Create the distance matrix
distance_matrix = create_distance_matrix(places_list)
print("Number of places: " + str(len(places_list)))

#dictionary of lists for each ant
tabu_list = {}
for ant in range(n_ants):
    list_name = f"ant_{ant}"
    tabu_list[list_name] = list()
#cycle counter
cycle = 0

#init cycle
#reset lists, add starting place, reset best cost and best list
while cycle < max_cycles:
    #reset value and list of best path
    tabu_list["ant_best"] = list()
    best_cost = 0
    #reset list of each ant (add starting position)
    for ant in range(n_ants):
        list_name = f"ant_{ant}"
        tabu_list[list_name].clear()
        tabu_list[list_name].append(0)

    #set beggining feromone intesity between places -new matrix
    feromone_matrix = create_feromone_matrix(places_list, start_feromone)

    for i in range(len(places_list)-1):
        for ant in range(n_ants):
            #TODO
            next_place = pick_next_place(tabu_list[f"ant_{ant}"], feromone_matrix)
            tabu_list[f"ant_{ant}"].append(next_place)
    #for each ant count the total path cost (counting also end to start path)
    for ant in range(n_ants):
        #TODO
        cost = count_path_cost()
        #TODO
        update_feromones(feromone_matrix, cost, tabu_list[f"ant_{ant}"])
        # set new shortest path and length (compare with old one)
        if cost < best_cost:
            best_cost = cost
            tabu_list["ant_best"] = tabu_list[f"ant_{ant}"].copy()
    cycle += 1




