from typing import Union, Tuple
from classes import File, Directory

lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()

def parse_command(command: str) -> Tuple[str, str]:
    command = command.replace("$", "").strip()
    splitted_command = command.split(" ")

    command_only = splitted_command[0]

    arg = splitted_command[1] if len(splitted_command) > 1 else None

    return command_only, arg

def take_files_from_ls(lines: list[str], current_index: int, current_directory: Directory) -> Tuple[int, list]:
    items = []
    while not lines[current_index].startswith("$") and lines[current_index] != "###":
        first_part, second_part = parse_command(lines[current_index])
        

        if first_part.isalnum() and not first_part.startswith("dir"):
            items.append(File(second_part, int(first_part)))
        else:
            items.append(Directory(second_part, [], current_directory))

        current_index += 1
    

    return current_index - 1, items

def main():
    root_dir = Directory("/", [], None)
    current_directory = root_dir
    current_index = 0

    while current_index < len(lines):

        command, argument = parse_command(lines[current_index])

        if command == "cd":
            if argument == "..":
                current_directory = current_directory.go_up()
            else:
                found_directory = root_dir.find(argument)
                if found_directory is None:
                    print("No such directory")
                    current_directory = current_directory.go_up()
                else:
                    current_directory = found_directory

        elif command == "ls":
            current_index, items = take_files_from_ls(lines, current_index + 1, current_directory)
            current_directory.add(items)
        current_index += 1


    final_sum = 0
    for dir in root_dir.get_all_directories_below_me([]):
        size_of_dir = dir.get_total_size(0)
        if size_of_dir <= 1000000:
            final_sum += size_of_dir

    print(final_sum)

if __name__ == "__main__":
    main()