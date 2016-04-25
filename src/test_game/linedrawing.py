bif="bg.jpg"
mif="worm.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((480,480),0,32)

color = (200,100,20)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
        
        if len(points)>1:
            pygame.draw.lines(screen,color,True,points,8)
        
        pygame.display.update()
        