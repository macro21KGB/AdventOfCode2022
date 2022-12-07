from typing import Union, Tuple

lines = []
from dataclasses import dataclass
with open("./test_input.txt", "r") as file:
    lines = file.readlines()


@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    items: list[Union[File,'Directory']]
    parent: 'Directory' = None

    def add(self, *items):
        for item in items:
            self.items.append(item)

    def go_up(self):
        return self.parent

    def find(self,folder_name: str) -> 'Directory' :
        if folder_name == self.name:
            return self

        for item in self.items:
            if item is Directory:
                item.find(folder_name)

        return None

class ChangeCommand:
    def __init__(self):
        self.directory_stack = []
    
    def get_current_directory(self):
        return self.directory_stack[-1]

    def __remove_directory(self):
        self.directory_stack.pop()

    def __str__(self):
        return f"Current Directory: {self.get_current_directory()} Directories: {self.directory_stack}"


def parse_command(command: str) -> Tuple[str, str]:
    command = command.replace("$", "").strip()
    splitted_command = command.split(" ")

    command_only = splitted_command[0]

    arg = splitted_command[1] if len(splitted_command) > 1 else None

    return command_only, arg

def take_files_from_ls(lines, current_index, current_directory) -> Tuple[int, list]:
    items = []
    while not lines[current_index].startswith("$") and current_index < len(lines) - 1:
        first_part, second_part = parse_command(lines[current_index])
        

        if first_part.isalnum() and not first_part.startswith("dir"):
            print(first_part)
            print(second_part)
            items.append(File(second_part, first_part))
        else:
            items.append(Directory(second_part, [], current_directory))

        current_index += 1
    

    return current_index, items

current_index = 0

root_directory = Directory("/", [])
current_directory = root_directory
while current_index < len(lines):

    command, arg = parse_command(lines[current_index])
        
    match command:
        case "cd":
            if arg == "..":
                current_directory = current_directory.go_up()
            
            found_folder = root_directory.find(arg)
            if found_folder is None:
                current_directory.add(Directory(arg, [], current_directory))
            else:
                current_directory = found_folder

        case "ls":
            current_index += 1
            current_index , items_inside_folder = take_files_from_ls(lines, current_index, current_directory)
            current_directory.add(items_inside_folder)
 
    current_index += 1
    
    
