import string
import random


class Game:
    """ Class for game instances"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase, k = 9)


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        combine = list(word) + self.grid

        return len(set(combine)) == 9
