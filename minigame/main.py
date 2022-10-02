import pygame
import time
import random
from ene import *


pygame.init()
display_width = 1200
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

enemy = GameSprite("leopard.png")
enemy_group = pygame.sprite.Group(enemy)

# tank_pos = pygame.Rect(0,0,250,104)

def tank(x,y):
    gameDisplay.blit(tankImg, (x,y))

# def fire(x,y):
#     for i in range(100):
#         x += i
#         y += 1
#         gameDisplay.blit(shellImg, (x,y))

def game_loop():      
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    tank_speed = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                print("--GAMEEND--")
                gameExit = True
                pygame.quit()
                exit()
            # ------------------------ #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            # ------------------------ #
            
        x += x_change
        
        #Set Boundary
        if x >= display_width:
            x = 0
        elif x <= 0:
            x = 0
        
        #Enemy Event
        # enemy_group.update()
        # enemy_group.draw(gameDisplay)
            
        #Update Tank Pos    
        gameDisplay.fill(white)
        tank(x,y)
        # fire(x,y)
        #fire(100,100)
        # if x > display_width - tank_width or x < 0:
        #     gameExit = True    
        
        
        pygame.display.update()
        clock.tick(60)    

game_loop()
pygame.quit()
quit()
