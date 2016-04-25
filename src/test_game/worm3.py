bif="bg.jpg"
mif="worm.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,360),0,32)

background=pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()

x,y = 0,0
movex,movey = 0,0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.lock()
    pygame.draw.rect(screen,(120,120,120),Rect((100,100),(200,130)))
    screen.unlock()
        
    pygame.display.update()
        