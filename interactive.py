
def print_matrix(matrix, message):
    print(message)
    for row in matrix:
        print("\t".join(f"{value:.2f}" for value in row))

def display_places(list):
    print(" -> ".join(list))

