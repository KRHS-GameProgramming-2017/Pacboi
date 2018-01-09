import pygame, sys, math, random

pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [18, 5, 180]

level = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill(bgColor)
    pygame.display.flip()
    clock.tick(60)
