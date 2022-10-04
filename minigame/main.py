import pygame
import time
import random
from ene import *


pygame.init()
display_width = 1000
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tank Simulation')
clock = pygame.time.Clock()

crashed = False
tankImg = pygame.image.load('TE_Karrar.png')
tank_width = 250

shellImg = pygame.image.load('Heavy_Shell.png')
targetImg = pygame.image.load('img/target.png')

enemy = GameSprite("leopard.png")
enemy_group = pygame.sprite.Group(enemy)
# tank_pos = pygame.Rect(0,0,250,104)

def tank(x,y):
    gameDisplay.blit(tankImg, (x,y))

def shell(x,y):
    gameDisplay.blit(shellImg, (x,y))
    
def target(x,y):
    gameDisplay.blit(targetImg, (x,y))

def game_loop():
    # x = (display_width * 0.45)
    # y = (display_height * 0.8)
    x=0
    y=480
    shell_x = x + tank_width
    shell_y = display_height - 110
    
    target_x = 800
    target_y = 200
    
    x_change = 0
    y_change = 0
    tank_speed = 0
    gameExit = False
     
    while not gameExit:
        STATUS = False
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                print("--GAMEEND--")
                gameExit = True
                pygame.quit()
                exit()
            # ------------------------ #
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:
                x_change = -3
            elif keys_pressed[pygame.K_RIGHT]:
                x_change = 3
            elif keys_pressed[pygame.K_UP]:
                y_change = -2
            elif keys_pressed[pygame.K_DOWN]:
                y_change = 2
            elif keys_pressed[pygame.K_f]:
                STATUS = True
            # ------------------------ #
        #---Target---#
        direction = random.randint(-1,1)
        target_moving_speed = 3
        target_y += target_moving_speed * direction
        target(target_x,target_y)
        pygame.display.update()
        #Tank Movement
        x += x_change
        y += y_change
        #Set Boundary
        if x >= display_width:
            x = 0
        elif x <= 0:
            x = 0
        #Update Tank Pos    
        gameDisplay.fill(white)

        tank(x,y)
        if STATUS:
            while shell_x < display_width:
                print("EXE")
                shell(shell_x,shell_y)
                shell_x += 100
                STATUS = False
                pygame.display.update() 
        shell_x = x + tank_width
        shell_y = y + 10
        # shell(shell_x,shell_y)
        pygame.display.update()
        clock.tick(30)    

game_loop()
pygame.quit()
quit()
