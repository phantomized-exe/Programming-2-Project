import pygame
from sys import exit #terminate the program
import os
from pathlib import Path
import json
import random
from network import Network
import time
import subprocess
level = Path("level_code.json")
save = Path("save.json")

# game variables
TILE_SIZE = 32
GAME_WIDTH = 640#512
GAME_HEIGHT = 480#512

PLAYER_WIDTH = 28
PLAYER_HEIGHT = 58
PLAYER_X = 306
PLAYER_Y = 208
PLAYER_JUMP_WIDTH = 28
PLAYER_JUMP_HEIGHT = 58
PLAYER_CROUCH_WIDTH = 28
PLAYER_CROUCH_HEIGHT = 32
PLAYER_DISTANCE = 5
BACKGROUND_X = 2048
global BACKGROUND_Y
BACKGROUND_Y = 512
BACKGROUND_WIDTH = 1024
BACKGROUND_HEIGHT = 1024

GRAVITY = 2.5
FRICTION = 1.2
PLAYER_VELOCITY_X = 9#6
global PLAYER_VELOCITY_Y
PLAYER_VELOCITY_Y = -20
global CROUCH_FRICTION
CROUCH_FRICTION = 1

# images
def load_image(image_name,scale=None):
    """Loads all the images in the Test Sprite folder

    Args:
        image_name (str): name of image
        scale (int, optional): scales the image. Defaults to None.

    Returns:
        pygame.image: image
    """
    image = pygame.image.load(os.path.join("Test Sprites",image_name))
    if scale is not None:
        image = pygame.transform.scale(image,scale)
    return image
