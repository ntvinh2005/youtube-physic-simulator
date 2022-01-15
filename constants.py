import pygame
pygame.font.init()
FONT = pygame.font.Font("asset/Merriweather-Bold.ttf", 12)

WIDTH, HEIGHT=1200, 600
#1 metres in our simulator equal to 1 pixels
CELL_WIDTH, CELL_HEIGHT = 100, 100

WIN=pygame.display.set_mode((WIDTH, HEIGHT))

WHITE=(255, 255, 255)
RED = (255, 0, 0)
BLACK=(0, 0, 0)

gravity_acceleration = 10

FPS=60
