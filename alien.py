import pygame
import random

class alien:
    def __init__(self, tilesize, color):
        self.item = [[10,5]]
        self.tilesize = tilesize
        self.color = color
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        
        
    def draw(self, screen):
        for elt in self.item:
            pygame.draw.circle(screen, self.color, [elt[0] * self.tilesize, elt[1] * self.tilesize], 15)
            
    def update_position(self):
        if self.direction == 'UP':
            self.item[0][1] -= 1
        elif self.direction == 'DOWN':
            self.item[0][1] += 1
        elif self.direction == 'LEFT':
            self.item[0][1] -= 1
        elif self.direction == 'RIGHT':
            self.item[0][1] += 1