background_image0 = load_image("Mountains-front.png.png",(BACKGROUND_WIDTH,BACKGROUND_HEIGHT))
background_image3 = load_image("Test Sprite-back3.png.png",(BACKGROUND_WIDTH,BACKGROUND_HEIGHT))
background_image = load_image("Mountains-back.png.png",(BACKGROUND_WIDTH,BACKGROUND_HEIGHT))
background_image2 = load_image("Test Sprite-back2.png.png",(BACKGROUND_WIDTH,BACKGROUND_HEIGHT))
background_image4 = load_image("Test Sprite-back4.png.png",(GAME_WIDTH,GAME_HEIGHT))
player_image_right = load_image("Test Sprite-right.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_right2 = load_image("Test Sprite-right2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT)) #resizes player
player_image_left = load_image("Test Sprite-left.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_left2 = load_image("Test Sprite-left2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player2_image_right = load_image("Test Sprite2-right.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player2_image_right2 = load_image("Test Sprite2-right2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT)) #resizes player
player2_image_left = load_image("Test Sprite2-left.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player2_image_left2 = load_image("Test Sprite2-left2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
image_icon = load_image("Test Sprite-icon.png.png")
image_icon2 = load_image("Test Sprite-icon2.png.png")
image_icon3 = load_image("Test Sprite-icon3.png.png")
spawn_tile = load_image("Test Sprite-icon.png.png",(TILE_SIZE,TILE_SIZE))
spawn_tile2 = load_image("Test Sprite-icon2.png.png",(TILE_SIZE,TILE_SIZE))
bg = load_image("Test Sprite-bg.png.png",(TILE_SIZE,TILE_SIZE))
player_image_jump_right = load_image("Test Sprite-jump-right.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image("Test Sprite-jump-left.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_crouch_right = load_image("Test Sprite-crouch-right.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_left = load_image("Test Sprite-crouch-left.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_right2 = load_image("Test Sprite-crouch-right2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_left2 = load_image("Test Sprite-crouch-left2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player2_image_jump_right = load_image("Test Sprite2-jump-right.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player2_image_jump_left = load_image("Test Sprite2-jump-left.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player2_image_crouch_right = load_image("Test Sprite2-crouch-right.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player2_image_crouch_left = load_image("Test Sprite2-crouch-left.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player2_image_crouch_right2 = load_image("Test Sprite2-crouch-right2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player2_image_crouch_left2 = load_image("Test Sprite2-crouch-left2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
floor_tile_image = load_image("Test Sprite Tile-legacy.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image2 = load_image("Test Sprite Tile-legacy2.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image3 = load_image("Test Sprite Tile-legacy3.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image4 = load_image("Test Sprite Tile-lava.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image5 = load_image("Test Sprite Tile-lava2.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image6 = load_image("Test Sprite Tile-lava3.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image7 = load_image("Test Sprite Tile-lava4.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image8 = load_image("Test Sprite Tile-side.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_image9 = load_image("Test Sprite Tile-side2.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagea = load_image("Test Sprite Tile-lava5.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imageb = load_image("Test Sprite Tile-lava6.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagec = load_image("Test Sprite Tile-lava7.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imaged = load_image("Test Sprite Tile-lava8.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagee = load_image("Test Sprite Tile-lava9.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagef = load_image("Test Sprite Tile-lava10.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imageg = load_image("Test Sprite Tile-lava11.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imageh = load_image("Test Sprite Tile-lava12.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagei = load_image("Test Sprite Tile-legacy4.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagej = load_image("Test Sprite-star.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagek = load_image("Test Sprite Tile-lava13.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagel = load_image("Test Sprite Tile-lava14.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagem = load_image("Test Sprite Tile-lava15.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagen = load_image("Test Sprite Tile-lava16.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imageo = load_image("Test Sprite Tile-lava17.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagep = load_image("Test Sprite Tile-lava18.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imageq = load_image("Test Sprite Tile-lava19.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imager = load_image("Test Sprite Tile-bounce.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_images = load_image("Test Sprite Tile-lava20.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imaget = load_image("Test Sprite Tile-lava21.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imageu = load_image("Test Sprite Tile-lava22.png.png",(TILE_SIZE,TILE_SIZE))
floor_tile_imagev = load_image("Test Sprite Tile-lava23.png.png",(TILE_SIZE,TILE_SIZE))
spawn_tile0 = load_image("Test Sprite-icon0.png.png",(TILE_SIZE,TILE_SIZE))
clouds1 = load_image("clouds1.png")
clouds2 = load_image("clouds2.png")
clouds3 = load_image("clouds3.png")
clouds4 = load_image("clouds4.png")
clouds5 = load_image("clouds5.png")
clouds6 = load_image("clouds6.png")
win = load_image("win.png.png",(GAME_WIDTH,GAME_HEIGHT))
win_baby = load_image("win-baby.png.png",(GAME_WIDTH,GAME_HEIGHT))
win_hot_lava = load_image("win-hot-lava.png.png",(GAME_WIDTH,GAME_HEIGHT))
win_carolina = load_image("win-carolina.png.png",(GAME_WIDTH,GAME_HEIGHT))
air = load_image("Mountains-air.png.png",(GAME_WIDTH,GAME_HEIGHT))
crown = load_image("Test Sprite Tile-crown.png.png",(TILE_SIZE,TILE_SIZE))
crown_baby = load_image("Test Sprite Tile-crown-baby.png.png",(TILE_SIZE,TILE_SIZE))
crown_hot_lava = load_image("Test Sprite Tile-crown-hot-lava.png.png",(TILE_SIZE,TILE_SIZE))
button_list = []
button_baby = load_image("button-baby.png",(128,64))
button_list.append(button_baby)
button_baby_spicy = load_image("button-baby-spicy.png",(128,64))
button_list.append(button_baby_spicy)
button_normal = load_image("button.png",(128,64))
button_list.append(button_normal)
button_hot_feet_baby = load_image("button-hot-feet-baby.png",(128,64))
button_list.append(button_hot_feet_baby)
button_hot_feet = load_image("button-hot-feet.png",(128,64))
button_list.append(button_hot_feet)
button_hot_feet_spicy = load_image("button-hot-feet-spicy.png",(128,64))
button_list.append(button_hot_feet_spicy)
hj_list = []
host = load_image("host.png",(128,64))
hj_list.append(host)
join = load_image("join.png",(128,64))
hj_list.append(join)
ln_list = []
load = load_image("load.png",(128,64))
ln_list.append(load)
new = load_image("new.png",(128,64))
ln_list.append(new)
difficulty = 2
baby_mode = False
lava_mode = False
extra_baby = False
extra_lava = 0
'''
while True:
    print()
    difficulty = int(input("How difficult do you want your game?\n1. Baby\n2. Normal\n3. Hot Lava Mode (aka Hot Feet)\n(1/2/3) "))
    if difficulty == 1 or difficulty == 2 or difficulty == 3:
        break
global baby_mode
if difficulty == 1:
    baby_mode = True
    lava_mode = False
    extra_lava = 0
    while True:
        print()
        extra_baby = int(input("How spicy do you want your baby?\n1. Normal Baby\n2. Extra Spicy Baby\n(1/2) "))
        if extra_baby == 1 or extra_baby == 2:
            break
elif difficulty == 2:
    baby_mode = False
    lava_mode = True
    extra_lava = 0
    extra_baby = 0
elif difficulty == 3:
    baby_mode = False
    lava_mode = True
    extra_baby = 0
    while True:
        #lava = input("Enable hot lava mode aka hot feet? (y/n) ")
        #if lava == "y" or lava == "yes":
        while True:
            print()
            extra_lava = int(input("How spicy do you want your hot feet?\n1. Jalapeño\n2. Habanero\n3. Carolina Reaper (WARNING: Hot feet destroy checkpoints!!!)\n(1/2/3) "))
            if extra_lava == 1 or extra_lava == 2 or extra_lava == 3:
                break
        break
        #elif lava == "n" or lava == "no":
            #lava_mode = False
            #break
'''
class Button(pygame.Rect):
    """generates the buttons

    Args:
        pygame (_type_): _description_
    """
    def __init__(self,x,y,image=None):
        pygame.Rect.__init__(self,x,y,128,64)
        self.image = image
        self.original_image = image
        self.big_image = pygame.transform.scale(image, (int(128 * 1.2), int(64 * 1.2)))
        self.hovered = False
        self.original_pos = (x, y)
'''
while True:
    print()
    hosting = input("Host or join game? (h/j) ")
    if hosting == "h" or hosting == "host":
        server_process = subprocess.Popen(["python", "server.py"])
        server_ip = "127.0.0.1"
        #print("Server started. You are hosting the game.")
        break
    elif hosting == "j" or hosting == "join":
        server_ip = input("Enter server IP: ")
        break
read_save = save.read_text()
load_save = json.loads(read_save)
if load_save is not None:
    while True:
        start_save = input("Start from last save? (y/n) ")
        if start_save == "y" or start_save == "yes":#difficulty,baby_mode,lava_mode,extra_baby,extra_lava,running
            difficulty = load_save[1]
            baby_mode = load_save[2]
            lava_mode = load_save[3]
            extra_baby = load_save[4]
            extra_lava = load_save[5]
            break
        elif start_save == "n" or start_save == "no":
            break
'''
pygame.init() #always needed to initialize pygame
window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("Celeste 2") #title of window
pygame.display.set_icon(image_icon3)
clock = pygame.time.Clock() #used for the framerate

read_save = save.read_text()
load_save = json.loads(read_save)
if load_save is not None:
    ln_coords = [(128, 208),(384, 208)]
    ln_rects = []
    for i in range(2):
        x,y = ln_coords[i]
        ln_rect = Button(x,y,ln_list[i])
        ln_rects.append(ln_rect)
    running = True
    while running:
        for button in ln_rects:
            mouse = pygame.mouse.get_pos()
            if button.collidepoint(mouse):
                if not button.hovered:
                    button.hovered = True
                    button.image = button.big_image
                    button.width,button.height = button.image.get_size()
                    button.x = button.original_pos[0]-(button.width-128)//2
                    button.y = button.original_pos[1]-(button.height-64)//2
            else:
                if button.hovered:
                    button.hovered = False
                    button.image = button.original_image
                    button.width,button.height = 128,64
                    button.x, button.y = button.original_pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                for button in ln_rects:
                    if button.collidepoint(mouse):
                        if button.original_image == load:
                            start_save = "y"
                            difficulty = load_save[1]
                            baby_mode = load_save[2]
                            lava_mode = load_save[3]
                            extra_baby = load_save[4]
                            extra_lava = load_save[5]
                            running = False
                            break
                        elif button.original_image == new:
                            start_save = "n"
                            running = False
                            break
            window.fill((0,0,0))
            for button in ln_rects:
                window.blit(button.image, (button.x, button.y))
            pygame.display.update()
            clock.tick(60)

#button_coords = [(112, 138), (288, 138), (464, 138), (112, 308), (288, 308), (464, 308)]
hj_coords = [(128, 208),(384, 208)]
hj_rects = []
for i in range(2):
    x,y = hj_coords[i]
    hj_rect = Button(x,y,hj_list[i])
    hj_rects.append(hj_rect)
running = True
while running:
    for button in hj_rects:
        mouse = pygame.mouse.get_pos()
        if button.collidepoint(mouse):
            if not button.hovered:
                button.hovered = True
                button.image = button.big_image
                button.width,button.height = button.image.get_size()
                button.x = button.original_pos[0]-(button.width-128)//2
                button.y = button.original_pos[1]-(button.height-64)//2
        else:
            if button.hovered:
                button.hovered = False
                button.image = button.original_image
                button.width,button.height = 128,64
                button.x, button.y = button.original_pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse = pygame.mouse.get_pos()
            for button in hj_rects:
                if button.collidepoint(mouse):
                    if button.original_image == host:
                        hosting = "h"
                        server_process = subprocess.Popen(["python", "server.py"])
                        server_ip = "127.0.0.1"
                        #print("Server started. You are hosting the game.")
                        running = False
                        break
                    elif button.original_image == join:
                        hosting = "j"
                        server_ip = input("Enter server IP: ")
                        running = False
                        break
        window.fill((0,0,0))
        for button in hj_rects:
            window.blit(button.image, (button.x, button.y))
        pygame.display.update()
        clock.tick(60)
if load_save is not None:
    if start_save == "n" or start_save == "no":
        button_coords = [(128, 72),(384, 72),(128, 208),(384, 208),(128, 344),(384, 344)]
        button_rects = []
        for i in range(6):
            x,y = button_coords[i]
            button_rect = Button(x,y,button_list[i])
            button_rects.append(button_rect)
        running = True
        while running:
            for button in button_rects:
                mouse = pygame.mouse.get_pos()
                if button.collidepoint(mouse):
                    if not button.hovered:
                        button.hovered = True
                        button.image = button.big_image
                        button.width,button.height = button.image.get_size()
                        button.x = button.original_pos[0]-(button.width-128)//2
                        button.y = button.original_pos[1]-(button.height-64)//2
                else:
                    if button.hovered:
                        button.hovered = False
                        button.image = button.original_image
                        button.width,button.height = 128,64
                        button.x, button.y = button.original_pos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    for button in button_rects:
                        if button.collidepoint(mouse):
                            if button.original_image == button_normal:
                                difficulty = 2
                                baby_mode = False
                                lava_mode = False
                                extra_baby = False
                                extra_lava = 0
                                running = False
                                break
                            elif button.original_image == button_baby:
                                difficulty = 1
                                baby_mode = True
                                lava_mode = False
                                extra_lava = 0
                                extra_baby = False
                                running = False
                                break
                            elif button.original_image == button_baby_spicy:
                                difficulty = 1
                                baby_mode = True
                                lava_mode = False
                                extra_baby = True
                                extra_lava = 0
                                running = False
                                break
                            elif button.original_image == button_hot_feet_baby:
                                difficulty = 3
                                baby_mode = False
                                lava_mode = True
                                extra_baby = False
                                extra_lava = 1
                                running = False
                                break
                            elif button.original_image == button_hot_feet:
                                difficulty = 3
                                baby_mode = False
                                lava_mode = True
                                extra_baby = False
                                extra_lava = 2
                                running = False
                                break
                            elif button.original_image == button_hot_feet_spicy:
                                difficulty = 3
                                baby_mode = False
                                lava_mode = True
                                extra_baby = False
                                extra_lava = 3
                                running = False
                                break
            window.fill((0,0,0))
            for button in button_rects:
                window.blit(button.image, (button.x, button.y))
            pygame.display.update()
            clock.tick(60)


class Background(pygame.Rect):
    """generates the background

    Args:
        pygame (_type_): _description_
    """
    def __init__(self):
        pygame.Rect.__init__(self,PLAYER_X,PLAYER_Y,PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT)
'''
def generate_cloud(): #unused idea
    cloud_num = random.randint(1,6)
    if cloud_num == 1:
        cloud_image = clouds1
    elif cloud_num == 2:
        cloud_image = clouds2
    elif cloud_num == 3:
        cloud_image = clouds3
    elif cloud_num == 4:
        cloud_image = clouds4
    elif cloud_num == 5:
        cloud_image = clouds5
    elif cloud_num == 6:
        cloud_image = clouds6
    cloud_width = cloud_image.get_width()
    cloud_height = cloud_image.get_height()
    cloud_x = 100
    cloud_y = random.randint(0,512)
    cloud_speed = random.randint(1,5)
    return (cloud_x,cloud_y,cloud_width,cloud_height,cloud_image,cloud_speed)
class Clouds(pygame.Rect):
    def __init__(self,cloud=generate_cloud()):
        pygame.Rect.__init__(self,cloud[0],cloud[1],cloud[2],cloud[3])
        self.image = cloud[4]
        self.speed = cloud[5]
'''
class Player(pygame.Rect):
    """player 1 and 2

    Args:
        pygame (_type_): _description_
    """
    player_animation = 0
    def __init__(self):
        """initializes player
        """
        pygame.Rect.__init__(self,PLAYER_X,PLAYER_Y,PLAYER_WIDTH,PLAYER_HEIGHT)
        self.velocity_x = 0
        self.velocity_y = 1
        self.direction = "right"
        self.jumping = False
        self.crouching = False
        self.standing_y = (GAME_HEIGHT/2)-(PLAYER_HEIGHT/2)
        self.standing_x = (GAME_WIDTH/2)-(PLAYER_WIDTH/2)
        self.crouching_y = (GAME_HEIGHT/2)-(PLAYER_CROUCH_HEIGHT/2)
        self.crouching_x = (GAME_WIDTH/2)-(PLAYER_CROUCH_WIDTH/2)
        self.crouch_jump = False
        self.player = 1
        self.jump_count = 0
        self.max_jumps = 1
    def update(self):
        """updates player's hitbox
        """
        self.rect = (self.x, self.y, self.width, self.height)
    def update_image(self):
        """updates player's animations
        """
        if self.player == 1:
            if self.crouching:
                if self.direction == "right":
                    if self.velocity_x > 0:
                        if self.player_animation >= 40//PLAYER_VELOCITY_X:
                            self.image = player_image_crouch_right2
                            self.player_animation += 1
                            if self.player_animation >= 80//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player_image_crouch_right
                            self.player_animation += 1
                    else:
                        self.image = player_image_crouch_right
                elif self.direction == "left":
                    if self.velocity_x < 0:
                        if self.player_animation >= 40//PLAYER_VELOCITY_X:
                            self.image = player_image_crouch_left2
                            self.player_animation += 1
                            if self.player_animation >= 80//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player_image_crouch_left
                            self.player_animation += 1
                    else:
                        self.image = player_image_crouch_left
            elif self.jumping:
                if self.direction == "right":
                    self.image = player_image_jump_right
                elif self.direction == "left":
                    self.image = player_image_jump_left
            else:
                if self.direction == "right":
                    if self.velocity_x > 0:
                        if self.player_animation >= 20//PLAYER_VELOCITY_X:
                            self.image = player_image_right2
                            self.player_animation += 1
                            if self.player_animation >= 40//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player_image_right
                            self.player_animation += 1
                    else:
                        self.image = player_image_right
                elif self.direction == "left":
                    if self.velocity_x < 0:
                        if self.player_animation >= 20//PLAYER_VELOCITY_X:
                            self.image = player_image_left2
                            self.player_animation += 1
                            if self.player_animation >= 40//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player_image_left
                            self.player_animation += 1
                    else:
                        self.image = player_image_left
        elif self.player == 2:
            if self.crouching:
                if self.direction == "right":
                    if self.velocity_x > 0:
                        if self.player_animation >= 40//PLAYER_VELOCITY_X:
                            self.image = player2_image_crouch_right2
                            self.player_animation += 1
                            if self.player_animation >= 80//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player2_image_crouch_right
                            self.player_animation += 1
                    else:
                        self.image = player2_image_crouch_right
                elif self.direction == "left":
                    if self.velocity_x < 0:
                        if self.player_animation >= 40//PLAYER_VELOCITY_X:
                            self.image = player2_image_crouch_left2
                            self.player_animation += 1
                            if self.player_animation >= 80//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player2_image_crouch_left
                            self.player_animation += 1
                    else:
                        self.image = player2_image_crouch_left
            elif self.jumping:
                if self.direction == "right":
                    self.image = player2_image_jump_right
                elif self.direction == "left":
                    self.image = player2_image_jump_left
            else:
                if self.direction == "right":
                    if self.velocity_x > 0:
                        if self.player_animation >= 20//PLAYER_VELOCITY_X:
                            self.image = player2_image_right2
                            self.player_animation += 1
                            if self.player_animation >= 40//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player2_image_right
                            self.player_animation += 1
                    else:
                        self.image = player2_image_right
                elif self.direction == "left":
                    if self.velocity_x < 0:
                        if self.player_animation >= 20//PLAYER_VELOCITY_X:
                            self.image = player2_image_left2
                            self.player_animation += 1
                            if self.player_animation >= 40//PLAYER_VELOCITY_X:
                                self.player_animation = 0
                        else:
                            self.image = player2_image_left
                            self.player_animation += 1
                    else:
                        self.image = player2_image_left

class Tile(pygame.Rect):
    """creates the tiles

    Args:
        pygame (_type_): _description_
    """
    def __init__(self,x,y,image=None):
        pygame.Rect.__init__(self,x,y,TILE_SIZE,TILE_SIZE)
        self.image = image
        self.lava_timer_y = 0
        self.lava_timer_x = 0
        self.timer_y = 0
        self.timer_x = 0
        self.original_image = image

def create_map():
    """creates the map
    """
    read_level = level.read_text()
    load_level = json.loads(read_level)
    for i in range(len(load_level)):
        row = load_level[i]
        for j in range(len(row)):
            if row[j] == "!":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,spawn_tile)
                tile.width = TILE_SIZE
                tile.height = TILE_SIZE
                tiles.append(tile)
            if row[j] == "@":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,bg)
                tile.width = TILE_SIZE
                tile.height = TILE_SIZE
                tiles.append(tile)
            if row[j] == "#":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,spawn_tile0)
                tile.width = TILE_SIZE
                tile.height = TILE_SIZE
                tiles.append(tile)
            if row[j] == "$":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                if difficulty == 1:
                    win_tile = crown_baby
                elif difficulty == 2:
                    win_tile = crown
                elif difficulty == 3:
                    win_tile = crown_hot_lava
                else:
                    print("Error with gamemode selection")
                    quit()
                tile = Tile(x,y,win_tile)
                tile.width = TILE_SIZE
                tile.height = TILE_SIZE
                tiles.append(tile)
            if row[j] == "1":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image)
                tiles.append(tile)
            elif row[j] == "2":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image2)
                tiles.append(tile)
            elif row[j] == "3":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image3)
                tiles.append(tile)
            elif row[j] == "4":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image4)
                tiles.append(tile)
            elif row[j] == "5":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image5)
                tiles.append(tile)
            elif row[j] == "6":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image6)
                tiles.append(tile)
            elif row[j] == "7":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image7)
                tiles.append(tile)
            elif row[j] == "8":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image8)
                tiles.append(tile)
            elif row[j] == "9":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_image9)
                tiles.append(tile)
            elif row[j] == "a":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagea)
                tiles.append(tile)
            elif row[j] == "b":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imageb)
                tiles.append(tile)
            elif row[j] == "c":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagec)
                tiles.append(tile)
            elif row[j] == "d":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imaged)
                tiles.append(tile)
            elif row[j] == "e":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagee)
                tiles.append(tile)
            elif row[j] == "f":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagef)
                tiles.append(tile)
            elif row[j] == "g":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imageg)
                tiles.append(tile)
            elif row[j] == "h":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imageh)
                tiles.append(tile)
            elif row[j] == "i":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagei)
                tiles.append(tile)
            elif row[j] == "j":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagej)
                tiles.append(tile)
            elif row[j] == "k":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagek)
                tiles.append(tile)
            elif row[j] == "l":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagel)
                tiles.append(tile)
            elif row[j] == "m":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagem)
                tiles.append(tile)
            elif row[j] == "n":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagen)
                tiles.append(tile)
            elif row[j] == "o":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imageo)
                tiles.append(tile)
            elif row[j] == "p":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagep)
                tiles.append(tile)
            elif row[j] == "q":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imageq)
                tiles.append(tile)
            elif row[j] == "r":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imager)
                tiles.append(tile)
            elif row[j] == "s":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_images)
                tiles.append(tile)
            elif row[j] == "t":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imaget)
                tiles.append(tile)
            elif row[j] == "u":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imageu)
                tiles.append(tile)
            elif row[j] == "v":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x,y,floor_tile_imagev)
                tiles.append(tile)

