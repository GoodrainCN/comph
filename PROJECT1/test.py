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

def first_scene():
  draw_text("COILGUN", font, TEXT_COL, 100, 25)
  draw_text("Press f to simulate", small_font, TEXT_COL, 150, 600)
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
    data = get_data.run()
    x_data = data[0]
    x_data = [i*100 + 200 for i in x_data]
    y_data = data[1]
    y_data = [i*100 + 50 for i in y_data]
    temp_x = 0
    temp_y = 0
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
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_start == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
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
      draw_text("Fire When Fully Charged", small_font, TEXT_COL, 100, 100)
      if back_button.draw(screen):
        menu_state = "main"
    elif menu_state == "scene":
      first_scene()
  else:
    draw_text("Press SPACE to START", font, TEXT_COL, 160, 250)

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