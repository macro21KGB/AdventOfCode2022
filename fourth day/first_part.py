
lines = []
with open("./input.txt") as file:
    lines = file.read().splitlines()

def get_range_from_string(string):
    return [int(i) for i in string.split("-")]
    
def isFullyContainedInRanges(range_1:list[int], range_2:list[int]):
    if range_1[0] >= range_2[0] and range_1[1] <= range_2[1]:
        return True
    
    elif range_2[0] >= range_1[0] and range_2[1] <= range_1[1]:
        return True

    return False

ranges_that_fully_contain_the_other = 0
for line in lines:
    pair_1, pair_2 = line.split(",")
    range_1 = get_range_from_string(pair_1)
    range_2 = get_range_from_string(pair_2)

    if isFullyContainedInRanges(range_1, range_2):
        ranges_that_fully_contain_the_other += 1

print(ranges_that_fully_contain_the_other)


