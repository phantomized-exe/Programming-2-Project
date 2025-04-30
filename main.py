import pygame
from sys import exit #terminate the program
import os

# game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512

PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 80
PLAYER_DISTANCE = 5

# imgages
background_image = pygame.image.load(os.path.join("Test Sprites/Test Sprite-back.png.png"))
player_image = pygame.image.load(os.path.join("Test Sprites/Test Sprite-right.png.png"))
player_image = pygame.transform.scale(player_image,(PLAYER_WIDTH,PLAYER_HEIGHT)) #resizes player
image_icon = pygame.image.load(os.path.join("Test Sprites/Test Sprite-icon.png.png"))

pygame.init() #always needed to initialize pygame
window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("test") #title of window
pygame.display.set_icon(image_icon)
clock = pygame.time.Clock() #used for the framerate

class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,PLAYER_X,PLAYER_Y,PLAYER_WIDTH,PLAYER_HEIGHT)
        self.image = player_image

#left(x), top(y), width, height
player = Player()

def draw():
    #window.fill("blue")
    #window.fill("#54de9e")
    #window.fill((84,222,158))
    window.fill((20,18,167))
    window.blit(background_image, (0,0))
    window.blit(player.image,player)
while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicks the X button in window
            pygame.quit()
            exit()

        #KEYDOWN - key was pressed, KEYUP - key was pressed/release
        '''
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                player.y -= 5
            if event.key in (pygame.K_DOWN, pygame.K_s):
                player.y += 5
            if event.key in (pygame.K_LEFT, pygame.K_a):
                player.x -= 5
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                player.x += 5
        '''
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y - PLAYER_DISTANCE >= 0:
        player.y -= PLAYER_DISTANCE
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y + player.height + PLAYER_DISTANCE <= GAME_HEIGHT:
        player.y += PLAYER_DISTANCE
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_image = pygame.image.load(os.path.join("Test Sprites/Test Sprite-left.png.png"))
        player_image = pygame.transform.scale(player_image,(PLAYER_WIDTH,PLAYER_HEIGHT))
        player.image = player_image
        player.x -= PLAYER_DISTANCE
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_image = pygame.image.load(os.path.join("Test Sprites/Test Sprite-right.png.png"))
        player_image = pygame.transform.scale(player_image,(PLAYER_WIDTH,PLAYER_HEIGHT))
        player.image = player_image
        player.x += PLAYER_DISTANCE

    draw()
    pygame.display.update()
    clock.tick(60) #frames per second (fps)
