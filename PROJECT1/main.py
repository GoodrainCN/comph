from re import X
import pygame
import get_data
import button

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)
small_font = pygame.font.SysFont("arialblack", 20)
#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
coil_img = pygame.image.load('images/coilgun.jpeg')
ball_img = pygame.image.load('images/ball.jpg').convert_alpha()

#Test get image size
a = quit_img.get_width()
print(a)

coil_img = pygame.transform.scale(coil_img, (100,100))
ball_img = pygame.transform.scale(ball_img, (25,25))
#create button instances
resume_button = button.Button(SCREEN_WIDTH/2 - (resume_img.get_width()/2), 125, resume_img, 1)
options_button = button.Button(SCREEN_WIDTH/2 - (options_img.get_width()/2), 250, options_img, 1)
quit_button = button.Button(SCREEN_WIDTH/2 - (quit_img.get_width()/2), 375, quit_img, 1)
keys_button = button.Button(400, 325, keys_img, 1)
back_button = button.Button(400, 450, back_img, 1)

def pointInRectanlge(px, py, rw, rh, rx, ry):
    if px > rx and px < rx  + rw:
        if py > ry and py < ry + rh:
            return True
    return False

#Blueprint to make sliders in the game
class Slider:
    def __init__(self, position:tuple, upperValue:int=50000, sliderWidth:int = 30, text:str="Editing features for simulation",
                 outlineSize:tuple=(300, 100))->None:
        self.position = position
        self.outlineSize = outlineSize
        self.text = text
        self.sliderWidth = sliderWidth
        self.upperValue = upperValue
        
    #returns the current value of the slider
    def getValue(self)->float:
        return 5000 + self.sliderWidth / (self.outlineSize[0] / self.upperValue)

    #renders slider and the text showing the value of the slider
    def render(self, display:pygame.display)->None:
        #draw outline and slider rectangles
        pygame.draw.rect(display, (0, 0, 0), (self.position[0], self.position[1], 
                                              self.outlineSize[0], self.outlineSize[1]), 3)
        
        pygame.draw.rect(display, (0, 0, 0), (self.position[0], self.position[1], 
                                              self.sliderWidth, self.outlineSize[1] - 10))

        #determite size of font
        self.font = pygame.font.Font(pygame.font.get_default_font(), int((15/100)*self.outlineSize[1]))

        #create text surface with value
        valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (255, 0, 0))
        
        #centre text
        # textx = self.position[0] + (self.outlineSize[0]/2) - (valueSurf.get_rect().width/2)
        # texty = self.position[1] + (self.outlineSize[1]/2) - (valueSurf.get_rect().height/2)

        textx = 600
        texty = 400
        
        display.blit(valueSurf, (textx, texty))

    #allows users to change value of the slider by dragging it.
    def changeValue(self)->None:
        #If mouse is pressed and mouse is inside the slider
        mousePos = pygame.mouse.get_pos()
        if pointInRectanlge(mousePos[0], mousePos[1]
                            , self.outlineSize[0], self.outlineSize[1], self.position[0], self.position[1]):
            if pygame.mouse.get_pressed()[0]:
                #the size of the slider
                self.sliderWidth = mousePos[0] - self.position[0]

                #limit the size of the slider
                print(self.sliderWidth)
                # if self.sliderWidth == 0:
                #     self.sliderWidth = 5000
                if self.sliderWidth <= 1:
                    self.sliderWidth =0
                if self.sliderWidth > self.outlineSize[0]:
                    self.sliderWidth = self.outlineSize[0]

def slider_scene():
  draw_text("Slider Scene", font, (0,0,0), 400, 50)
  draw_text("Press 'c' to comfirm your value", small_font, (0,0,0), 400, 100)
  pygame.display.update()
  not_selected = True
  slider = Slider((600, 350))
  while not_selected:
    pygame.event.get()
    screen.fill((255, 255, 255))
    slider.render(screen)
    slider.changeValue()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                not_selected = False
                break
    #print(slider.getValue())
    pygame.display.update()
  return slider.getValue()

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def coilgun(x,y):
  screen.blit(coil_img,(x,y))

def quitgame():
    pygame.quit()
    quit()

def draw_ball(x,y):
  screen.blit(ball_img, (x,y))

def first_scene(new_ampere=None):
  temp = new_ampere
  temp = "Ampere: " + str(temp)
  draw_text("COILGUN", font, TEXT_COL, 100, 25)
  draw_text("Press f to simulate", small_font, TEXT_COL, 150, 600)
  draw_text(temp, small_font, TEXT_COL, 150, 550)
  draw_text("Press q to quit", small_font, TEXT_COL, 150, 650)
  screen.blit(coil_img, (100,150))
  
    #event handler
  simu_start = False
  quit_game = False
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_f:
        simu_start = True
        print("f pressed")
      if event.key == pygame.K_q:
          quit_game = True
          print("game quit")
  if quit_game:
        quitgame()
  if simu_start == True:
    print("simu start")
    if new_ampere == None:
        data = get_data.run()
    else:
        data = get_data.run(new_ampere)
    x_data = data[0]
    x_data = [i*100 + 200 for i in x_data]
    y_data = data[1]
    y_data = [i*100 + 50 for i in y_data]
    temp_x = 0
    temp_y = 0
    x_d = x_data[-1] - 200
    y_d = y_data[-1] - 50
    x_st = "x: " + str(round(x_d)) + "m"
    y_st = "y: " + str(round(y_d)) + "m"
    draw_text(x_st, small_font, TEXT_COL, 600, 600)
    draw_text(y_st, small_font, TEXT_COL, 600, 650)
    pygame.display.update()
    for i in range(0,len(x_data)):
      temp_x = x_data[i]
      temp_y = 398.41 - y_data[i]
      print(temp_x, temp_y)
      screen.blit(ball_img, (temp_x,temp_y))
      pygame.display.update()
      if i == len(x_data)-1:
        break

#game loop
game_start = False
run = True
timess = 0
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_start == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      draw_text("To see tutorial select option", small_font, TEXT_COL, 100, 600)
      if resume_button.draw(screen):
        menu_state = "scene"
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      draw_text("This Program is Designed to Simulate Coilgun's Projectile", small_font, TEXT_COL, 100, 75)
      draw_text("First use the slide bar to select value of ampere", small_font, TEXT_COL, 100, 100)
      draw_text("Press C to confirm your selection", small_font, TEXT_COL, 100, 125)
      draw_text("Press F to start the simulation", small_font, TEXT_COL, 100, 150)
      if back_button.draw(screen):
        menu_state = "main"
    elif menu_state == "scene":
      if timess == 0:
        temp = slider_scene()
        timess = 1
      else:
        first_scene(temp)
  else:
    draw_text("Press SPACE to START", font, TEXT_COL, 250, 250)

  #event handler
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_start = True
        # game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()