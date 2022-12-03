from functools import reduce

total_list = []
with open("./lista_elfi.txt", "r") as file:
    total_list = file.read().split("\n\n")

total_sum = [reduce(lambda x, y: x + y, [int(x) for x in el.split("\n")]) for el in total_list]

total_sum.sort(reverse=True)

sum_of_first_3 = total_sum[0] + total_sum[1] + total_sum[2]

print(sum_of_first_3)

