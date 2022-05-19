from game import Game
from player import Player
from string import whitespace
import csv

NUM_ROUNDS = 3
NUM_DICE_PER_PLAYER = 3
DICE_TYPES = (6, 6, 6)
MAX_PLAYERS = 2


def init_players():
    with open("highscores.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        prev_players = [row[0] for row in reader]
        print(prev_players)

    players = []
    
    while True:
        player_name = input("Enter player name: ")
        if (player_name == "") or \
           (any(ws in player_name for ws in whitespace)) or \
           (not (0 < len(player_name) <= 20)) or \
           (player_name in prev_players): # check if player name is valid
            print("Invalid player name. Try again.")
            continue
        else:
            players.append(Player(player_name))

        if len(players) == MAX_PLAYERS:
            print("Maximum number of players reached!")
            break

        continue_ = input("Enter another player? (y/n): ")
        if continue_ == "y":
            continue
        elif len(players) > 1:
            break
        else:
            print("You need at least 2 players to play!")

    print()
    return players


def main():
    players = init_players()
    game = Game(players, NUM_ROUNDS, NUM_DICE_PER_PLAYER, DICE_TYPES)
    print("Game started!")
    print()
    game.run()
    print("Game over! Thanks for playing!")


if __name__ == "__main__":
    main()

