import math
from distance_matrix import *
from process_input import *
from helping_functions import *

start_y, start_x, n_ants, start_pheromone, max_cycles = get_user_input()

places_list = process_file(start_y, start_x)
if not places_list:
    exit("There was a problem wit extracting data from the file.")
else:
    print("Places data successfully extracted!")

# Create the distance matrix
distance_matrix = create_distance_matrix(places_list)
for place in places_list:
    print(place)
print("Number of places: " + str(len(places_list)))

#dictionary of lists for each ant
tabu_list = {}
for ant in range(n_ants):
    list_name = f"ant_{ant}"
    tabu_list[list_name] = list()
#cycle counter
cycle = 0
place_nums = range(len(places_list))
print(place_nums)
#reset value and list of best path
tabu_list["ant_best"] = list()
best_cost = 0
#init cycle
while cycle < max_cycles:
    #reset list of each ant (add starting position)
    for ant in range(n_ants):
        list_name = f"ant_{ant}"
        tabu_list[list_name].clear()
        tabu_list[list_name].append(0)

    #set beggining pheromone intesity between places -new matrix
    pheromone_matrix = create_pheromone_matrix(places_list, start_pheromone)

    for i in range(len(places_list)-1):
        for ant in range(n_ants):
            #choose next place for and to visit based on pheromone matrix
            next_place = pick_next_place(tabu_list[f"ant_{ant}"], pheromone_matrix, place_nums)
            tabu_list[f"ant_{ant}"].append(next_place)

    #for each ant count the total path cost (counting also end to start path)
    for ant in range(n_ants):
        #count cost of path the ant has chosen
        cost = count_path_cost(tabu_list[f"ant_{ant}"], distance_matrix)
        print("Cost of ant ", ant, " in cycle", cycle, " is:", cost)
        print("Path of ant ", tabu_list[f"ant_{ant}"])
        #update pheromone values
        update_pheromones(pheromone_matrix, cost, tabu_list[f"ant_{ant}"])
        #set new shortest path and length (compare with old one)
        print(cost, best_cost)
        if cost < best_cost or best_cost == 0:
            best_cost = cost
            print("path before", tabu_list["ant_best"])
            tabu_list["ant_best"] = tabu_list[f"ant_{ant}"].copy()
            print("path before", tabu_list["ant_best"])
    print("Best solution after ", cycle, " cycles is:", tabu_list["ant_best"])
    print("With the cost: ", best_cost)
    cycle += 1
print("Final solution is: ", tabu_list["ant_best"])
print("With the cost: ", best_cost)




