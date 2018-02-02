import pygame, math

class Pacboi():
    def __init__(self, screenSize):
        self.images = [pygame.image.load("Pacboi\Pacboi Closed.png"),
                     pygame.image.load("Pacboi\Pacboi Open.png")]
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.count = 0
        self.countMax = 60/4
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.maxSpeed = 6
        self.speed = [0,0]
          
    def move(self):
        self.animate()
        self.rect.move_ip(self.speed)

    def animate(self):
        if self.count < self.countMax:
            self.count += 1
        else:
            self.count = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]

    def go(self, direction):
        if direction == "up":
            self.speed[1] = -self.maxSpeed
        elif direction == "down":
            self.speed[1] = self.maxSpeed
        elif direction == "right":
            self.speed[0] = self.maxSpeed
        elif direction == "left":
            self.speed[0] = -self.maxSpeed

        if direction == "stop up":
            self.speed[1] = 0
        elif direction == "stop down":
            self.speed[1] = 0
        elif direction == "stop right":
            self.speed[0] = 0
        elif direction == "stop left":
            self.speed[0] = 0
