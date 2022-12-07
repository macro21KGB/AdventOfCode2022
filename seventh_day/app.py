from typing import Union

lines = []
from dataclasses import dataclass
with open("./input.txt", "r") as file:
    lines = file.readlines()


@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    items: list

    def add(self, item):
        self.items.append(item)



class ChangeCommand:
    def __init__(self):
        self.directory_stack = []
    
    def get_current_directory(self):
        return self.directory_stack[-1]

    def __remove_directory(self):
        self.directory_stack.pop()

    def go(self,path: str):

        match path:
            case "..":
                self.__remove_directory()
            case _:
                self.directory_stack.append(path)
    def __str__(self):
        return f"Current Directory: {self.get_current_directory()} Directories: {self.directory_stack}"

ccommand = ChangeCommand()

def parse_command(command: str):
    command = command.replace("$", "").strip()
    splitted_command = command.split(" ")

    command_only = splitted_command[0]

    arg = splitted_command[1] if len(splitted_command) > 1 else None

    return splitted_command[0], arg

def take_files_from_ls(lines, current_index) -> int:
    while not lines[current_index].startswith("$") and current_index < len(lines) - 1:
        splitted_line = lines[current_index].split(" ")

        if splitted_line[0].isalnum() and splitted_line[0].startswith("dir"):
            directory_map[ccommand.get_current_directory()].add(File(splitted_line[1].strip(), splitted_line[0]))
        current_index += 1

    return current_index

current_index = 0
directory_map = {}
while current_index < len(lines):
    if lines[current_index].startswith("$"):
        command, arg = parse_command(lines[current_index])
            
        match command:
            case "cd":
                ccommand.go(arg)
                directory_added = directory_map.get(arg)
                if directory_added is None:
                    directory_map[arg] = Directory(arg, [])
            case "ls":
                # print all lines without $
                current_index += 1
                current_index = take_files_from_ls(lines, current_index)
     
    current_index += 1
    
    
print(directory_map["/"])
