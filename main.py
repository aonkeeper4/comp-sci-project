from game import Game
from player import Player
from string import whitespace # whitespace detection
import csv # file handling


# init constants
NUM_ROUNDS = 3 # num rounds
NUM_DICE_PER_PLAYER = 3 # num dice per player
DICE_TYPES = (6, 6, 6) # the types of dice that each of the players roll
MAX_PLAYERS = 2 # maximumm players per game


# read prev players for player name validation
def get_prev_players():
    with open("highscores.csv", "r") as f:
        reader = csv.reader(f) # read from highscores.csv
        next(reader) # skip header
        prev_players = [row[0] for row in reader] # get players from file

    return prev_players


# function for test if player name valid
def player_name_valid(player_name):
    is_empty = player_name == "" # presence check
    contains_whitespace = any(ws in player_name for ws in whitespace) # whitespace bad
    within_length_range = 0 < len(player_name) <= 20 # length check
    unique = player_name not in get_prev_players() # is player name unique    

    # error messages
    if is_empty:
        print("Player name must not be empty")
        return

    if contains_whitespace:
        print("Player name must not contain whitespace")
        return

    if not within_length_range:
        print("Player name must be within 1 and 20 characters")
        return

    if not unique:
        print("This player already exists")
        return

    # if we have not returned here all checks have been passed
    return True


# function for init players
def init_players():
    players = []

    while True:
        player_name = input("Enter player name: ")
        if not player_name_valid(player_name): # validate player name
            continue
        else:
            players.append(Player(player_name)) # add player to players

        if len(players) == MAX_PLAYERS: # reached max number of players
            print("Maximum number of players reached!")
            break # stop

        continue_ = input("Enter another player? (y/n): ") # ask to continue
        if continue_ == "y": # keep entering players
            continue
        elif len(players) >= 2: # minimum 2 players
            break
        else: # only if asked to stop and not enough players
            print("You need at least 2 players to play!")

    print()
    return players


def main():
    players = init_players() # init players
    game = Game(players, NUM_ROUNDS, NUM_DICE_PER_PLAYER, DICE_TYPES) # init game
    print("Game started!")
    print()
    game.run() # play game
    print("Game over! Thanks for playing!")


if __name__ == "__main__":
    main() # run the program
