import pygame

import os

letterX = pygame.image.load(os.path.join('cross_git.png'))
letterO = pygame.image.load(os.path.join('circle_git.png'))

class Player():
    def __init__(self, width, height, symbol):

        self.widtth = width
        self.height = height
        self.symbol = symbol
        self.grid_lines = [((0, height / 3), (width, height / 3)),
                           ((0, 2 * height / 3), (width, 2 * height / 3)),
                           ((width / 3, 0), (width / 3, height)),
                           ((2 * width / 3, 0), (2 * width / 3, height))]

        self.grid = [[0 for x in range(3)] for y in range(3)]

    def draw(self, window):
        for line in self.grid_lines:
            pygame.draw.line(window, (200, 200, 200), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == 'X':
                    window.blit(letterX, (x*200, y*200))
                elif self.get_cell_value(x, y) == 'O':
                    window.blit(letterO, (x*200, y*200))


    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y):
        if not self.grid[y][x]:
            self.grid[y][x] = self.symbol


    def move(self, pos):
       #if pygame.mouse.get_pressed()[0]:
        #pos = pygame.mouse.get_pos()
        self.set_cell_value(pos[0] // 200, pos[1] // 200)

    def finish(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if not self.get_cell_value(x, y):
                    return False
        return True



    def winner(self):
        for i in range(0, 2):
            if self.get_cell_value(i,0) == self.symbol and  self.get_cell_value(i,1) == self.symbol and self.get_cell_value(i,2) == self.symbol:
                return True
            elif self.get_cell_value(0, i) == self.symbol and  self.get_cell_value(1, i) == self.symbol and self.get_cell_value(2, i) == self.symbol:
                return True

        if self.get_cell_value(0, 0) == self.symbol and  self.get_cell_value(1, 1) == self.symbol and self.get_cell_value(2, 2) == self.symbol:
                return True
        elif self.get_cell_value(0, 2) == self.symbol and  self.get_cell_value(1, 1) == self.symbol and self.get_cell_value(2, 0) == self.symbol:
                return True
        else:
            return False












