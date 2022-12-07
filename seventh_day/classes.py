from dataclasses import dataclass
from typing import Union, Tuple

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    items: list[Union[File,'Directory']]
    parent: 'Directory' = None

    def add(self, new_items: list['Directory']):
        for item in new_items:
            item.parent = self
            self.items.append(item)

    def go_up(self):
        if self.parent is None:
            return self
        
        return self.parent

    def get_total_size(self, total_sum: int) -> int:
        for item in self.items:
            if isinstance(item, File):
                total_sum += item.size
            else:
                total_sum += item.get_total_size(total_sum)
        
        return total_sum

    def get_all_directories_below_me(self, directories: list['Directory']) -> list['Directory']:
        for item in self.items:
            if isinstance(item, Directory):
                directories.append(item)
                item.get_all_directories_below_me(directories)

        return directories
        

    def view(self, indent_level: int):
       
        print("\t"*indent_level, end="")
        print(f"{self.name} (dir)")
        for item in self.items:
            if isinstance(item, Directory):
                item.view(indent_level + 1)
            else:
                print("\t"*indent_level, end="")
                print(f"  - {item.name} ({item.size} bytes)")

    def find(self,folder_name: str) -> 'Directory' :
        if self.name == folder_name:
            return self

        for item in self.items:
            if isinstance(item, Directory):
                found_folder = item.find(folder_name)
                if found_folder is not None:
                    return found_folder

        return None