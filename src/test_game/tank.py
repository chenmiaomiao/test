bif = "bg.jpg"
baxa = "baxa.png"
ongxa = "ongxa.jpg"
cookie = "cookie.png"

import pygame, sys
import time
import random
from pygame.locals import *

display_width = 1200
display_height = 700
appleThickness = 50
block_size = 50
step_size = 50
FPS = 5
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
direction = "down"
gameEntrance = False

pygame.init()
screen = pygame.display.set_mode((display_width, display_height), 0, 32)
icon = pygame.image.load(baxa)
pygame.display.set_icon(icon)
pygame.display.set_caption("Ongxa Eats Baxa")

background = pygame.image.load(bif).convert()
baxa = pygame.image.load(baxa).convert_alpha()
ongxa = pygame.image.load(ongxa).convert_alpha()
cookie = pygame.image.load(cookie).convert_alpha()
baxa_dep = pygame.transform.scale(baxa, (appleThickness, appleThickness))
ongxa_dep = pygame.transform.scale(ongxa, (block_size, block_size))
cookie = pygame.transform.scale(cookie, (block_size, block_size))
clock = pygame.time.Clock()
font_general = pygame.font.SysFont(None, 50)

def rotateImage(image, direction):
    if direction  ==  "left":
        image = pygame.transform.rotate(image, 270)
    if direction  ==  "right":
        image = pygame.transform.rotate(image, 90)
    if direction  ==  "up":
        image = pygame.transform.rotate(image, 180)
    if direction  ==  "down":
        image = image
    return image

def text_objects(text, color, size = "small"):
    if size  ==  "small":
        font = pygame.font.SysFont("comicsansms", 25)
    if size  ==  "medium":
        font = pygame.font.SysFont("comicsansms", 50)
    if size  ==  "large":
        font = pygame.font.SysFont("comicsansms", 80)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, size, displace_y = 0):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2+displace_y)
    screen.blit(textSurf, textRect)
    
def gameEvent():
    global gameExit, gameOver, gamePause, gameEntrance
    for event in pygame.event.get():
        if event.type  ==  QUIT:
            gameExit = True
            gameOver = False
            gamePause = False
            gameEntrance = True
        if event.type  ==  pygame.KEYDOWN:
            if event.key  ==  pygame.K_q:
                gameExit = True
                print gameExit
                gameOver = False
                gamePause = False
                gameEntrance = True
            if event.key  ==  pygame.K_c:
                if gameOver  ==  True:
                    gameLoop()
                gameExit = False
                gameOver = False
                gamePause = False
                gameEntrance = True
                
def scoreShow(scores):
    scores = str(scores)
    text_score = font_general.render("Score: "+scores, True, black)
    screen.blit(text_score,(0,0))
    pygame.display.update()
def over():
    global gameExit, gameOver, gamePause, gameEntrance
    gameOver = True
    while gameOver:
        gameEvent()
        
        message_to_screen("Xau Qua", red, size = "large")
        message_to_screen("Press C to continue or Q to quit", black, "small",displace_y=100)
        pygame.display.update()
        clock.tick(5)
        
def pause(moving):
    global gameExit, gameOver, gamePause, gameEntrance
    gamePause = True
    while gamePause and moving:
        gameEvent()
        
        message_to_screen("Game Paused", green, "large")
        message_to_screen("Press C to continue or Q to quit", black, "small",displace_y=100)
        pygame.display.update()
        clock.tick(5)       

def gameInro():
    global gameExit, gameOver, gamePause, gameEntrance
    while not gameEntrance:
        gameEvent()
        
        screen.fill(white)
        message_to_screen("Welcome to Ongxaeatsbaxa", black, "large")
        message_to_screen("Press C to continue, P to Pause or Q to quit", black, "small",displace_y=100)
        pygame.display.update()
        clock.tick(5)
                 
def apple(apple_x, apple_y, block_size):
    #pygame.draw.rect(screen, green, [apple_x, apple_y, block_size, block_size])
    screen.blit(baxa_dep, (apple_x, apple_y))

def snake(snakelist, block_size, snakeLenth, direction="down"):
    head = rotateImage(ongxa_dep, direction)
    screen.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        #pygame.draw.rect(screen, red, [XnY[0], XnY[1], block_size, block_size])
        screen.blit(cookie,(XnY[0], XnY[1]))
        
# the main loop of the game
def gameLoop():
    global direction, gameExit, gameOver, gamePause,gameEntrance
    lead_x, lead_y = display_width/2, display_height/2
    movex, movey = 0, 0
    snakeList = []
    snakeLenth = 1
    
    randAppleX = random.randrange(0, display_width-appleThickness)
    randAppleY = random.randrange(0, display_height-appleThickness)
    
    gameExit = False
    gameOver = False
    gamePause = False
    
    while not gameExit:
        gameInro()
        
        for event in pygame.event.get():
            if event.type  ==  QUIT:
                gameExit = True
            if event.type  ==  KEYDOWN:
                if event.key  ==  K_q:
                    gameExit = True
                elif event.key  ==  K_LEFT:
                    movex = -step_size
                    movey = 0
                    direction = "left"
                elif event.key  ==  K_RIGHT:
                    movex = +step_size
                    movey = 0
                    direction = "right"
                elif event.key  ==  K_UP:
                    movey = -step_size
                    movex = 0
                    direction = "up"
                elif event.key  ==  K_DOWN:
                    movey = +step_size
                    movex = 0
                    direction = "down"
                # check the snake's motion
                if movex != 0 or movey != 0:
                    moving = True
                else:
                    moving = False
                if event.key  ==  K_p:
                    pause(moving)
        
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            over()
           
        lead_x+= movex
        lead_y+= movey
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList)>snakeLenth:
            del snakeList[0]
        
        for eachSegment in snakeList[:-1]:
            if eachSegment  ==  snakeList[-1]:
                over()
                
        if lead_x <= randAppleX and lead_x + block_size >= randAppleX or lead_x <= randAppleX + appleThickness and lead_x + block_size >= randAppleX + appleThickness:
            if lead_y <= randAppleY and lead_y + block_size >= randAppleY or lead_y <= randAppleY + appleThickness and lead_y + block_size >= randAppleY + appleThickness:
                randAppleX = random.randrange(0, display_width-appleThickness)
                randAppleY = random.randrange(0, display_height-appleThickness) 
                snakeLenth += 1 
        
        for XnY in snakeList:
            if XnY[0] <= randAppleX and XnY[0] + block_size >= randAppleX or XnY[0] <= randAppleX + appleThickness and XnY[0] + block_size >= randAppleX + appleThickness:
                if XnY[1] <= randAppleY and XnY[1] + block_size >= randAppleY or XnY[1] <= randAppleY + appleThickness and XnY[1] + block_size >= randAppleY + appleThickness:
                    randAppleX = random.randrange(0, display_width-appleThickness)
                    randAppleY = random.randrange(0, display_height-appleThickness)
        
        screen.blit(background, (0, 0))
        snake(snakeList, block_size, snakeLenth, direction)
        apple(randAppleX, randAppleY, appleThickness)
        scoreShow((snakeLenth-1)*10)
        pygame.display.update()
        
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
    