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
def treeIsVisibileInADirection(x,y, matrix):
    if look_direction(x,y, matrix, Direction.UP):
        print("UP")
        return True
        
    if look_direction(x,y, matrix, Direction.DOWN):
        print("DOWN")
        return True

    if look_direction(x,y, matrix, Direction.LEFT):
        print("LEFT")
        return True

    if look_direction(x,y, matrix, Direction.RIGHT):
        print("RIGHT")
        return True
    return False


def look_direction(x,y, matrix, direction):
    current_tree = matrix[x][y]
    
    match direction:
        case Direction.UP:
            for i in range(x-1, 0, -1):
                target_tree = matrix[i][y]
                if target_tree < current_tree:
                    return True
            return False
        case Direction.DOWN:
            for i in range(x+1, len(matrix)):
                target_tree = matrix[i][y]
                if target_tree < current_tree:
                    return True
            return False
        case Direction.LEFT:
            for i in range(y-1, 0, -1):
                target_tree = matrix[x][i]
                if target_tree < current_tree:
                    return True
            return False
        case Direction.RIGHT:
            for i in range(y+1, len(matrix[0])):
                target_tree = matrix[x][i]
                if target_tree < current_tree:
                    return True
            return False
            

visibileTress = get_all_edge_visibile_trees(matrix)

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if isOnTheEdge(x,y,matrix):
            continue

        if treeIsVisibileInADirection(x,y,matrix):
            visibileTress.append((x,y))
            
print(len(get_all_edge_visibile_trees(matrix)))
print(len(visibileTress))