import pygame, sys, math, random
from Points import *

pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [18, 5, 180]

points = [Points("sb", [100, 100]),
          Points("beat", [200, 200])]

level = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill(bgColor)
    for p in points:
        screen.blit(p.image, p.rect)
    pygame.display.flip()
    clock.tick(60)
