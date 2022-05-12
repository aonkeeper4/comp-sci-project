from game import Game
from player import Player
from string import whitespace


def init_players():
    players = []
    while True:
        player_name = input("Enter player name: ")
        if (player_name == "") or \
           (any(ws in player_name for ws in whitespace)) or \
           (not (0 < len(player_name) <= 20)): # check if player name is valid
            print("Invalid player name. Try again.")
            continue
        else:
            players.append(Player(player_name))

        continue_ = input("Enter another player? (y/n): ")
        if continue_ == "y":
            continue
        elif len(players) > 1:
            break
        else:
            print("You need at least 2 players to play!")

    return players


def main():
    players = init_players()
    game = Game(players)
    print("Game started!")
    game.run()
    print("Game over! Thanks for playing!")


if __name__ == "__main__":
    main()

