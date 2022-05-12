import csv
from player import Player
from dice import Dice


class Game:
    def __init__(self, players, num_rounds=3, dice_types=(6, 6, 6)):
        self.players = players
        self.dice = [Dice(dice_type) for _, dice_type in enumerate(dice_types)]
        self.num_rounds = num_rounds
        self.winner = None
        self.rounds_played = 0
        self.highscores = []

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
            print(f"{player.name} rolled {dice_str} and got {dice_score} points!")
            if highest[0] == highest[1]: # if two highest are equal
                print(f"{player.name} got a double!")
                if highest[0] == 6:
                    player.score += 6
                    print(f"Double six! A bonus 6 points were added to {player.name}'s score!")
                else:
                    player.score += 5
                    print(f"A bonus 5 points were added to {player.name}'s score!")

            print()

        self.rounds_played += 1

    def get_winner(self):
        # get the winner
        for player in self.players:
            sorted_scores = sorted([player.score for player in self.players], reverse=True)
            if sorted_scores[0] == sorted_scores[1]:
                return None # draw
            elif player.score == sorted_scores[0]:
                return player
        
    def run(self):
        # run the game
        while self.winner is None:
            for i in range(self.num_rounds):
                self.play_round()
                print(f"Scores for round {self.rounds_played}:")
                for player in self.players:
                    print(f"{player.name}: {player.score} points")
                
                print()
            
            # check if there is a winner
            self.winner = self.get_winner()
        
        # print the winner
        print(f"{self.winner.name} won with score {self.winner.score}!")
        print()

        # add the winner to the highscores
        self.highscores.append(self.winner)
        self.print_highscores()
        self.save_highscores()
    
    def print_highscores(self):
        self.load_highscores()
        sorted_highscores = sorted(self.highscores, key=lambda player: player.score, reverse=True)
        print("Highscores:")
        for player in sorted_highscores:
            print(f"{player.name}: {player.score} points")
        
        print()

    def save_highscores(self):
        with open("highscores.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["player", "score"])
            for player in self.highscores:
                writer.writerow([player.name, player.score])

    def load_highscores(self):
        with open("highscores.csv", "r") as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                self.highscores.append(Player(row[0], int(row[1])))
