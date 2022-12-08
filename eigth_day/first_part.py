from enum import Enum
matrix = []


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

with open("test_input.txt", "r") as f:
    for line in f:
        matrix.append(list(line.strip()))

def isOnTheEdge(x,y, matrix):
    if x == 0 or x == len(matrix)-1:
        return True
    if y == 0 or y == len(matrix[0])-1:
        return True
    return False

def get_all_edge_visibile_trees(matrix):
    visibileTress = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if isOnTheEdge(x,y,matrix):
                visibileTress.append((x,y))
    return visibileTress

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
def isTreeVisibile(x : int,y : int, matrix : list[list[int]]) -> bool:
    """Check if the tree is visibile in a direction"""
    if isOnTheEdge(x,y,matrix):
        return True

    if check_direction_visibile_left_right(x,y,matrix):
        print("LEFT OR RIGHT APERTURE")
        return True

    if check_direction_visibile_up_down(x,y,matrix):
        print("UP OR DOWN APERTURE")
        return True

    print("NO APERTURE")
    return False    

def check_direction_visibile_up_down(x: int, y: int, matrix: list[list[int]], ) -> bool:
    """Check if the tree is visibile in the up and down direction"""
    all_trees = []
    for i in range(0, len(matrix)):
        all_trees.append(matrix[i][y])

    any_tree_is_higher = any([tree > matrix[x][y] for tree in all_trees])
    if any_tree_is_higher:
        return False
    
    return True


def check_direction_visibile_left_right(x: int, y: int, matrix: list[list[int]], ) -> bool:
    """Check if the tree is visibile in the left and right direction"""
    all_trees = []
    for i in range(0, len(matrix[0])):
        all_trees.append(matrix[x][i])
    any_tree_is_higher = any([tree >  matrix[x][y] for tree in all_trees])
    print(any_tree_is_higher)
    print(all_trees)
    print(matrix[x][y])

    if any_tree_is_higher:
        return False
    
    return True


visibileTress = get_all_edge_visibile_trees(matrix)

# for x in range(len(matrix)):
#     for y in range(len(matrix[0])):
#         if isOnTheEdge(x,y,matrix):
#             continue

#         if isTreeVisibile(x,y,matrix):
#             visibileTress.append((x,y))
            
# print(len(get_all_edge_visibile_trees(matrix)))
# print(len(visibileTress))
# print(visibileTress)

# TODO dividere left, right, up, down altrimenti in casi particolari non funziona
# TODO controllare se la tree è visibile in tutte le direzioni
isTreeVisibile(2,1,matrix)
print("----")
isTreeVisibile(2,2,matrix)
print("----")
isTreeVisibile(2,3,matrix)