import pygame

class item:
    def __init__(self, tilesize, color):
        self.item = [[10,3]]
        self.tilesize = tilesize
        self.color = color
        
        
    def draw(self, screen):
        for elt in self.item:
            pygame.draw.polygon(screen,self.color,((elt[0]*self.tilesize + (self.tilesize/2), elt[1]*self.tilesize), (elt[0]*self.tilesize, elt[1]*self.tilesize  + (self.tilesize/2)), (elt[0]*self.tilesize + (self.tilesize/2), elt[1]*self.tilesize  + self.tilesize),  (elt[0]*self.tilesize + self.tilesize, elt[1]*self.tilesize + (self.tilesize/2))) )
    
    