def check_tile_collision():
    """detects player collision with tile

    Returns:
        either object or None: if th eplayer collides, it returns the player, otherwise it returns None
    """
    if player.colliderect(player2):
        return player2
    for tile in tiles:
        if player.colliderect(tile):
            return tile
    return None
def check_lava_collision():
    """detects lava collisions
    """
    global coyote_lava
    global joy_restart
    global tiles
    for tile in tiles:
        if lava_rect.colliderect(tile) or lava_rect2.colliderect(tile) or keys[pygame.K_r] or joy_restart:
            if keys[pygame.K_r] or joy_restart or tile.image == floor_tile_image4 or tile.image == floor_tile_image5 or tile.image == floor_tile_image6 or tile.image == floor_tile_image7 or tile.image == floor_tile_imagea or tile.image == floor_tile_imageb or tile.image == floor_tile_imagec or tile.image == floor_tile_imaged or tile.image == floor_tile_imagee or tile.image == floor_tile_imagef or tile.image == floor_tile_imageg or tile.image == floor_tile_imageh or tile.image == floor_tile_imagek or tile.image == floor_tile_imagel or tile.image == floor_tile_imagem or tile.image == floor_tile_imagen or tile.image == floor_tile_imageo or tile.image == floor_tile_imagep or tile.image == floor_tile_imageq or tile.image == floor_tile_images or tile.image == floor_tile_imaget or tile.image == floor_tile_imageu or tile.image == floor_tile_imagev:
                if coyote_lava >= 32 or keys[pygame.K_r] or joy_restart:
                    coyote_lava = 0
                    player.velocity_x = 0
                    player.velocity_y = 0
                    for i in tiles:
                        if i.image == spawn_tile2:
                            no_checkpoints = False
                            spawn_x = i.x-(10*32)+16#+random.randint(0,TILE_SIZE)
                            spawn_y = i.y-(10*32)+TILE_SIZE+16+3#-player.height
                            for j in tiles:
                                j.x -= spawn_x
                                j.y -= spawn_y
                            break
                        else:
                            no_checkpoints = True
                    if no_checkpoints:
                        for i in tiles:
                            if i.image == spawn_tile0:
                                spawn_x = i.x-(10*32)+16#+random.randint(0,TILE_SIZE)
                                spawn_y = i.y-(10*32)+TILE_SIZE+16+3-PLAYER_HEIGHT
                                for j in tiles:
                                    j.x -= spawn_x
                                    j.y -= spawn_y
                                break
                    player.jump_count = 0
                    joy_restart = False
                    if lava_mode:
                        for tile in tiles:
                            if tile.image == floor_tile_image4:
                                tile.image = tile.original_image
                                tile.lava_timer_x = 0
                                tile.lava_timer_y = 0
                                tile.timer = 0
                        lava_tile_x.clear()
                else:
                    coyote_lava += 1
                    break
    for tile in tiles:
        if lava_rect.colliderect(tile):
            if tile.image == floor_tile_image4 or tile.image == floor_tile_image5 or tile.image == floor_tile_image6 or tile.image == floor_tile_image7 or tile.image == floor_tile_imagea or tile.image == floor_tile_imageb or tile.image == floor_tile_imagec or tile.image == floor_tile_imaged or tile.image == floor_tile_imagee or tile.image == floor_tile_imagef or tile.image == floor_tile_imageg or tile.image == floor_tile_imageh or tile.image == floor_tile_imagek or tile.image == floor_tile_imagel or tile.image == floor_tile_imagem or tile.image == floor_tile_imagen or tile.image == floor_tile_imageo or tile.image == floor_tile_imagep or tile.image == floor_tile_imageq or tile.image == floor_tile_images or tile.image == floor_tile_imaget or tile.image == floor_tile_imageu or tile.image == floor_tile_imagev:
                touching_tile_x = True
                break
            else:
                touching_tile_x = False
        else:
            touching_tile_x = False
    for tile in tiles:
        if lava_rect2.colliderect(tile):
            if tile.image == floor_tile_image4 or tile.image == floor_tile_image5 or tile.image == floor_tile_image6 or tile.image == floor_tile_image7 or tile.image == floor_tile_imagea or tile.image == floor_tile_imageb or tile.image == floor_tile_imagec or tile.image == floor_tile_imaged or tile.image == floor_tile_imagee or tile.image == floor_tile_imagef or tile.image == floor_tile_imageg or tile.image == floor_tile_imageh or tile.image == floor_tile_imagek or tile.image == floor_tile_imagel or tile.image == floor_tile_imagem or tile.image == floor_tile_imagen or tile.image == floor_tile_imageo or tile.image == floor_tile_imagep or tile.image == floor_tile_imageq or tile.image == floor_tile_images or tile.image == floor_tile_imaget or tile.image == floor_tile_imageu or tile.image == floor_tile_imagev:
                touching_tile_x2 = True
                break
            else:
                touching_tile_x2 = False
        else:
            touching_tile_x2 = False
    if not touching_tile_x and not touching_tile_x2:
        if coyote_lava != 0:
            coyote_lava -= 1

