from enum import Enum

POINT_FOR_LOSE = 0
POINT_FOR_DRAW = 3
POINT_FOR_WIN = 6

class Outcome(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3

    def symbol_to_outcome(symbol):
    
        match symbol:
            case "X":
                return Outcome.LOSE
            case "Y":
                return Outcome.DRAW
            case "Z":
                return Outcome.WIN

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
    def __init__(self, enemyShape : Shape, outcome: Outcome):
        self.enemyShape = enemyShape
        self.outcome = outcome
        self.myShape = self.calculate_my_shape()


    def calculate_my_shape(self):
        match self.outcome:
            case Outcome.WIN:
                if self.enemyShape == Shape.ROCK:
                    return Shape.PAPER
                elif self.enemyShape == Shape.PAPER:
                    return Shape.SCISSORS
                elif self.enemyShape == Shape.SCISSORS:
                    return Shape.ROCK
            case Outcome.LOSE:
                if self.enemyShape == Shape.ROCK:
                    return Shape.SCISSORS
                elif self.enemyShape == Shape.PAPER:
                    return Shape.ROCK
                elif self.enemyShape == Shape.SCISSORS:
                    return Shape.PAPER
            case Outcome.DRAW:
                return self.enemyShape

    def calculate_result(self):
        if self.myShape == self.enemyShape:
            return self.myShape.value + POINT_FOR_DRAW
        elif self.myShape == Shape.ROCK and self.enemyShape == Shape.SCISSORS:
            return self.myShape.value + POINT_FOR_WIN
        elif self.myShape == Shape.PAPER and self.enemyShape == Shape.ROCK:
            return self.myShape.value + POINT_FOR_WIN
        elif self.myShape == Shape.SCISSORS and self.enemyShape == Shape.PAPER:
            return self.myShape.value + POINT_FOR_WIN
        else:
            return self.myShape.value + POINT_FOR_LOSE

    def __str__(self) -> str:
        return f"Round: {self.myShape} vs {self.enemyShape}"

    def __repr__(self) -> str:
        return self.__str__()

rounds : list[Round] = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")

        outcome_to_obtain = Outcome.symbol_to_outcome(line[1])
        enemyShape = Shape.symbol_to_shape(line[0])
        rounds.append(Round(enemyShape, outcome_to_obtain))


scores = [round.calculate_result() for round in rounds]

print(sum(scores))