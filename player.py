import pygame

class Player():
    def __init__(self, number):
        self.number = number
        self.symbol = ""

    def set_symbol(self):
        if not self.number:
            self.symbol = "X"
        else:
            self.symbol = "O"

    def get_symbol(self):
        return self.symbol

    def get_number(self):
        return self.number