def check_tile_collision_x():
    """detects collisions on the x-axis
    """
    global lava_tile_x
    check_lava_collision()
    tile = check_tile_collision()
    adjust_bg = False
    '''
    if (left.colliderect(player2) or right.colliderect(player2)) and player.velocity_x == 0 and not feet_rect.colliderect(player2):# and player2.velocity_x != 0:
        adjust_bg = True
        check_tile_collision_y()
        if right.colliderect(player2):
            player.x = player2.x-player.width-1
        elif left.colliderect(player2):
            player.x = player2.x+player2.width+1
    '''
    if tile is not None and lava_mode and tile.image != spawn_tile0 and tile.image != floor_tile_imagej and tile.timer_x == 0 and tile.image != crown and tile.image != crown_baby and tile.image != crown_hot_lava:
        if extra_lava == 3:
            lava_tile_x.append(tile)
        elif (extra_lava == 1 or extra_lava == 2) and tile.image != spawn_tile0 and tile.image != spawn_tile and tile.image != spawn_tile2 and tile.image != floor_tile_imagej and tile.timer_x == 0 and tile.image != crown and tile.image != crown_baby and tile.image != crown_hot_lava:
            lava_tile_x.append(tile)
    if tile is not None and player.velocity_x != 0:
        adjust_bg = True
        if player.velocity_x < 0 or player.direction == "left":
            player.x = tile.x+(TILE_SIZE if tile.x != player2.x else player2.width)
        elif player.velocity_x > 0 or player.direction == "right":
            player.x = tile.x-player.width
        player.velocity_x = 0
    if adjust_bg:
        if player.x > player.standing_y:
            for tile in tiles:
                tile.x -= player.x-player.standing_x
            player.x -= player.x-player.standing_x
        else:
            for tile in tiles:
                tile.x += player.x-player.standing_x
            player.x += player.x-player.standing_x
    for tile in lava_tile_x:
        tile.timer_x += 1
        if tile.timer_x >= 22 and extra_lava == 1:
            tile.image = floor_tile_image4
            tile.timer_x = 0
            lava_tile_x.remove(tile)
        elif tile.timer_x >= 11 and (extra_lava == 2 or extra_lava == 3):
            tile.image = floor_tile_image4
            tile.timer_x = 0
            lava_tile_x.remove(tile)

    #player.x = player.crouching_x if player.crouching else player.standing_x
