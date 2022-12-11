from dataclasses import dataclass


@dataclass
class Monkey:
    id: int
    starting_items: list[int]
    divisible_number: int
    operation_value: (str, str)
    monkey_to_pass: (int, int)
    inspect_count: int = 0

    def remove_first_item(self):
        self.starting_items = self.starting_items[1:]
        
    def inspect(self):
        self.inspect_count += 1
        return self.starting_items[0]

    def get_inspection_count(self):
        return self.inspect_count
    
    def do_operation(self, item_worry_level: int):
        if self.operation_value[1].isnumeric():
            numerical_value = int(self.operation_value[1])
            match self.operation_value[0]:
                case "*":
                    return item_worry_level * numerical_value
                case "+":
                    return item_worry_level + numerical_value
        else:
            return item_worry_level * item_worry_level

    def take_item(self, item_to_take: int):
        self.starting_items.append(item_to_take)

        
    def test(self, stress_value: int) -> int:
        if stress_value % self.divisible_number == 0:
            return self.monkey_to_pass[0]

        return self.monkey_to_pass[1]

    @staticmethod
    def from_string(monkey_data: list[str]) -> 'Monkey':

        id: int = int(monkey_data[0].split(" ")[1].replace(":", ""))
        starting_items = [int(item) for item in monkey_data[1].split(": ")[1].split(", ")]
        operation = monkey_data[2].split("= ")[1].split(" ")[1:]
        divisible_by = int(monkey_data[3].split("by ")[1])
        monkey_to_pass = [ 
                      int(monkey_data[4].split("monkey ")[1]), 
                      int(monkey_data[5].split("monkey ")[1])
                ]

        return Monkey(id, starting_items, divisible_by, operation, monkey_to_pass)


    
    



