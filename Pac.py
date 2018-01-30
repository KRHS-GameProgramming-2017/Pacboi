import pygame, sys, math, random
from Points import *
from Pacboi import *
from Opponents import *

pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [18, 5, 180]

points = [Points("sb", [100, 100]),
          Points("beat", [200, 200])]

boi = Pacboi(size)

level = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                boi.go("up")
            if event.key == pygame.K_DOWN:
                boi.go("down")
            if event.key == pygame.K_LEFT: 
                boi.go("left")
            if event.key == pygame.K_RIGHT: 
                boi.go("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                boi.go("stop up")
            if event.key == pygame.K_DOWN: 
                boi.go("stop down")
            if event.key == pygame.K_LEFT: 
                boi.go("stop left")
            if event.key == pygame.K_RIGHT: 
                boi.go("stop right")
             
    boi.move()
            
    screen.fill(bgColor)
    for p in points:
        screen.blit(p.image, p.rect)
    screen.blit(boi.image, boi.rect)
    screen.blit(Opponent.image, Opponent.rect)
    pygame.display.flip()
    clock.tick(60)