def check_tile_collision_y():
    """detects collisions on the y-axis
    """
    global BACKGROUND_Y
    global PLAYER_VELOCITY_Y
    global CROUCH_FRICTION
    global lava_tile_y
    global coyote_time
    global crouch_jump2
    global won
    check_lava_collision()
    feet_rect.height = player.height+2
    left.height = player.height-4
    right.height = player.height-4
    if player2.crouching:
        feet_rect2.height = TILE_SIZE+2
        feet_rect2.y = player2.y
    else:
        feet_rect2.height = player2.height+2
        feet_rect2.y = player2.y
    lava_rect.height = player.height+12
    num_touch = 0
    for num in tiles:
        if feet_rect.colliderect(num):
            num_touch += 1
    for tile in tiles:
        if up.colliderect(tile):
            player.y = tile.y+tile.height
            player.velocity_y = 0
            if feet_rect.colliderect(player2):
                player.crouching = True
        elif down.colliderect(tile):
            player.y = tile.y-player.height
            player.velocity_y = 0
            player.jumping = False
            player.jump_count = 0
        elif num_touch == 0:# and player.velocity_y != 0:
            if down.colliderect(player2):
                player.y = player2.y-player.height
                player.velocity_y = 0
                player.jumping = False
                player.jump_count = 0
            elif up.colliderect(player2):
                player.velocity_y = 0
                player.y = player2.y+player2.height
        if feet_rect.colliderect(tile) or feet_rect.colliderect(player2):
            if lava_mode and tile.image != spawn_tile0 and tile.image != floor_tile_imagej and feet_rect.colliderect(tile) and tile.timer_y == 0 and tile.image != crown and tile.image != crown_baby and tile.image != crown_hot_lava:
                if extra_lava == 3:
                    lava_tile_y.append(tile)
                elif (extra_lava == 1 or extra_lava == 2) and tile.image != spawn_tile and tile.image != spawn_tile2 and tile.image != spawn_tile0 and tile.image != floor_tile_imagej and feet_rect.colliderect(tile) and tile.timer_y == 0 and tile.image != crown and tile.image != crown_baby and tile.image != crown_hot_lava:
                    lava_tile_y.append(tile)
            if tile.image == spawn_tile or tile.image == spawn_tile0:
                for i in tiles:
                    if i.image == spawn_tile2:
                        i.image = spawn_tile
                if tile.image == spawn_tile:
                    tile.image = spawn_tile2
                else:
                    tile.image = spawn_tile0
                '''
                for i in tiles:
                        if i.image == spawn_tile2:
                            no_checkpoints = False
                            spawn_x = i.x-(10*32)+16#+random.randint(0,TILE_SIZE)
                            spawn_y = i.y-(10*32)+TILE_SIZE+16+3#-player.height
                            for j in tiles:
                                j.x -= spawn_x
                                j.y -= spawn_y
                            break
                        else:
                            no_checkpoints = True
                '''
                for i in tiles:
                    if i.image == spawn_tile0:
                        spawn_x = i.x-(10*32)+16
                        spawn_y = i.y-(10*32)+TILE_SIZE+16+3
                save_list = [(spawn_x,spawn_y),difficulty,baby_mode,lava_mode,extra_baby,extra_lava,player.max_jumps]
                save_dump = json.dumps(save_list)
                save.write_text(save_dump)
            elif tile.image == floor_tile_imagej:
                if player.max_jumps != 2 and PLAYER_VELOCITY_Y != -12.1:
                    print()
                    print("Double jump unlocked!")
                    player.max_jumps = 2
                    PLAYER_VELOCITY_Y = -19
            elif tile.image == floor_tile_imager:
                for tile in tiles:
                    tile.y -= PLAYER_VELOCITY_Y*1.5
                player.velocity_y = PLAYER_VELOCITY_Y*1.5
                player.jumping = True
                player.jump_count += 1
            elif tile.image == crown or tile.image == crown_baby or tile.image == crown_hot_lava:# and not won:
                if extra_lava != 3:
                    print("You win idiot")
                else:
                    print("You win")
                won = True
            touching_tile_feet = True
            break
        else:
            touching_tile_feet = False
    for tile in lava_tile_y:
        tile.timer_y += 1
        if tile.timer_y >= 22 and extra_lava == 1:
            tile.image = floor_tile_image4
            tile.timer_y = 0
            lava_tile_y.remove(tile)
        elif tile.timer_y >= 11 and (extra_lava == 2 or extra_lava == 3):
            tile.image = floor_tile_image4
            tile.timer_y = 0
            lava_tile_y.remove(tile)
    tile = check_tile_collision()
    if tile is not None:
        coyote_time = 0
        if player.velocity_y < 0:
            player.jumping = True
            player.velocity_y = 0
            player.y = tile.y+tile.height
        elif player.velocity_y > 0:
            CROUCH_FRICTION = 1
            player.y = tile.y - player.height
            if player.jumping:
                player.jumping = False
                player.jump_count = 0
            player.velocity_y = 0
    elif not touching_tile_feet:
        if coyote_time >= 8 and not player.jumping:
            player.jumping = True
            coyote_time = 0
        elif not player.jumping:
            coyote_time += 1
            #player.velocity_y = 0
    else:
        coyote_time = 0
    if player2.crouching and feet_rect.colliderect(player2) and not crouch_jump2:
        crouch_jump2 = True
    elif not player2.crouching and feet_rect.colliderect(player2) and crouch_jump2:
        crouch_jump2 = False
        for tile in tiles:
            tile.y -= PLAYER_VELOCITY_Y
        player.velocity_y = PLAYER_VELOCITY_Y
        player.jumping = True
        player.jump_count += 1
    feet_rect.y = player.crouching_y if player.crouching else player.standing_y

def move():
    """moves the player according to their inputs
    """
    global BACKGROUND_Y
    global BACKGROUND_X
    #y movement
    if player.jumping and player.velocity_y < 500:
        player.velocity_y += GRAVITY
    if player2.crouching:
        player2.y -= 13
    player.velocity_y = round(player.velocity_y,1)
    check_lava_collision()
    check_tile_collision_y()
    player.y += player.velocity_y
    for tile in tiles:
        if tile.image == bg:
            BACKGROUND_Y = tile.y/25#+1024
            BACKGROUND_X = tile.x/25+128
    BACKGROUND_Y = round(BACKGROUND_Y,1)
    check_tile_collision_y()
    if not player.crouching:
        while player.y != player.standing_y:
            if player.y > player.standing_y:
                player.y -= 1
                for tile in tiles:
                    tile.y -= 1
            else:
                player.y += 1
                for tile in tiles:
                    tile.y += 1
    else:
        while player.y != player.crouching_y:
            if player.y > player.crouching_y:
                player.y -= 1
                for tile in tiles:
                    tile.y -= 1
            else:
                player.y += 1
                for tile in tiles:
                    tile.y += 1
    #x movement
    if abs(player.velocity_x) <= FRICTION:
        player.velocity_x = 0
    elif player.velocity_x > 0:
        player.velocity_x -= FRICTION
    elif player.velocity_x < 0:
        player.velocity_x += FRICTION
    player.x += player.velocity_x
    check_lava_collision()
    check_tile_collision_x()
    for tile in tiles:
        tile.x -= player.velocity_x
    check_tile_collision_x()
    player.x = player.crouching_x if player.crouching else player.standing_x
    if player.crouching:
        feet_rect.x = player.crouching_x+2
        feet_rect.y = player.crouching_y
        lava_rect.x = player.crouching_x+(player.width/2)-3
        lava_rect.y = player.crouching_y-2
        lava_rect2.x = player.crouching_x-2
        lava_rect2.y = player.crouching_y+(player.height/2)-5
        down.y = player.y+player.height-2
        up.y = player.y
        left.y = player.y+2
        right.y = player.y+2
    else:
        feet_rect.x = player.standing_x+2
        feet_rect.y = player.standing_y
        lava_rect.x = player.standing_x+(player.width/2)-3
        lava_rect.y = player.standing_y-2
        lava_rect2.x = player.standing_x-2
        lava_rect2.y = player.standing_y+(player.height/2)-5
        down.y = player.y+player.height-2
        up.y = player.y
        left.y = player.y+2
        right.y = player.y+2
    player.y = player.crouching_y if player.crouching else player.standing_y

def read_pos(str):
    """gets the player's position for player 2

    Args:
        str (str): n.getPos()

    Returns:
        None or x,y,v,crouch: Returns the player's x, y, their x velocity, and iof they are crouching
    """
    s = str.strip()
    parts = s.split(",")
    if len(parts) != 4:
        print(f"error: {repr(s)}")
        return None
    x_str,y_str,v_str,crouch_str=parts
    try:
        x = int(x_str)
        y = int(y_str)
        v = float(v_str)
        crouch = (crouch_str == "True")
    except ValueError:
        print(f"error: {parts}")
        return None
    return x, y, v, crouch

def make_pos(tup):
    """formats the player's position

    Args:
        tup (tup): player values

    Returns:
        str: returns neatly formatted str with all player values
    """
    return f"{tup[0]},{tup[1]},{tup[2]},{tup[3]}"

