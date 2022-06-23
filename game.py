from player import Player
from dice import Dice
import time # time.sleep
import csv # file handling


# game class to represent game
class Game:
    def __init__(self, players, num_rounds=3, num_dice=3,
                 dice_types=None, *, _no_print=False): # _no_print is a kw-only argument (has to be set explicitly by name)
        self.players = players # init players
        self.dice_types = (6, ) * num_dice if dice_types is None else dice_types # default dice_types

        if len(self.dice_types) != num_dice: # checks that num_dice is equal to the number of dice types
            raise ValueError("Number of dice must match number of dice types")

        self.dice = [Dice(dice_type) for dice_type in self.dice_types] # init dice

        # init properties
        self.num_rounds = num_rounds
        self.winner = None
        self.rounds_played = 0
        self.highscores = []
        self._no_print = _no_print

    def _print(self, *args, **kwargs): # for _no_print debug
        if self._no_print:
            return # dont do anything
        else:
            print(*args, **kwargs) # call print function
            time.sleep(0.5) # sleep half a second for readability

    def roll_dice(self):
        # roll dice
        return [dice.roll() for dice in self.dice]

    def play_round(self):
        # play a round
        for player in self.players:
            # roll dice
            dice = self.roll_dice()
            # get two highest
            highest = sorted(dice, reverse=True)[:2]
            dice_score = sum(highest)
            # add dice score to player score
            player.score += dice_score
            dice_str = ", a ".join(str(d) for d in dice)
            self._print(
                f"{player.name} rolled {dice_str} and got {dice_score} points!"
            )
            if highest[0] == highest[1]:  # if two highest are equal
                self._print(f"{player.name} got a double!")
                if highest[0] == 6: # if two highest = 6
                    player.score += 6
                    self._print(
                        f"Double six! A bonus 6 points were added to {player.name}'s score!"
                    )
                else:
                    player.score += 5
                    self._print(
                        f"A bonus 5 points were added to {player.name}'s score!"
                    )

            self._print()

        self.rounds_played += 1

    def get_winner(self):
        # get the winner
        sorted_scores = sorted( # sort scores from highest to lowest
            [player.score for player in self.players],
            reverse=True
        )
        if sorted_scores[0] == sorted_scores[1]:
            return None  # draw
            
        for player in self.players:
            if player.score == sorted_scores[0]:
                return player # return winning player

    def run(self):
        # run the game
        while self.winner is None: # while there is no winner
            for i in range(self.num_rounds):
                # do a round
                self.play_round()
                # display scores
                self._print(f"Scores for round {self.rounds_played}:")
                for player in self.players:
                    self._print(f"{player.name}: {player.score} points")

                self._print()

            # check if there is a winner
            self.winner = self.get_winner()
            if self.winner is None:
                self._print("Draw!")
                self._print()

        # print the winner
        self._print(f"{self.winner.name} won with score {self.winner.score}!")
        self._print()

        # add the winner to the highscores, display and save
        self.highscores.append(self.winner) # add winner
        self.print_highscores() # display highscores
        self.save_highscores() # save highscores

    def print_highscores(self): # display highscores
        self.load_highscores() # load highscores to print
        sorted_highscores = sorted(self.highscores,
                                   key=lambda player: player.score,
                                   reverse=True) # sort highscores
        self._print("Highscores:")
        for i in range(5): # only print top 5
            player = sorted_highscores[i]
            self._print(f"{player.name}: {player.score} points") # display score

        self._print()

    def save_highscores(self): # save highscores to file
        with open("highscores.csv", "w", newline="") as f: # write to file
            writer = csv.writer(f)
            writer.writerow(["player", "score"]) # header
            for player in self.highscores:
                writer.writerow([player.name, player.score]) # write scores

    def load_highscores(self): # load highscores from file
        with open("highscores.csv", "r") as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                self.highscores.append(Player(row[0], int(row[1]))) # build players from row
