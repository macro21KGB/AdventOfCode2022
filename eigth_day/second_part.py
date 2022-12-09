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
def generate_view_score(x : int,y : int, matrix : list[list[int]]) -> bool:
    """Check if the tree is visibile in a direction"""
    if isOnTheEdge(x,y,matrix):
        return True

    view_top = count_visibile_tree_of_view(x, y, matrix, range(x-1, -1, -1), horizontal=False)
    view_bottom = count_visibile_tree_of_view(x, y, matrix, range(x+1, len(matrix)), horizontal=False)
    view_left = count_visibile_tree_of_view(x, y, matrix, range(y-1, -1, -1), horizontal=True)
    view_right = count_visibile_tree_of_view(x, y, matrix, range(y+1, len(matrix[0])), horizontal=True)

    return view_top * view_bottom * view_left * view_right


 
def count_visibile_tree_of_view(x: int, y: int, matrix: list[list[int]], target_range: range, horizontal: bool = True) -> int:
    """Check if the tree is visibile in a range"""
    all_trees : list[str] = []
    tree_view_count = 0
    current_tree_value = int(matrix[x][y])

    if horizontal:
        for i in target_range:
            all_trees.append(int(matrix[x][i]))


        for target_tree in all_trees:
            if current_tree_value > int(target_tree):
                tree_view_count += 1
            if current_tree_value <= int(target_tree):
                tree_view_count += 1
                break

        return tree_view_count
    else:
        for i in target_range:
            all_trees.append(int(matrix[i][y]))

        for target_tree in all_trees:
            if current_tree_value > int(target_tree):
                tree_view_count += 1
            if current_tree_value <= int(target_tree):
                tree_view_count += 1
                break

        return tree_view_count



scores = []
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if isOnTheEdge(x,y,matrix):
            continue
            
        scores.append(generate_view_score(x,y,matrix))

print(max(scores))