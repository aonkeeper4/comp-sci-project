from random import randint


# dice class to represent a dice
class Dice:
    def __init__(self, sides=6):
        self.sides = sides # set sides
        if not isinstance(sides, int): # can't have non-integer sides
            raise TypeError("Sides must be an integer")

    def roll(self): # roll dice
        return randint(1, self.sides)

    def __str__(self): # casts to str
        return f"d{self.sides}"
