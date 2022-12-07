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
        return self.parent

    def get_total_size(self, total_sum: int) -> int:
        for item in self.items:
            if isinstance(item, Directory):
                total_sum += item.get_total_size(total_sum)
            else:
                total_sum += item.size

        return total_sum


    def view(self, indent_level: int):
       
        print("\t"*indent_level, end="")
        print(f"dir {self.name}")
        for item in self.items:
            if isinstance(item, Directory):
                item.view(indent_level + 1)
            else:
                print("\t"*indent_level, end="")
                print(f"  - {item.name}")

    def find(self,folder_name: str) -> 'Directory' :
        if folder_name == self.name:
            return self

        for item in self.items:
            if isinstance(item, Directory):
                return item.find(folder_name)
