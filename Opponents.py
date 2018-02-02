import pygame, math

class Opponent():
    def __init__(self, screenSize):
        self.image = pygame.image.load("Ghost.png")
        self.maxSpeed = 6
        self.speed = [0,0]
        self.rect = self.image.get_rect()
       
        
    def hitWall(self):
        width = self.screenSize[0]
        height = self.screenSize[1]
    
        if self.box.left < 0 or self.box.right > width:
            self.speed[0]  = -self.speed[0]
            self.go()
        if self.box.top < 0 or self.box.bottom > height:
            self.speed[1]  = -self.speed[1]
            self.go()
            
    def go(self):
        self.rect.move_ip(self.speed)

