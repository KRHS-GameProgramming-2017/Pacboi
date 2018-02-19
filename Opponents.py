import pygame, math

class Opponent():
    def __init__(self, screenSize):
        self.image = pygame.image.load("Opponents\Ghost.png")
        self.maxSpeed = 6
        self.speed = [2,2]
        self.rect = self.image.get_rect()
        
    def hitWall(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0]  = -self.speed[0]
            self.move()
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1]  = -self.speed[1]
            self.move()
            
    def move(self):
        self.rect.move_ip(self.speed)

