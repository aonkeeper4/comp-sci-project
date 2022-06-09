import unittest
from dice import Dice
from game import Game
from player import Player


class DiceTest(unittest.TestCase):
    def test_dice_init_no_args(self):
        new_dice = Dice()
        self.assertEqual(new_dice.sides, 6)

    def test_dice_init_args_valid(self):
        new_dice = Dice(12)
        self.assertEqual(new_dice.sides, 12)

    def test_dice_init_args_invalid(self):
        with self.assertRaises(TypeError):
            new_dice = Dice("eleven")

    def test_dice_roll(self):
        new_dice = Dice()
        rolled = new_dice.roll()
        valid_range = range(1, 7)  # 1 to 6
        self.assertIn(rolled, valid_range)

    def test_dice_str(self):
        new_dice = Dice()
        dice_str = str(new_dice)
        self.assertEqual(dice_str, "d6")


class PlayerTest(unittest.TestCase):
    def test_player_init_no_args(self):
        new_player = Player()
        self.assertEqual(new_player.name, "Player")
        self.assertEqual(new_player.score, 0)

    def test_player_init_args(self):
        new_player = Player("Daniel", 3)
        self.assertEqual(new_player.name, "Daniel")
        self.assertEqual(new_player.score, 3)


class GameTest(unittest.TestCase):
    def test_game_init(self):
        players = [Player() for i in range(3)]
        new_game = Game(players, _no_print=True)
        self.assertEqual(new_game.players, players)
        self.assertEqual(new_game.winner, None)
        self.assertEqual(new_game.rounds_played, 0)
        self.assertEqual(new_game.highscores, [])

    def test_game_init_invalid(self):
        with self.assertRaises(ValueError):
            players = [Player() for i in range(3)]
            new_game = Game(players,
                            num_dice=4,
                            dice_types=(6, 6, 6),
                            _no_print=True)

    def test_game_run(self):
        players = [Player() for i in range(3)]
        new_game = Game(players, _no_print=True)
        new_game.run()

    def test_game_save_scores(self):
        players = [Player() for i in range(3)]
        new_game = Game(players, _no_print=True)
        new_game.run()
        with open("highscores.csv", "r") as f:
            prev = f.read()
            new_game.save_highscores()
            self.assertNotEqual(prev, f.read())

    def test_game_load_scores(self):
        players = [Player() for i in range(3)]
        new_game = Game(players, _no_print=True)
        new_game.load_highscores()
        self.assertNotEqual(new_game.highscores, [])


if __name__ == "__main__":
    unittest.main()
