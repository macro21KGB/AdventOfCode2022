from monkey import Monkey

lines = []
with open("./input.txt") as f:
    lines = f.read().split("\n")


lines = [line.strip() for line in lines if line != ""]

monkeys = []
while len(lines) > 0:
    monkeys.append(Monkey.from_string(lines[:6]))
    lines = lines[6:]


current_monkey_index = 0
max_monkey_index = len(monkeys)
max_round = 20


for round_count in range(max_round):
    while current_monkey_index < max_monkey_index:
        current_monkey = monkeys[current_monkey_index]
        print(f"Monkey {current_monkey.id}: ")

        while len(current_monkey.starting_items) > 0:
            worry_level_item = current_monkey.inspect()
            print("Inspecting item with worry level: " + str(worry_level_item))
            worry_level_item = current_monkey.do_operation(worry_level_item)
            print("Worry item level increased to " + str(worry_level_item))

            worry_level_item = worry_level_item // 3
            print(f"Worry level divided by 3: {worry_level_item}")
            monkey_to_send_item_index = current_monkey.test(worry_level_item)
            print(f"SENDING ITEM TO MONKEY {monkey_to_send_item_index}")
            monkeys[monkey_to_send_item_index].take_item(worry_level_item)
            current_monkey.remove_first_item()
            print("--------------------")

        current_monkey_index += 1
    current_monkey_index = 0
        

counts = [(monkey.id, monkey.get_inspection_count()) for monkey in monkeys]

counts.sort(key=lambda item: item[1], reverse=True)

active_monkey_1 = counts[0][1]
active_monkey_2 = counts[1][1]

print(counts)
print(active_monkey_1 * active_monkey_2)
