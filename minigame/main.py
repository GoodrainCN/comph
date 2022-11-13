import pygame
import time
import random


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
tankImg = pygame.image.load('img/TE_Karrar.png')
tank_width = 250

shellImg = pygame.image.load('img/Heavy_Shell.png')
targetImg = pygame.image.load('img/target.png')
# tank_pos = pygame.Rect(0,0,250,104)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("TANK SIM/ Goodrain", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",750,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("HIT: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def tank(x,y):
    gameDisplay.blit(tankImg, (x,y))

def shell(x,y):
    gameDisplay.blit(shellImg, (x,y))
    
def target(x,y):
    target_rect = targetImg.get_rect()
    target_rect.x = x
    target_rect.y = y
    gameDisplay.blit(targetImg, target_rect)    
    
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def quitgame():
    pygame.quit()
    quit()

def game_loop():
    x=0
    y=480
    shell_x = x + tank_width
    shell_y = display_height - 110
    
    target_x = 850
    target_y = 0
    target_speed = 2
    
    thing_starty = -600
    thing_height = 100

    HIT = 0

    x_change = 0
    y_change = 0

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -3
                if event.key == pygame.K_RIGHT:
                    x_change = 3
                if event.key == pygame.K_UP:
                    y_change = -3
                if event.key == pygame.K_DOWN:
                    y_change = 3
                if event.key == pygame.K_f:
                    STATUS = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                        event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
                            event.key == pygame.K_f:
                    x_change = 0
                    y_change = 0
                    STATUS = False
    
        #Tank Movement
        x += x_change
        y += y_change
        
        #Set Boundary
        if x >= display_width:
            x = 0
        elif x <= 0:
            x = 0
            
        #Plot the Background
        gameDisplay.fill(white)

        #Plot the Target
        target(target_x, target_y)
        things_dodged(HIT)
        target_y += target_speed
        
        #Update Tank
        tank(x,y)
        
        #accuracy
        err = 60
        #Shell Animation
        if STATUS:
            HIT = 0
            while shell_x < display_width:
                print("EXE")
                shell(shell_x,shell_y)
                shell_x += 100
                pygame.display.update()
                # if (target_x - err <= shell_x <= target_x + err)\
                #     and (target_y - err <= shell_y <= target_y + err):
                if(shell_x == target_x):
                    HIT += 1
                    STATUS = False
            
        shell_x = x + tank_width
        shell_y = y + 10
        # shell(shell_x,shell_y)
        pygame.display.update()
        clock.tick(30)
        
game_intro()
game_loop()
pygame.quit()
quit()
