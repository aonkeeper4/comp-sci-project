from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        if not isinstance(sides, int):
            raise TypeError("Sides must be an integer")

    def roll(self):
        return randint(1, self.sides)

    def __str__(self):
        return f"d{self.sides}"
