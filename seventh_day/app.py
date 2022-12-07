from typing import Union, Tuple
from classes import File, Directory

lines = []
from dataclasses import dataclass
with open("./test_input.txt", "r") as file:
    lines = file.readlines()

def parse_command(command: str) -> Tuple[str, str]:
    command = command.replace("$", "").strip()
    splitted_command = command.split(" ")

    command_only = splitted_command[0]

    arg = splitted_command[1] if len(splitted_command) > 1 else None

    return command_only, arg

def take_files_from_ls(lines: list[str], current_index: int, current_directory: Directory) -> Tuple[int, list]:
    items = []
    while not lines[current_index].startswith("$") and current_index < len(lines) - 1:
        first_part, second_part = parse_command(lines[current_index])
        

        if first_part.isalnum() and not first_part.startswith("dir"):
            items.append(File(second_part, int(first_part)))
        else:
            items.append(Directory(second_part, [], current_directory))

        current_index += 1
    

    return current_index, items


def isCommand(line: str):
    return line.startswith("$")

def execute_command(input: Tuple[str, str], current_directory: Directory, current_index: int):
    command = input[0]
    argument = input[1]

    match command:
        case "cd":
            if argument == "..":
                current_directory.go_up()
                return

            if current_directory.name != argument:

                nuova_directory = Directory(argument, [], current_directory)
                current_directory.add([nuova_directory])
                current_directory = nuova_directory
        case "ls":


    

current_index = 0
root_directory = Directory("/", [])
current_directory = root_directory

while current_index < len(lines):

    line : str = lines[current_index]

    if isCommand(line):
                command, argument = parse_command(line)
        execute_command((command, argument), current_directory)



    current_index += 1


print(root_directory)
