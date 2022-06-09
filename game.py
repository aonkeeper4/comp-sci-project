import csv
from player import Player
from dice import Dice
import time


class Game:
    def __init__(self,
                 players,
                 num_rounds=3,
                 num_dice=3,
                 dice_types=None,
                 *,
                 _no_print=False):
        self.players = players
        self.dice_types = (
            6, ) * num_dice if dice_types is None else dice_types

        if len(self.dice_types) != num_dice:
            raise ValueError("Number of dice must match number of dice types")

        self.dice = [Dice(dice_type) for dice_type in self.dice_types]
        self.num_rounds = num_rounds
        self.winner = None
        self.rounds_played = 0
        self.highscores = []
        self._no_print = _no_print

    def _print(self, *args, **kwargs):
        if self._no_print:
            return
        else:
            print(*args, **kwargs)
            time.sleep(0.5)

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
                if highest[0] == 6:
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
        for player in self.players:
            sorted_scores = sorted([player.score for player in self.players],
                                   reverse=True)
            if sorted_scores[0] == sorted_scores[1]:
                return None  # draw
            elif player.score == sorted_scores[0]:
                return player

    def run(self):
        # run the game
        while self.winner is None:
            for i in range(self.num_rounds):
                self.play_round()
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

        # add the winner to the highscores
        self.highscores.append(self.winner)
        self.print_highscores()
        self.save_highscores()

    def print_highscores(self):
        self.load_highscores()
        sorted_highscores = sorted(self.highscores,
                                   key=lambda player: player.score,
                                   reverse=True)
        self._print("Highscores:")
        for i in range(5):  # only print top 5
            player = sorted_highscores[i]
            self._print(f"{player.name}: {player.score} points")

        self._print()

    def save_highscores(self):
        with open("highscores.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["player", "score"])
            for player in self.highscores:
                writer.writerow([player.name, player.score])

    def load_highscores(self):
        with open("highscores.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                self.highscores.append(Player(row[0], int(row[1])))
