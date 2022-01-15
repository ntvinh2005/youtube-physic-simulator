import pygame
from constants import *
from environment import CoordinationSystem
from objects import Player

pygame.init()
pygame.HWSURFACE


pygame.display.set_caption("Gravity")

def draw_window(coordinationSystem, player):
    WIN.fill(WHITE)
    coordinationSystem.draw()
    for ball in player.balls:
        ball.draw()

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    coordinationSystem = CoordinationSystem()

    player = Player()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                player.throw_ball(x, y)
            
        for ball in player.balls:
            ball.fall()
        player.remove_ball()
        draw_window(coordinationSystem, player)
    pygame.quit()

if __name__ == "__main__":
    main()