
MIN_SIZE_OF_GROUP = 14

stream = ""
with open('./input.txt', 'r') as f:
    stream = f.read()

class CharacterGroup:
    def __init__(self, initial_group: list[str]) -> None:
        self.group = initial_group


    def get_group_size(self) -> int:
        return len(self.group)
    

    def isAllDifferentCharacters(self) -> bool:
        return len(set(self.group)) == len(self.group)
        

    def forward(self, next_character: str) -> None:
        self.group.append(next_character)
        self.group.pop(0)

    def __str__(self) -> str:
        return str(self.group)


group = CharacterGroup(list(stream[:MIN_SIZE_OF_GROUP]))
stream = stream[MIN_SIZE_OF_GROUP:]

current_char_index = 0

while current_char_index < len(stream) - 1:
    if group.isAllDifferentCharacters():
        print(group)
        print(current_char_index + MIN_SIZE_OF_GROUP)
        break

    group.forward(stream[current_char_index])
    current_char_index += 1
