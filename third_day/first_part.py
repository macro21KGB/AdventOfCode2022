from typing import Tuple

lines = []
with open("./input.txt") as f:
    lines = f.readlines()

lines = [lines.strip() for lines in lines]


# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def convert_item_type_to_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 64 + 26

def get_two_compartments(line: str) -> Tuple[list[str], list[str]]:
    sack = list(line)
    sack_length = len(sack)

    first_compartment = sack[:sack_length // 2]
    second_compartment = sack[sack_length // 2:]

    return first_compartment, second_compartment

def find_common_item_in_two_compartment(first_compartment: list[str], second_compartment: list[str]) -> str:
    for item in first_compartment:
        if item in second_compartment:
            return item

    return None

shared_items = [] 
for line in lines:
    compartment_1, compartment_2 = get_two_compartments(line)
    common_item = find_common_item_in_two_compartment(compartment_1, compartment_2)
    shared_items.append(common_item)


priority_values = list(map(convert_item_type_to_priority, shared_items))

print(sum(priority_values))