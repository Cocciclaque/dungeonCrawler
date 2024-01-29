import pygame

class alien:
    def __init__(self, tilesize, color):
        self.item = [[10,5]]
        self.tilesize = tilesize
        self.color = color
        
        
    def draw(self, screen):
        for elt in self.item:
            pygame.draw.circle(screen, self.color, [elt[0] * self.tilesize, elt[1] * self.tilesize], 15)