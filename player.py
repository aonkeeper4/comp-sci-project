# player class to represent a player
class Player:
    def __init__(self, name="Player", starting_score=0):
        # init properties
        self.name = name
        self.score = starting_score

    def __str__(self): # casting to str
        return self.name