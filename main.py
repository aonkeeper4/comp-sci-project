from game import Game
from player import Player
from string import whitespace
import csv

NUM_ROUNDS = 3
NUM_DICE_PER_PLAYER = 3
DICE_TYPES = (6, 6, 6)
MAX_PLAYERS = 2

def get_prev_players():
    with open("highscores.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        prev_players = [row[0] for row in reader]

    return prev_players

def player_name_valid(player_name):
    is_empty = player_name == ""
    contains_whitespace = any(ws in player_name for ws in whitespace)
    within_length_range = 0 < len(player_name) <= 20
    unique = player_name not in get_prev_players()

    return (
        (not is_empty) and \
        (not contains_whitespace) and \
        (within_length_range) and \
        (unique)
    )
    

def init_players():
    players = []
    
    while True:
        player_name = input("Enter player name: ")
        if not player_name_valid(player_name):
            print("Invalid player name")
            continue
        else:
            players.append(Player(player_name))

        if len(players) == MAX_PLAYERS:
            print("Maximum number of players reached!")
            break

        continue_ = input("Enter another player? (y/n): ")
        if continue_ == "y":
            continue
        elif len(players) >= 2:
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