def draw():
    """makes everything show up on screen
    """
    global BACKGROUND_Y
    global baby_mode
    global debug
    global cheat
    #window.fill("blue")
    #window.fill("#54de9e")
    #window.fill((84,222,158))
    background_y = BACKGROUND_Y
    background_x = BACKGROUND_X
    window.fill((20,18,167))#(4,233,255))#(20,18,167))
    window.blit(air,(0,0))
    background_y = round(BACKGROUND_Y/5,1)+7
    background_x = round(BACKGROUND_X/5,1)-25
    window.blit(background_image4, (background_x,background_y))
    background_y = round(BACKGROUND_Y/4,1)-128
    background_x = round(BACKGROUND_X/4,1)
    round(background_y,1)
    window.blit(background_image3, (background_x,background_y))
    background_y = BACKGROUND_Y-64
    background_y = round(background_y/2,1)-224
    background_x = BACKGROUND_X
    background_x = round(background_x/2,1)-145
    round(background_y,1)
    window.blit(background_image, (background_x,background_y))
    background_y = BACKGROUND_Y
    background_y = background_y-206
    background_x = BACKGROUND_X
    background_x = background_x-206
    round(background_y,1)
    window.blit(background_image0, (background_x,background_y))
    background_y = BACKGROUND_Y-128
    background_y = background_y*2
    background_x = BACKGROUND_X-325
    background_x = background_x*2
    round(background_y,1)
    window.blit(background_image2, (background_x,background_y))
    if baby_mode:
        for tile in tiles:
            if extra_baby:
                if tile.image == spawn_tile or tile.image == spawn_tile2:
                    tile.image = floor_tile_image
            if tile.image == floor_tile_image4 or tile.image == floor_tile_image5 or tile.image == floor_tile_image6 or tile.image == floor_tile_image7 or tile.image == floor_tile_imagea or tile.image == floor_tile_imageb or tile.image == floor_tile_imagec or tile.image == floor_tile_imaged or tile.image == floor_tile_imagee or tile.image == floor_tile_imagef or tile.image == floor_tile_imageg or tile.image == floor_tile_imageh or tile.image == floor_tile_imagek or tile.image == floor_tile_imagel or tile.image == floor_tile_imagem or tile.image == floor_tile_imagen or tile.image == floor_tile_imageo or tile.image == floor_tile_imagep or tile.image == floor_tile_imageq or tile.image == floor_tile_images or tile.image == floor_tile_imaget or tile.image == floor_tile_imageu or tile.image == floor_tile_imagev:
                tile.image = floor_tile_image
                tile.original_image = floor_tile_image
        baby_mode = False
    for tile in tiles:
        window.blit(tile.image, tile)
    player2.update_image()
    window.blit(player2.image,player2)
    player.update_image()
    window.blit(player.image,player)
    if keys[pygame.K_l]:
        cheat = True
    if keys[pygame.K_o]:
        debug = True
    if keys[pygame.K_p]:
        debug = False
        cheat = False
    if debug:
        pygame.draw.rect(window, (255, 255, 255), player, 2)
        pygame.draw.rect(window, (255, 255, 255), player2, 2)
        pygame.draw.rect(window, (255, 0, 0), feet_rect, 2)
        pygame.draw.rect(window, (0, 0, 0), down, 2)
        pygame.draw.rect(window, (0, 0, 0), up, 2)
        pygame.draw.rect(window, (0, 0, 0), left, 2)
        pygame.draw.rect(window, (0, 0, 0), right, 2)
        pygame.draw.rect(window, (255, 0, 0), feet_rect2, 2)
        pygame.draw.rect(window, (0, 255, 0), lava_rect, 2)
        pygame.draw.rect(window, (0, 255, 0), lava_rect2, 2)
    if cheat:
        player.jump_count = 0
    if won:
        window.fill((0,0,0))
        if difficulty == 1:
            window.blit(win_baby,(0,-25))
        elif difficulty == 2:
            window.blit(win_hot_lava,(0,-25))
        elif difficulty == 3:
            if extra_lava == 3:
                window.blit(win,(0,0))
            else:
                window.blit(win_carolina,(0,-25))
def check_crouch():
    """checks if the player is crouching
    """
    global CROUCH_FRICTION
    global force_crouch
    collide_crouch = pygame.Rect(player.x, player.y-(PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT), PLAYER_WIDTH, PLAYER_HEIGHT)
    if player.crouching or feet_rect.colliderect(player2):
        for tile in tiles:#32 crouch 58 tall
            if collide_crouch.colliderect(tile):
                CROUCH_FRICTION = 2
                player.width = PLAYER_CROUCH_WIDTH
                player.height = PLAYER_CROUCH_HEIGHT
                player.crouching = True
                force_crouch = True
                break
            else:
                force_crouch = False
def delete_tile(x,y):
    """deletes tiles

    Args:
        x (int): x value of deleted tile
        y (int): y value of deleted tile
    """
    global tiles
    for tile in tiles:
        if tile.x == x and tile.y == y:
            tiles.remove(tile)
            break
#start game
print("\nController Controls:\nLeft Joystick: Move\nA Button: Jump\nB/X Button: Crouch\nY Button: Restart Level\n\nKeyboard Controls:\nA/LEFT ARROW: Left\nD/RIGHT ARROW: Right\nW/UP ARROW/SPACE: Jump\nS/DOWN ARROW: Crouch\nR: Restart Level\n")#\nL: Enable Cheat Mode\nO: Enable Debug Mode\nP: Disable Debug/Cheat Mode")
level_list = []
rand_int = 0
for i in range(48):
    level_str = ""
    for j in range(48):
        rand_int = random.randint(0,47-i) #generate random map
        if i == 24 and j == 24:
            level_str += "2"
            continue
        if rand_int == 0:
            level_str += "1"
        else:
            level_str += "0"
    level_list.append(level_str)
test_map0 = ["00000000000000000000000000000000000000000000000000000000000000001", 
            "00000000000000000000000000000000000000000000001000000000000000001", 
            "0000000000000000000000!0001000000000000000000010000010000100001!4", 
            "00000000000001000010000000000010001000000000001100000000000000004", 
            "@0000000000010000000000100001000000000000001001000000000000001004", 
            "00000000000000000000000000000000000000001001000000000000000000004", 
            "0000000000#0000000000000000001010!0001001001000000000000000010004", 
            "5555h111111111114141414141010101410141414141414100000000000000014", 
            "iiiii822222222222222222222020202220222222222222200000000000100004", 
            "33333333333333333333333333030303330333333333333310000000000000004", 
            "33333333333333333333333333000000000333333333333300000000001000004", 
            "33333333333333333333333333030303330333333333333300000000000000004", 
            "33333333333333333333333333030303330333333333333310000000010000004", 
            "33333333333333333333333333030303330333333333333300000000000000004",
            "00000000000000000000000000404040000000000000000000000000100000004",
            "00000000000000000000000000000000000000000000000010000000000000004",
            "00000000000000000000000000000000000000000000000000000001000000004",
            "00001000000010000000000000000000000000100000000000000000000000004",
            "!0000000100000000111000000000000011000000000010010000010000000004",
            "00000000000000100000000100000!00000000000000000000000000000000004",
            "00001000000000000000000000000000000100000000100000000100000000004",
            "00000000001000000000000000000000000000000000000010000000000000004",
            "01000000000000000000111000000000000000000000000000001000000000004",
            "00000000011100000000000000001110000100001000001000000000000000004",
            "00011000000000000100000000000000000000000000000010010000000000004",
            "00000000000000000000000000000000100000000000000000000000000000004",
            "00011100000000001111000000110000000000100001100000100000000000004",
            "00000000001000000000000001000000000001000000000010000000000000004",
            "00000010000100000000001000000000100000000010000000000000000000004",
            "00000000000000000000000000000100000100000000000000000000000000004",
            "00100000000000001111111000111000000000110000100110000000000000004",
            "00000000000000000000000000000000000000000000000000000000000000004",
            "0000000000000000000000000000000000000000000000000000000000000004",
            "j00000000000000000000000000000000000000000000000000000000000004",
            "44444444444444444444444444444444444444444444444444444444444444"]
