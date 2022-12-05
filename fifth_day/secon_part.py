from typing import Optional, Tuple


def extract_movement_from_movement_string(movement_string: str) -> Tuple[int, int, int]:
    """Extracts the movement from a movement string.
    
    Args:
        movement_string: A string representing a movement.

    Returns:
        A tuple of the form (how_many_crates, from_pile_index, to_pile_index).
    """

    movement_string = movement_string.strip().split(" ")

    return int(movement_string[1]), int(movement_string[3]), int(movement_string[5])


class Crate():
    def __init__(self, id: str) -> None:
        self.id = id

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.id

class Pile():
    def __init__(self, idx_pile, array: Optional[list[Crate]] = None) -> None:
        if array is None:
            array = []

        self.array : list[Crate] = array
        self.idx_pile = idx_pile

    def push(self, crate: Crate) -> None:
        self.array.append(crate)

    def pop(self) -> Crate:
        return self.array.pop()

    def __str__(self) -> str:
        return f"Pile {self.idx_pile}: {self.array}"

    def get_top_crate(self) -> Crate:
        return self.array[-1]

class Crane():
    def __init__(self, piles : list[Crate]):
        self.piles = piles

    def move_crate(self, idx_pile_from: int, idx_pile_to: int, amount_to_move: int) -> None:
        piles_to_move = []
        for _ in range(amount_to_move):
            piles_to_move.insert(0, self.piles[idx_pile_from - 1].pop())
        
        for pile in piles_to_move:
            self.piles[idx_pile_to - 1].push(pile)

            
    def get_all_top_crates(self) -> list[Crate]:
        return [pile.get_top_crate() for pile in self.piles]

# Phase One: decode the drawing

input_piles = """
[B]                     [N]     [H]
[V]         [P] [T]     [V]     [P]
[W]     [C] [T] [S]     [H]     [N]
[T]     [J] [Z] [M] [N] [F]     [L]
[Q]     [W] [N] [J] [T] [Q] [R] [B]
[N] [B] [Q] [R] [V] [F] [D] [F] [M]
[H] [W] [S] [J] [P] [W] [L] [P] [S]
[D] [D] [T] [F] [G] [B] [B] [H] [Z]
 1   2   3   4   5   6   7   8   9
"""

layers = input_piles.split("\n")
piles : list[Pile] = []

piles.append(Pile(1, [Crate("D"), Crate("H"), Crate("N"), Crate("Q"), Crate("T"), Crate("W"), Crate("V"), Crate("B")]) )
piles.append(Pile(2, [Crate("D"), Crate("W"), Crate("B")]))
piles.append(Pile(3, [Crate("T"), Crate("S"), Crate("Q"), Crate("W"), Crate("J"), Crate("C")]))
piles.append(Pile(4, [Crate("F"), Crate("J"), Crate("R"), Crate("N"), Crate("Z"), Crate("T"), Crate("P")]))
piles.append(Pile(5, [Crate("G"), Crate("P"), Crate("V"), Crate("J"), Crate("M"), Crate("S"), Crate("T")]))
piles.append(Pile(6, [Crate("B"), Crate("W"), Crate("F"), Crate("T"), Crate("N")]))
piles.append(Pile(7, [Crate("B"), Crate("L"), Crate("D"), Crate("Q"), Crate("F"), Crate("H"), Crate("V"), Crate("N")]))
piles.append(Pile(8, [Crate("H"), Crate("P"), Crate("F"), Crate("R")]))
piles.append(Pile(9, [Crate("Z"), Crate("S"), Crate("M"), Crate("B"), Crate("L"), Crate("N"), Crate("P"), Crate("H")]))


# Phase Two: simulate the movement of the crate

movements = []
with open("./input_file.txt" ,"r") as f:
    movements = f.readlines()


crane = Crane(piles)

for movement in movements:
    amount_to_move, idx_pile_from, idx_pile_to = extract_movement_from_movement_string(movement)
    crane.move_crate(idx_pile_from, idx_pile_to, amount_to_move)

for crate in crane.get_all_top_crates():
    print(crate, end="")
