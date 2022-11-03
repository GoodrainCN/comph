import time
import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('FUCKSHIT')

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)
clock = pygame.time.Clock()

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
    
def game_tutorial():
    pygame.display.update()
    clock.tick(30)
    gameDisplay.fill(white)
    smallText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = text_objects("Tutorial", smallText)
    TextRect.center = (200,100)
    gameDisplay.blit(TextSurf, TextRect)
    button("Back",375,300,100,50,red,bright_red,game_intro)
    pygame.display.update()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("COILGUN SIM", largeText)
        TextRect.center = (400,100)
        gameDisplay.blit(TextSurf, TextRect)

        button("Tutorial",375,200,100,50,green,bright_green,game_tutorial)
        button("Quit",375,425,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
        
def quitgame():
    pygame.quit()
    quit()

def game_loop():
    # pygame.display.update()
    # clock.tick(30)
    pass
        
game_intro()
game_loop()
pygame.quit()
quit()