test_map = [
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "4$40000000000000000000000000000",
    "4440000000000000000000000000000",
    "0400000000000000000000000000000",
    "0400000000000000000000000000000",
    "0400000000000000000000000000000",
    "0414000000000000000000000000000",
    "0444000000000000000000000000000",
    "0004000000000000000000000000000",
    "0004000000000000000000000000000",
    "0004000000000000000000000000000",
    "0004140000000000000000000000000",
    "0004440000000000000000000000000",
    "0000040000000000000000000000000",
    "0000040000000000000000000000000",
    "0000040000000000000000000000000",
    "0000041400000000000000000000000",
    "0000044400000000000000000000000",
    "0000000400000000000000000000000",
    "0000000400000000000000000000000",
    "0000000400000000000000000000000",
    "0000000414000000000000000000000",
    "0000000444000000000000000000000",
    "0000000004000000000000000000000",
    "0000000004000000000000000000000",
    "0000000004000000000000000000000",
    "0000000004140000000000000000000",
    "0000000004440000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000041400000000000000000",
    "0000000000044400000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000414000000000000000",
    "0000000000000444000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000004140000000000000",
    "0000000000000004440000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000041400000000000",
    "0000000000000000044400000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000414000000000",
    "0000000000000000000444000000000",
    "0000000000000000000000000000000",
    "0000004400000000000000000000000",
    "0000004000000000000000000000000",
    "0000004000000000011!11000000000",
    "000000410000000000utt1000000000",
    "0000004t4000000000044t000000000",
    "0000004000000000000444000000000",
    "0000004000000000000044000000000",
    "0000004100000000000044000000000",
    "0000004t00000000000004000000000",
    "0004444400000000000004000000000",
    "0004000000000000040004000000000",
    "0004000000000000100004000000000",
    "0004001000000000000004000000000",
    "000400t000000000000004000000000",
    "0004004000000000000004000000000",
    "0000004000000000000004000000000",
    "0000004000000000000000000000000",
    "000!004000000000000000000000000",
    "000t004000000000000000000000000",
    "1004004000004000000004000000000",
    "4444444400044000000004400000000",
    "0000000000044000000004400000000",
    "0000000000444400000004440000000",
    "0000000004444440000004444000000",
    "11gq44qh1gq44qh11110044441111!1",
    "222244222224422222t004444222222",
    "3333443333344333334004444333333",
    "0003443000344300000000444300000",
    "0000440000044000000000044000000",
    "0000440000044000000400044000000",
    "0000440000044000000000044000000",
    "0000440000044000000000044000000",
    "00004400000440000000000440000000000000000000",
    "000044000004400000010004400000000000000000000",
    "00004000000440000000000000000000000000000000000004",
    "000000000004400000000000000000000000000000000004!4",
    "00000000000040000000000001000000000000000400000444",
    "000000000000000000000000000000000004",
    "0000040000000000000000000000000",
    "0000440000040000000000000000040",
    "000044000004400000000000000000000000000000000004",
    "000044000004400000000000000000000000000000000004",
    "000044000004400000000000000000000000000000000004",
    "011144!1gqqqqqqqqqqqqqqqqqq44qqqqqqq4444qqqqqq444",
    "00114411111111111111111111144111111140001111114",
    "000244200022220002222000022400000222400002222",
    "000004000003300000330000003a0000003300300033",
    "0000000000033000003300000033!00000300003003303",
    "0410000010003000003300000033000000300000003",
    "0000000000000000000300000033000000030000003",
    "00000000000000010000000000030000000000000003",
    "00000000000000000000000100000011",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000001",
    "!111000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000001",
    "0000000004000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000001",
    "0000000000000000000000000000000",
    "0000000000000000000000414000000",
    "0000041400000041400000444000000",
    "0000044400000044400000000000000",
    "0000000000000000000000000000000",
    "1000000000000000000000000000000",
    "4000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0004000040004000400000000000000",
    "0040000400000000000040000000000",
    "!000000000000000000000000400000",
    "0000010000100010001000100000104",
    "0000000000000000000000000000404",
    "0000000000000000000000000000004",
    "0000000000000000000000000000004",
    "0000000000000000000000000000000",
    "0000000000000000000000000000011",
    "0000000000000000000000004000000",
    "0000000000000000000000000000000",
    "00000000000001!1100000000000000",
    "0000000000000000000000400000000",
    "0000040000000000000001400000001",
    "0000001000000000000000400000000",
    "0000000000000000000000400000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000100000410000000000001",
    "0000000000000000000000001000000",
    "0000000000000000000000000000000",
    "0000000000100000000000000000000",
    "0000000000000000000000000000000",
    "00000000000000000000000000000100000000!",
    "0000000400000000000004144000000",
    "0000004414000000000000000000000",
    "0000000000000000040000000000000",
    "0000000000000004144400000000010",
    "0000000041000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000010",
    "0000000000000000000000000000000",
    "0000000001r00000000000000000000",
    "00000000000000000000!0000000000",
    "0000000000000000000000000000010",
    "0000000000000414000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000001j00000000010",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000001110000000000000000",
    "0000000000000000000000000000010",
    "0000000000000000000000000000000",
    "0000000001000000010000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000010",
    "4000011100000000001411000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "!000000000000000000000000411000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0001000100000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000001000100000000000000",
    "0000000000000000000041000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000010000100",
    "0000001000000000000000000000000",
    "0000001000000400000000000000000",
    "0000001000004440000000000000010",
    "000000100001gqh@00000111gqqh111",
    "0000002000022222000002222222222",
    "0r000030000333330000033333333330001",
    "01!00000000333330000033333333330001!1",
    "0000000000000000000000000000000",
    "0000001100000000000000000000000",
    "0000000000110011000001110000000",
    "00000000000000000000000000001!1",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0001140000000000000000000001100",
    "0001000000000000000000000000000",
    "0001000000000000000000000000000",
    "!101000001000000000000000000011",
    "0001000000000000000000000000000",
    "0001000000000014410000000000000",
    "0011100000000000000000110001100",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "1100000000000000000000000000000",
    "0000100000000000000000000000000",
    "0000100000000000000000000000000",
    "0000100000000000000000000000000",
    "0000110001100000000000000000000",
    "0000000000000011000140011000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "000000000000000000000000011000!",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000110001000000",
    "0001100010001000100000000000000",
    "0001000000000000000000000000000",
    "0001000000000000000000000000000",
    "01!1000000000000000000000000000",
    "0000000000000000000000000000000",
    "0000000000000000000000000000000",
    "11000000000000000000000000111#1",
    "1100000000000000000011000011111",
    "1100001111000111000011000011111",
    "11r44411114441114444114444111114444444444",
    "iiiqqqiiiiqqqiiiqqqqiiqqqqiiiiiqqqqqqqqqq",
    "22222222222222222222222222222222222222222",
    "33333333333333333333333333333333333333333",
    "33333003333330033333300333333003333330000",
    "33330000333300003333000033330000333300000",
    "33330000333300003333000033330000333300000",
    "03300000033000000330000003300000033000000",
    "03000000033000000330000003000000033000000",
    "03000000033000000030000003000000033000000",
    "00000000030000000030000000000000003000000",
]

level_dump = json.dumps(test_map)
level.write_text(level_dump)
global  coyote_time
coyote_time = 0
global tiles
tiles = []
create_map()
n = Network(server_ip)
if hosting == "j" or hosting == "join":
    print("Connected to server")
startPos = read_pos(n.getPos())
player2 = Player()
player2.player = 2
player2.direction = "right"
player2.x = startPos[0]
player2.y = startPos[1]
player = Player()
player.width = PLAYER_WIDTH
player.player = 1
read_level = level.read_text()
load_level = json.loads(read_level)
background = Background()
global time_walking
global force_crouch
force_crouch = False
feet_rect = Player()
feet_rect.x = player.standing_x+2
feet_rect.y = player.standing_y
feet_rect.height = PLAYER_HEIGHT+2
feet_rect.width = PLAYER_WIDTH-4
lava_rect = Player()
lava_rect.x = player.standing_x+(player.width/2)-3
lava_rect.y = player.standing_y-2
lava_rect.height = PLAYER_HEIGHT+12
lava_rect.width = 6
lava_rect2 = Player()
lava_rect2.x = player.standing_x+(player.width/2)-4
lava_rect2.y = player.standing_y+(player.height/2)-5
lava_rect2.height = 10
lava_rect2.width = PLAYER_WIDTH+4
feet_rect2 = Player()
feet_rect2.x = player2.standing_x+2
feet_rect2.y = player2.standing_y
feet_rect2.height = player2.height+2
feet_rect2.width = player2.width-4
down = Player()
down.x = player.standing_x+(player.width/2)-3
down.y = player.y+player.height-2
down.height = 2
down.width = 6
up = Player()
up.x = player.standing_x+(player.width/2)-3
up.y = player.y
up.height = 2
up.width = 6
left = Player()
left.x = player.x-2
left.y = player.y+2
left.height = player.height-4
left.width = 2
right = Player()
right.x = player.x+player.width
right.y = player.y+2
right.height = player.height-4
right.width = 2
touching_tile_buffer = False
player2_crouching = False
global debug
debug = False
global cheat
cheat = False
global coyote_lava
coyote_lava = 0
global crouch_jump2
crouch_jump2 = False
joy_jump = False
joy_crouch = False
joy_left = False
joy_right = False
global joy_restart
joy_restart = True
button_crouch = False
global lava_tile_x
lava_tile_x = []
global lava_tile_y
lava_tile_y = []
global won
won = False
joysticks = []
keys = pygame.key.get_pressed()
for tile in tiles:
    if tile.image == spawn_tile2:
        tile.image == spawn_tile
