bif="bg.jpg"
mif="worm.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((480,480),0,32)

points=[(0,150),(150,150),(150,0),(225,75),(300,0),(300,150),(450,150),(375,225),(450,300),(300,300),(300,450),(225,375),(150,450),(150,300),(0,300),(75,225)]
color=(255,255,0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        screen.lock()
        pygame.draw.polygon(screen,color,points)
        screen.unlock()
        
        pygame.display.update()
        