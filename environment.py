import pygame
from constants import *

class CoordinationSystem():
    def __init__(self):
        self.horizontal_lines = []
        self.vertical_lines = []
        i = 0
        while i <= HEIGHT:
            newHorizontalLine = HorizontalLine (0, i)
            self.horizontal_lines.append(newHorizontalLine)
            i+=100
        i = 0
        while i <= WIDTH:
            newVerticalLine = VerticalLine (i, 0)
            self.vertical_lines.append(newVerticalLine)
            i+=100
    
    def draw(self):
        for line in self.horizontal_lines:
            pygame.draw.rect(WIN, BLACK, (line.x, line.y, WIDTH, 1))
            text_surface = FONT.render(str(line.y), 1, BLACK)
            WIN.blit(text_surface, (line.x , line.y- text_surface.get_height()/2))

        for line in self.vertical_lines:
            pygame.draw.rect(WIN, BLACK, (line.x, line.y, 1, HEIGHT))
            text_surface = FONT.render(str(line.x), 1, BLACK)
            WIN.blit(text_surface, (line.x - text_surface.get_width()/2, line.y))

class HorizontalLine():
    def __init__(self, x, y):
        self.x = x   
        self.y = y
 
class VerticalLine():
    def __init__(self, x, y):
        self.x = x
        self.y = y