if load_save is not None:
    if start_save == "n" or start_save == "no":
        joy_restart = True
        for tile in tiles:
            if tile.image == spawn_tile0:
                spawn_x = tile.x-(10*32)+16
                spawn_y = tile.y-(10*32)+TILE_SIZE+16+3+PLAYER_HEIGHT
                for i in tiles:
                    i.x -= spawn_x
                    i.y -= spawn_y
                break
    elif start_save == "y" or start_save == "yes":
        player.max_jumps = load_save[6]
        check_lava_collision()
        for tile in tiles:
            tile.x += load_save[0][0]
            tile.y += load_save[0][1]-PLAYER_HEIGHT-3
else:
    joy_restart = True
    for tile in tiles:
        if tile.image == spawn_tile0:
            spawn_x = tile.x-(10*32)+16
            spawn_y = tile.y-(10*32)+TILE_SIZE+16+3+PLAYER_HEIGHT
            for i in tiles:
                i.x -= spawn_x
                i.y -= spawn_y
            break
'''
clouds = []
for i in range(100):
    cloud = Clouds()
    clouds.append(cloud)
'''
while True: #game loop
    if joysticks == []:
        pygame.joystick.init()
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            joysticks.append(joystick)
            print(f"{joystick.get_name()} connected")
    spawn_x = 0
    spawn_y = 0
    for tile in tiles:
        if tile.image == bg:
            spawn_x = tile.x
            spawn_y = tile.y
    if player2.crouching:
        player2.height = TILE_SIZE
        feet_rect2.height = TILE_SIZE+2
    else:
        player2.height = PLAYER_HEIGHT
        feet_rect2.height = player2.height+2
    out_str = make_pos((spawn_x, spawn_y, player.velocity_x, player.crouching))
    response = n.send(out_str)
    x, y, vx, crouch = read_pos(response)
    player2.x = spawn_x-x+(10*32)-16+2
    player2.y = spawn_y-y+(10*32)-16-(player2.height + TILE_SIZE)
    player2.velocity_x = vx
    player2.crouching = crouch
    if player2.velocity_x > 0:
        player2.direction = "right"
    elif player2.velocity_x < 0: 
        player2.direction = "left"
    feet_rect2.x = player2.x+2
    feet_rect2.y = player2.y
    for tile in tiles:
        if feet_rect2.colliderect(tile) or feet_rect2.colliderect(player):
            player2.jumping = False
            break
        else:
            player2.jumping = True
    #joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicks the X button in window
            pygame.quit()
            exit()
        if event.type == pygame.JOYDEVICEREMOVED:
            print(f"{joystick.get_name()} disconnected")
            for joy in joysticks:
                if joy.get_instance_id() == event.instance_id:
                    joysticks.remove(joy)
                    #break
        if event.type == pygame.JOYAXISMOTION:
            if event.axis < 2:
                x = joysticks[event.joy].get_axis(0)
                y = joysticks[event.joy].get_axis(1)
                joy_left = False
                joy_right = False
                if x < -.5 and y < -.5:
                    joy_left = True
                elif x > .5 and y < -.5:
                    joy_right = True
                elif x < -.5 and y > .5:
                    joy_left = True
                    joy_crouch = True
                elif x > .5 and y > .5:
                    joy_right = True
                    joy_crouch = True
                elif y > .5 and abs(x) < .5:
                    joy_crouch = True
                elif x < -.5 and abs(y) < .5:
                    joy_left = True
                elif x > .5 and abs(y) < .5:
                    joy_right = True
                else:
                    joy_left = False
                    joy_right = False
                    if not button_crouch:
                        joy_crouch = False
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                joy_jump = True
            if event.button == 1 or event.button == 2:
                button_crouch = True
                joy_crouch = True
            if event.button == 3:
                joy_restart = True
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 1 or event.button == 2:
                button_crouch = False
                joy_crouch = False
        #KEYDOWN - key was pressed, KEYUP - key was pressed/release
        if event.type == pygame.KEYDOWN and not player.crouching or joy_jump:
            try:
                if event.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                    if player.jump_count < player.max_jumps and not player.colliderect(feet_rect2) and not player.crouching:
                        for tile in tiles:
                            tile.y -= PLAYER_VELOCITY_Y
                        player.velocity_y = PLAYER_VELOCITY_Y
                        player.jumping = True
                        player.jump_count += 1
                    elif not player.colliderect(feet_rect2):
                        for tile in tiles:
                            if lava_rect.colliderect(tile):
                                touching_tile_buffer = True
                                break
                            else:
                                touching_tile_buffer = False
            except AttributeError:
                if joy_jump:
                    if player.jump_count < player.max_jumps and not player.colliderect(feet_rect2) and not player.crouching:
                        for tile in tiles:
                            tile.y -= PLAYER_VELOCITY_Y
                        player.velocity_y = PLAYER_VELOCITY_Y
                        player.jumping = True
                        player.jump_count += 1
                    elif not player.colliderect(feet_rect2):
                        for tile in tiles:
                            if lava_rect.colliderect(tile):
                                touching_tile_buffer = True
                                break
                            else:
                                touching_tile_buffer = False
                    joy_jump = False
    keys = pygame.key.get_pressed()
    if touching_tile_buffer and not player.jumping and not player.crouching and not player.colliderect(feet_rect2):
        for tile in tiles:
            tile.y -= PLAYER_VELOCITY_Y
        player.velocity_y = PLAYER_VELOCITY_Y
        player.jumping = True
        touching_tile_buffer = False
    if player2.velocity_x > 0:
        player2.direction = "right"
    elif player2.velocity_x < 0:
        player2.direction = "left"
    check_crouch()
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) or force_crouch or joy_crouch:
        touching_tile_buffer = False
        if player.jumping:
            CROUCH_FRICTION = 1
        else:
            CROUCH_FRICTION = 2
        if not player.crouch_jump:
            if not player.crouching:
                if not player.jumping:
                    BACKGROUND_Y -= round((PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT)/50,1)
                    player.y += PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT
            player.width = PLAYER_CROUCH_WIDTH
            player.height = PLAYER_CROUCH_HEIGHT
            player.crouching = True
            player.crouch_jump = True
    else:
        if not force_crouch:
            if player.crouching:
                if not player.jumping:
                    BACKGROUND_Y += round((PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT)/50,1)
                    player.y -= PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT
            CROUCH_FRICTION = 1
            player.width = PLAYER_WIDTH
            player.height = PLAYER_HEIGHT
            player.crouching = False
            if not player.jumping:
                player.crouch_jump = False
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or joy_left:
        player.velocity_x = -PLAYER_VELOCITY_X//CROUCH_FRICTION
        player.direction = "left"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] or joy_right:
        player.velocity_x = PLAYER_VELOCITY_X//CROUCH_FRICTION
        player.direction = "right"
    for tile in tiles:
        if tile.image == floor_tile_image4:
            tile.lava_timer_x += 1
            if tile.lava_timer_x >= 32 and extra_lava == 1:
                tile.image = tile.original_image
                tile.lava_timer_x = 0
            elif tile.lava_timer_x >= 64 and (extra_lava == 2 or extra_lava == 3):
                tile.image = tile.original_image
                tile.lava_timer_x = 0
            tile.lava_timer_y += 1
            if tile.lava_timer_y >= 32 and extra_lava == 1:
                tile.image = tile.original_image
                tile.lava_timer_y = 0
            elif tile.lava_timer_y >= 64 and (extra_lava == 2 or extra_lava == 3):
                tile.image = tile.original_image
                tile.lava_timer_y = 0
    move()
    draw()
    pygame.display.update()
    clock.tick(60) #frames per second (fps)
