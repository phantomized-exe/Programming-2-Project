import pygame
from sys import exit #terminate the program
import os
from pathlib import Path
import json
import random
level = Path("level_code.json")

# game variables
TILE_SIZE = 32
GAME_WIDTH = 640#512
GAME_HEIGHT = 480#512

PLAYER_WIDTH = 28
PLAYER_HEIGHT = 58
PLAYER_X = (GAME_WIDTH/2)
PLAYER_Y = (GAME_HEIGHT/2)
PLAYER_JUMP_WIDTH = 28
PLAYER_JUMP_HEIGHT = 58
PLAYER_CROUCH_WIDTH = 28
PLAYER_CROUCH_HEIGHT = 32
PLAYER_DISTANCE = 5
BACKGROUND_X = -206*0
global BACKGROUND_Y
BACKGROUND_Y = -206*0
BACKGROUND_WIDTH = 1024
BACKGROUND_HEIGHT = 1024

GRAVITY = 1.2
FRICTION = .6
PLAYER_VELOCITY_X = 6
PLAYER_VELOCITY_Y = -20
global CROUCH_FRICTION
CROUCH_FRICTION = 1

# images
def load_image(image_name,scale=None):
    image = pygame.image.load(os.path.join("Test Sprites",image_name))
    if scale is not None:
        image = pygame.transform.scale(image,scale)
    return image
