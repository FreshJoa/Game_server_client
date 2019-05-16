import pygame

class Grid:
    def __init__(self, width, height):
        self.grid_lines= [((0, height/3), (width, height/3)),
                          ((0, 2*height/3), (width, 2*height/3)),
                          ((width/3, 0), (width/3, height)),
                          ((2*width/3, 0), (2*width/3, height))]

        self.grid = [[0 for x in range(3)] for y in range(3)]

    def draw_grid(self, window):
        for line in self.grid_lines:
            pygame.draw.line(window, (200, 200, 200), line[0], line[1], 2)

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, player):
        if not self.grid[y][x]:
            self.grid[y][x] = player

