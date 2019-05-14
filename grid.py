import pygame

class Grid:
    def __init__(self, width, height):
        self.grid_lines= [((0, height/3), (width, height/3)),
                          ((0, 2*height/3), (width, 2*height/3)),
                          ((width/3, 0), (width/3, height)),
                          ((2*width/3, 0), (2*width/3, height))]




    def draw_grid(self, window):
        for line in self.grid_lines:
            pygame.draw.line(window, (200, 200, 2000), line[0], line[1], 2)