background_image0 = load_image("Test Sprite-back0.png.png",(BACKGROUND_WIDTH,BACKGROUND_HEIGHT))
background_image3 = load_image("Test Sprite-back3.png.png",(BACKGROUND_WIDTH/2,BACKGROUND_HEIGHT/2))
background_image = load_image("Test Sprite-back.png.png",(BACKGROUND_WIDTH,BACKGROUND_HEIGHT))
background_image2 = load_image("Test Sprite-back2.png.png",(BACKGROUND_WIDTH/2,BACKGROUND_HEIGHT/2))
player_image_right = load_image("Test Sprite-right.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_right2 = load_image("Test Sprite-right2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT)) #resizes player
player_image_left = load_image("Test Sprite-left.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_left2 = load_image("Test Sprite-left2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
image_icon = load_image("Test Sprite-icon.png.png")
player_image_jump_right = load_image("Test Sprite-jump-right.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image("Test Sprite-jump-left.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_crouch_right = load_image("Test Sprite-crouch-right.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_left = load_image("Test Sprite-crouch-left.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_right2 = load_image("Test Sprite-crouch-right2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_left2 = load_image("Test Sprite-crouch-left2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
floor_tile_image = load_image("Test Sprite Tile.png.png",(TILE_SIZE,TILE_SIZE))

pygame.init() #always needed to initialize pygame
window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("test game") #title of window
pygame.display.set_icon(image_icon)
clock = pygame.time.Clock() #used for the framerate

class Background(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,PLAYER_X,PLAYER_Y,PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT)
class Player(pygame.Rect):
    player_animation = 0
    def __init__(self):
        pygame.Rect.__init__(self,PLAYER_X,PLAYER_Y,PLAYER_WIDTH,PLAYER_HEIGHT)
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = "right"
        self.jumping = False
        self.crouching = False
        self.standing_y = (GAME_HEIGHT/2)-(PLAYER_HEIGHT/2)
        self.standing_x = (GAME_WIDTH/2)-(PLAYER_WIDTH/2)
        self.crouching_y = (GAME_HEIGHT/2)-(PLAYER_CROUCH_HEIGHT/2)
        self.crouching_x = (GAME_WIDTH/2)-(PLAYER_CROUCH_WIDTH/2)
        self.crouch_jump = False
    def update_image(self):
        if self.crouching:
            if self.direction == "right":
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
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
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
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
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
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
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
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

class Tile(pygame.Rect):
    def __init__(self,x,y,image):
        pygame.Rect.__init__(self,x,y,TILE_SIZE,TILE_SIZE)
        self.image = image

def create_map():
    read_level = level.read_text()
    load_level = json.loads(read_level)
    for i in range(len(load_level)):
        row = load_level[i]
        for j in range(len(row)):
            tile_code = row[j]
            if tile_code == "1":
                x = j*TILE_SIZE
                y = i*TILE_SIZE
                tile = Tile(x, y, floor_tile_image)
                tiles.append(tile)

def check_tile_collision():
    for tile in tiles:
        if player.colliderect(tile):
            return tile
    return None
def check_tile_collision_x():
    tile = check_tile_collision()
    if tile is not None:
        if player.velocity_x < 0:
            player.x = tile.x+tile.width
        elif player.velocity_x > 0:
            player.x = tile.x-player.width
        player.velocity_x = 0

def check_tile_collision_y():
    global BACKGROUND_Y
    global coyote_time
    global touching_tile
    feet_rect.height = player.height
    feet_rect.y = player.crouching_y+1 if player.crouching else player.standing_y+1
    for tile in tiles:
        if feet_rect.colliderect(tile):
            touching_tile = True
            break
        else:
            touching_tile = False
    tile = check_tile_collision()
    if tile is not None:
        coyote_time = 0
        if player.velocity_y < 0:
            player.jumping = True
            player.y = tile.y+tile.height
        elif player.velocity_y > 0:
            player.y = tile.y-player.height
            if player.jumping:
                if player.crouching:
                    BACKGROUND_Y += .1
                else:
                    BACKGROUND_Y += .3
                player.jumping = False
        player.velocity_y = 0
    elif not touching_tile:
        if coyote_time >= 10 and not player.jumping:
            player.jumping = True
            coyote_time = 0
        elif not player.jumping:
            coyote_time += 1
    else:
        coyote_time = 0

def move():
    global BACKGROUND_Y
    global time_walking
    global crouch_adjust
    global touching_tile
    #x movement
    if player.velocity_x > 0:
        player.velocity_x -= FRICTION
        if player.velocity_x < 0:
            player.velocity_x = 0
    elif player.velocity_x < 0:
        player.velocity_x += FRICTION
        if player.velocity_x > 0:
            player.velocity_x = 0
    else:
        player.velocity_x = 0
    player.x += player.velocity_x
    check_tile_collision_x()
    for tile in tiles:
        tile.x -= player.velocity_x
    check_tile_collision_x()
    player.x = player.crouching_x if player.crouching else player.standing_x

    #y movement
    if player.jumping:
        player.velocity_y += GRAVITY
    check_tile_collision_y()
    player.y += player.velocity_y
    BACKGROUND_Y -= round(player.velocity_y/25,1)
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
    player.y = player.crouching_y if player.crouching else player.standing_y

def draw():
    global BACKGROUND_Y
    global debug
    #window.fill("blue")
    #window.fill("#54de9e")
    #window.fill((84,222,158))
    background_y = BACKGROUND_Y
    window.fill((20,18,167))
    background_y = round(BACKGROUND_Y/4,1)
    round(background_y,1)
    window.blit(background_image3, (BACKGROUND_X//4,background_y))
    background_y = BACKGROUND_Y
    background_y = round(background_y/2,1)-103
    round(background_y,1)
    window.blit(background_image, (BACKGROUND_X//2-206,background_y))
    background_y = BACKGROUND_Y
    background_y = background_y-103
    round(background_y,1)
    window.blit(background_image0, (BACKGROUND_X-206,background_y))
    background_y = BACKGROUND_Y
    background_y = background_y*2
    round(background_y,1)
    window.blit(background_image2, (BACKGROUND_X*2,background_y))
    for tile in tiles:
        window.blit(tile.image, tile)
    player.update_image()
    window.blit(player.image,player)
    if keys[pygame.K_o]:
        debug = True
    elif keys[pygame.K_p]:
        debug = False
    if debug:
        pygame.draw.rect(window, (255, 0, 0), feet_rect, 2)
def check_crouch():
    global CROUCH_FRICTION
    global force_crouch
    collide_crouch = pygame.Rect(player.x, player.y-(PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT), PLAYER_WIDTH, PLAYER_HEIGHT)
    tile_count = 0
    if player.crouching:
        for tile in tiles:
            if collide_crouch.colliderect(tile):
                tile_count += 1
                CROUCH_FRICTION = 2
                player.width = PLAYER_CROUCH_WIDTH
                player.height = PLAYER_CROUCH_HEIGHT
                player.crouching = True
                force_crouch = True
        if tile_count == 0:
            force_crouch = False
#start game
level_list = []
rand_int = 0
for i in range(48):
    level_str = ""
    for j in range(48):
        # for straight line map generation
        if i == 47 or i == 38 or i == 37 or i == 36 or i == 35:
            rand_int = 0
        else:
            rand_int = 1
        #rand_int = random.randint(0,47-i) #generate random map
        if rand_int == 0:
            level_str += "1"
        else:
            level_str += "0"
    level_list.append(level_str)
level_dump = json.dumps(level_list)
level.write_text(level_dump)
global  coyote_time
coyote_time = 0
player = Player()
background = Background()
tiles = []
global time_walking
time_walking = 0
global force_crouch
force_crouch = False
feet_rect = Player()
feet_rect.x = player.standing_x
feet_rect.y = player.standing_y
feet_rect.height = PLAYER_HEIGHT+1
global debug
debug = False
create_map()
'''
if player.crouching:
    player.x = player.crouching_x
    player.y = player.crouching_y
else:
    player.x = player.standing_x
    player.y = player.standing_y
'''

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicks the X button in window
            pygame.quit()
            exit()

        #KEYDOWN - key was pressed, KEYUP - key was pressed/release
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not player.jumping and not player.crouching:
        player.velocity_y = PLAYER_VELOCITY_Y
        player.jumping = True
        crouch_adjust = False
    check_crouch()
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) or force_crouch:
        if not player.crouch_jump:
            CROUCH_FRICTION = 2
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
                    BACKGROUND_Y = round(BACKGROUND_Y,1)
                    player.y -= PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT
            CROUCH_FRICTION = 1
            player.width = PLAYER_WIDTH
            player.height = PLAYER_HEIGHT
            player.crouching = False
            if not player.jumping:
                player.crouch_jump = False
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        time_walking += .1
        '''
        if FRICTION > 0:
            FRICTION -= .1
        else:
            FRICTION = 0
        '''
        if player.velocity_x < 0:
            BACKGROUND_X += .08
        player.velocity_x = -PLAYER_VELOCITY_X//CROUCH_FRICTION
        if player.crouching:
            player.x = player.crouching_x
        else:
            player.x = player.standing_x
        player.direction = "left"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        time_walking += .1
        '''
        if FRICTION > 0:
            FRICTION -= .1
        else:
            FRICTION = 0
        '''
        if player.velocity_x > 0:
            BACKGROUND_X -= .08
        player.velocity_x = PLAYER_VELOCITY_X//CROUCH_FRICTION
        '''
        if player.crouching:
            player.x = player.crouching_x
        else:
            player.x = player.standing_x
        '''
        player.direction = "right"
    if not (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        time_walking = 0
    '''
        if FRICTION < 1.5:
            FRICTION += .1
    FRICTION = round(FRICTION,3)
    '''
    move()
    draw()
    pygame.display.update()
    clock.tick(60) #frames per second (fps)
