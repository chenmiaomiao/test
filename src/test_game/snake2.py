import colorsys
from wx.tools.Editra.src.eclib import colorsetter
bif="bg.jpg"
mif="worm.png"

import pygame, sys
import time
import random
from pygame.locals import *


display_width = 640
display_height = 360
block_size = 10
step_size = 10
FPS = 10
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)

pygame.init()
screen=pygame.display.set_mode((display_width,display_height),0,32)

background=pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def text_objects(text, color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def apple(apple_x, apple_y, block_size):
    pygame.draw.rect(screen, green, [apple_x, apple_y, block_size, block_size])

def snake(snakelist, block_size, snakeLenth):
    for XnY in snakelist[-snakeLenth:]:
        pygame.draw.rect(screen, red, [XnY[0], XnY[1], block_size, block_size])

def message_to_screen(msg,color):
#     screen_text = font.render(msg,True,color)
#     screen.blit(screen_text, [display_width/2, display_height/2])
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (display_width/2), (display_height/2)
    screen.blit(textSurf, textRect)
#     print textRect
#     print textRect.center
#     print dir(textRect)

def gameLoop():
    lead_x,lead_y = display_width/2,display_height/2
    movex,movey = 0,0
    snakeList = []
    snakeLenth = 1
    
    randAppleX = round(random.randrange(0,display_width-block_size)/block_size)*block_size
    randAppleY = round(random.randrange(0,display_height-block_size)/block_size)*block_size
    
    gameExit = False
    gameOver = False
    
    while not gameExit:
        while gameOver:
            message_to_screen("Game Over", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                gameExit = True
                
            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    movex=-step_size
                    movey=0
                elif event.key==K_RIGHT:
                    movex=+step_size
                    movey=0
                elif event.key==K_UP:
                    movey=-step_size
                    movex=0
                elif event.key==K_DOWN:
                    movey=+step_size
                    movex=0
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
           
        lead_x+=movex
        lead_y+=movey
        
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0,display_width-block_size)/block_size)*block_size
            randAppleY = round(random.randrange(0,display_height-block_size)/block_size)*block_size
            snakeLenth += 1
            
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList)>snakeLenth:
            del snakeList[0]
        
        for eachSegment in snakeList[:-1]:
            if eachSegment ==  snakeList[-1]:
                gameOver = True
        
        screen.blit(background,(0,0))
        snake(snakeList, block_size,snakeLenth)
        apple(randAppleX, randAppleY, block_size)
        pygame.display.update()
        
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
    