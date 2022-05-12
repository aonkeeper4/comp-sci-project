class Player:
    def __init__(self, name="Player", starting_score=0):
        self.name = name
        self.score = starting_score

    def __str__(self):
        return self.name