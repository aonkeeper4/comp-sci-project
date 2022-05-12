from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self, p):
        return randint(1, self.sides)
        