from dataclasses import dataclass
from typing import Union

@dataclass
class Pair:
    pair1: list[Union[int, list[int]]]
    pair2: list[Union[int, list[int]]]



def make_string_to_array(string: str, start_index: int = 0) -> list[int]:
    temp_array = []

    while start_index < len(string):
       


print(make_string_to_array("[1,[2,3],4,5,6,7,8,9,10]"))