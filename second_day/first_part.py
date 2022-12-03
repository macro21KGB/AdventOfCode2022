from enum import Enum

POINT_FOR_LOSE = 0
POINT_FOR_DRAW = 3
POINT_FOR_WIN = 6

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def symbol_to_shape(symbol):
        
        match symbol:
            case "A" | "X":
                return Shape.ROCK
            case "B" | "Y":
                return Shape.PAPER
            case "C" | "Z":
                return Shape.SCISSORS

class Round():
    def __init__(self, myShape : Shape, otherShape: Shape):
        self.myShape = myShape
        self.otherShape = otherShape

    def calculate_result(self):
        if self.myShape == self.otherShape:
            return self.myShape.value + POINT_FOR_DRAW
        elif self.myShape == Shape.ROCK and self.otherShape == Shape.SCISSORS:
            return self.myShape.value + POINT_FOR_WIN
        elif self.myShape == Shape.PAPER and self.otherShape == Shape.ROCK:
            return self.myShape.value + POINT_FOR_WIN
        elif self.myShape == Shape.SCISSORS and self.otherShape == Shape.PAPER:
            return self.myShape.value + POINT_FOR_WIN
        else:
            return self.myShape.value + POINT_FOR_LOSE

    def __str__(self) -> str:
        return f"Round: {self.myShape} vs {self.otherShape}"

    def __repr__(self) -> str:
        return self.__str__()

rounds : list[Round] = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")

        myShape = Shape.symbol_to_shape(line[1])
        otherShape = Shape.symbol_to_shape(line[0])
        rounds.append(Round(myShape, otherShape))


scores = [round.calculate_result() for round in rounds]

print(sum(scores))