# unit testing

from dice import Dice
from game import Game
from player import Player
import unittest # unit testing


# test the dice class
class DiceTest(unittest.TestCase):
    def test_dice_init_no_args(self): # tests sides property init w/ default value
        new_dice = Dice() # no sides value passed, should be 6
        self.assertEqual(new_dice.sides, 6)

    def test_dice_init_args_valid(self): # tests sides property init w/ value given
        new_dice = Dice(12) # dice.sides should be 12
        self.assertEqual(new_dice.sides, 12)

    def test_dice_init_args_invalid(self): # tests sides property init w/ invalid value
        with self.assertRaises(TypeError):
            new_dice = Dice("eleven") # this should raise an error (non-integer number of sides)

    def test_dice_roll(self): # tests dice .roll() method
        new_dice = Dice() # no params, dice.sides is 6
        rolled = new_dice.roll() # roll dice
        valid_range = range(1, 7) # should be in range 1 to 6
        self.assertIn(rolled, valid_range)

    def test_dice_str(self): # tests casting to str
        new_dice = Dice() # no params, dice.dides is 6
        dice_str = str(new_dice) # cast to str
        self.assertEqual(dice_str, "d6")


# test the player class
class PlayerTest(unittest.TestCase):
    def test_player_init_no_args(self): # tests player init w/ default value
        new_player = Player() # new_player.name should be "Player" and new_player.score should be 0
        self.assertEqual(new_player.name, "Player")
        self.assertEqual(new_player.score, 0)

    def test_player_init_args(self): # tests player init w/ name and starting score
        new_player = Player("Daniel", 3) # name should be "Daniel and score should be 3"
        self.assertEqual(new_player.name, "Daniel")
        self.assertEqual(new_player.score, 3)


# test game class
class GameTest(unittest.TestCase):
    def test_game_init(self): # tests game init
        players = [Player() for i in range(3)] # players
        new_game = Game(players, _no_print=True) # init with debug so no console spam
        self.assertEqual(new_game.players, players)
        self.assertEqual(new_game.winner, None)
        self.assertEqual(new_game.rounds_played, 0)
        self.assertEqual(new_game.highscores, [])

    def test_game_init_invalid(self): # tests game init w/ invalid dice type
        with self.assertRaises(ValueError):
            players = [Player() for i in range(3)]
            new_game = Game(players,
                            num_dice=4, # num_dice is 4 but only 3 dice are given in dice_types, should raise error
                            dice_types=(6, 6, 6),
                            _no_print=True)

    def test_game_run(self): # test game working
        players = [Player() for i in range(3)]
        new_game = Game(players, _no_print=True)
        new_game.run() # should run no errors

    def test_game_save_scores(self): # test saving highscores
        players = [Player() for i in range(3)]
        new_game = Game(players, _no_print=True)
        new_game.run() # runs game so we have highscores to save
        with open("highscores.csv", "r") as f:
            prev = f.read()
            new_game.save_highscores() # save highscores
            self.assertNotEqual(prev, f.read()) # checks that the file has changed (scores written)

    def test_game_load_scores(self): # test loading highscores from file
        players = [Player() for i in range(3)]
        new_game = Game(players, _no_print=True)
        new_game.load_highscores() # load highscores
        self.assertNotEqual(new_game.highscores, []) # loaded highscores so it shouldnt be empty


if __name__ == "__main__":
    unittest.main() # run tests
