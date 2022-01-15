import pygame
from constants import *

class Player:
    def __init__(self):
        self.balls=[]
    
    def throw_ball(self, x, y):
        new_ball = Ball(x, y)
        self.balls.append(new_ball)
    
    def remove_ball(self):
        for ball in self.balls:
            if ball.y>=HEIGHT:
                self.balls.remove(ball)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15

        self.fall_vel = 0
        self.fall_time = 0
        self.distance = 0
        self.initial_y = y

        self.label = Label(x, y, y ,0)
    
    def draw(self):
        pygame.draw.circle(WIN, RED, (self.x, self.y), self.radius)
        self.label.draw()
    
    def fall(self):
        self.fall_time+=1/60
        self.fall_vel = gravity_acceleration*self.fall_time
        self.y = self.initial_y + gravity_acceleration*self.fall_time**2/2
        self.label.receive_data([self.y, self.fall_vel])


class Label:
    def __init__(self, x, y, position_y, fall_vel):
        self.x = x
        self.y = y
        self.indexes = [position_y, fall_vel]
    
    def receive_data(self, data):
        self.indexes = data
    
    def draw(self):
        i = 0
        for index in self.indexes:
            text_surface = FONT.render(str(index), 1, BLACK)
            WIN.blit(text_surface, (self.x, self.y + i*40))
            i+=1


    