import time
import pygame

pygame.init()

display_width = 640
display_height = 640

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Save the Cat')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
bright_red = (255,0,0)
bright_green = (0,150,0)
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def quitgame():
    pygame.quit()
    quit()

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
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("Save the Cat", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,400,100,50,green,bright_green,game_loop)
        button("Quit",400,400,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(240)
    gameDisplay.fill(white)
    pygame.display.update()



class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('maze.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_threshold(self.image, pygame.Color('black'), (1,1,1,255))


    def draw(self):
        gameDisplay.blit(self.image, self.rect)

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cat.png')
        DEFAULT_IMAGE_SIZE = (30, 30)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect(center=(10,20))
        self.mask1 = pygame.mask.from_threshold(self.image, pygame.Color('white'))
            

    def move(self, a, b, c):
        x_change = 0
        y_change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_UP:
                    y_change = -10
                if event.key == pygame.K_DOWN:
                    y_change = 10
                if pygame.sprite.collide_mask(a, b):
                    self.rect.x = 20
                    self.rect.y = 5
                if pygame.sprite.collide_mask(a, c):
                    exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
        self.rect.x += x_change
        self.rect.y += y_change
                    

    def draw(self):
        gameDisplay.blit(self.image, self.rect)

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('fish.jpg')
        DEFAULT_IMAGE_SIZE = (40, 40)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect(center=(570,20))
        self.mask2 = pygame.mask.from_surface(self.image)

    def draw(self):
        gameDisplay.blit(self.image, self.rect)
    

def game_loop():

    mazeMap = Map()
    cat = Cat()
    fish = Fish()
    cat.rect.x += 20
    cat.rect.y += 5
    while True:
        mazeMap.draw()
        cat.draw()
        fish.draw()
        cat.move(cat, mazeMap, fish)
        pygame.display.update()
game_intro()
pygame.display.update()
game_loop()
