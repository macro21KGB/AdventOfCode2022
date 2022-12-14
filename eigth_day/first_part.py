matrix = []

with open("input.txt", "r") as f:
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

    visibile = False

    if check_if_tree_is_visibile_in_range(x, y, matrix, range(x-1, -1, -1), horizontal=False):
        visibile = True

    if check_if_tree_is_visibile_in_range(x, y, matrix, range(x+1, len(matrix)), horizontal=False):
        visibile = True
    
    if check_if_tree_is_visibile_in_range(x, y, matrix, range(y-1, -1, -1), horizontal=True):
        visibile = True

    if check_if_tree_is_visibile_in_range(x, y, matrix, range(y+1, len(matrix[0])), horizontal=True):
        visibile = True

    return visibile    

def check_if_tree_is_visibile_in_range(x: int, y: int, matrix: list[list[int]], target_range: range, horizontal: bool = True):
    """Check if the tree is visibile in a range"""
    all_trees : list[str] = []
    current_tree_value = int(matrix[x][y])

    if horizontal:
        for i in target_range:
            all_trees.append(int(matrix[x][i]))

        if len(all_trees) == 0:
            return False

        for target_tree in all_trees:
            if int(target_tree) >= int(matrix[x][y]):
                return False

        return True
    else:
        for i in target_range:
            all_trees.append(int(matrix[i][y]))

        if len(all_trees) == 0:
            return False

        for target_tree in all_trees:
            if int(target_tree) >= current_tree_value:
                return False
        
        return True



visibileTress = get_all_edge_visibile_trees(matrix)

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if isOnTheEdge(x,y,matrix):
            continue

        if isTreeVisibile(x,y,matrix):
            visibileTress.append((x,y))
            
print(len(visibileTress))

