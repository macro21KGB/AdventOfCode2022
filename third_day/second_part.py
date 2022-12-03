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


def get_common_item_between_three_sacks(sack1 : list[str], sack2 : list[str], sack3 : list[str]) -> Tuple[str, int]:
    for item in sack1:
        if item in sack2 and item in sack3:
            return item, convert_item_type_to_priority(item)
    return None, None


badges_sack = []

while len(lines) > 0:
    group_of_three_sack =  [list(item) for item in lines[:3]]
    lines = lines[3:]

    badges_sack.append(get_common_item_between_three_sacks(group_of_three_sack[0], group_of_three_sack[1], group_of_three_sack[2]))


summed_priority = sum([item[1] for item in badges_sack])

print(summed_priority)