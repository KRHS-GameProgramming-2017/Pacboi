import pygame, math

class Points():
    def __init__(self, kind, pos = [0,0]):
        if kind == "sb":
            self.image = pygame.image.load("Points/Shrute Buck.png")
            self.point = 1
        else:
            self.image = pygame.image.load("Points/Beats.png")
            self.point = 3
        self.rect = self.image.get_rect(topleft = pos)

        
