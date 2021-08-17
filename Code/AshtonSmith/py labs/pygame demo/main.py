#from typing_extensions import TypeVarTuple
import pygame
import random
#following: at 1:34
#https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org
#initalize pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600)) #args: height, width
#background
background = pygame.image.load('background.png')

#Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

#alien
alien_img = pygame.image.load('alien.png')
alien_x = random.randint(0,800)
alien_y = random.randint(50,150)
alien_x_change = 0.3
alien_y_change = 20


#bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = .8
bullet_state = 'ready' #ready state - cant see bullet #fire can see

def player(x,y):
    screen.blit(player_img,(x, y)) #blit means to draw  args: image to blit and location (x, y)
    # blit now needs to be called in the game loop.

def alien(x,y):
    screen.blit(alien_img,(x, y)) #blit means to draw  args: image to blit and location (x, y)

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = 'fire'
    screen.blit(bullet_img, (x+16, y+10))

# Game loop
running = True
while running:
        #change the background color
    #screen.fill((2,50,5)) #args RGB, red, green ,blue (0-255)

    #background image
    screen.blit(background,(0,0))   
        #if event (exited window)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    #if keystroke is pressed check if it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -.3
                print('key pressed Left')
            if event.key == pygame.K_RIGHT:
                player_x_change = .3
                print('key pressed right')
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire_bullet(bullet_x,bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('key released')
                player_x_change = 0
    
    player_x += player_x_change
    #bounds checking
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    #alien bounds/movement
    if alien_x <= 0:
        alien_x_change = 0.2
        alien_y += alien_y_change
    elif alien_x >= 736:
        alien_x_change = -0.2
        alien_y += alien_y_change
    alien_x += alien_x_change
    
    # bullet movement
    if(bullet_y <= 0):
        bullet_y = 480
        bullet_state = 'ready'

    if(bullet_state is 'fire'):
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change

    alien(alien_x,alien_y)
    player(player_x,player_y)
        #update the display
    pygame.display.update()