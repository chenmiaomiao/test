bif="bg.jpg"
mif="worm.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,360),0,32)

background=pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()

x=0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(background, (0,0))
    screen.blit(mouse_c,(x,100))
    x+=0.1
    
    if x>640:
        x=0
    
    pygame.display.update()
