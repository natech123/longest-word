from longest_word.game import Game
import string
import random


class TestGame:
    def test_game_initialization(self):
            # setup
            game = Game()

            # exercise

            grid = game.grid
            # verify
            assert type(grid) == list
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase
            # teardown

    def test_is_valid(self):
        new_game = Game()

        # test_grid = random.choices(string.ascii_uppercase, k = 9)
        test_grid = 'AECNFRHVG'
        test_word = 'FRANCE'

        new_game.grid = list(test_grid)

        assert new_game.is_valid(test_word) is True

        assert new_game.grid == list(test_grid)
