import pygame
from sys import exit #terminate the program
import os
from pathlib import Path
import json
import random
from network import Network
level = Path("level_code.json")

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
BACKGROUND_X = -206*0
global BACKGROUND_Y
BACKGROUND_Y = -206*0
BACKGROUND_WIDTH = 1024
BACKGROUND_HEIGHT = 1024

GRAVITY = 1.1
FRICTION = .8
PLAYER_VELOCITY_X = 6
PLAYER_VELOCITY_Y = -13.2
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
player2_image_right = load_image("Test Sprite2-right.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player2_image_right2 = load_image("Test Sprite2-right2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT)) #resizes player
player2_image_left = load_image("Test Sprite2-left.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player2_image_left2 = load_image("Test Sprite2-left2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
image_icon = load_image("Test Sprite-icon.png.png")
image_icon2 = load_image("Test Sprite-icon2.png.png")
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
floor_tile_imageg = load_image("Test Sprite Tile-legacy4.png.png",(TILE_SIZE,TILE_SIZE))

pygame.init() #always needed to initialize pygame
window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("test game") #title of window
pygame.display.set_icon(image_icon2)
clock = pygame.time.Clock() #used for the framerate

class Background(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,PLAYER_X,PLAYER_Y,PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT)
class Player(pygame.Rect):
    player_animation = 0
    def __init__(self):
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
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
    '''
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
    '''
    def update_image(self):
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
    def __init__(self,x,y,image=None):
        pygame.Rect.__init__(self,x,y,TILE_SIZE,TILE_SIZE)
        self.image = image

def create_map():
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
                tile = Tile(x,y,spawn_tile2)
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

def check_tile_collision():
    for tile in tiles:
        if player.colliderect(tile):
            return tile
    return None
def check_lava_collision():
    global coyote_lava
    for tile in tiles:
        if lava_rect.colliderect(tile) or lava_rect2.colliderect(tile) or keys[pygame.K_r]:
            if keys[pygame.K_r] or tile.image == floor_tile_image4 or tile.image == floor_tile_image4 or tile.image == floor_tile_image5 or tile.image == floor_tile_image6 or tile.image == floor_tile_image7 or tile.image == floor_tile_imagea or tile.image == floor_tile_imageb or tile.image == floor_tile_imagec or tile.image == floor_tile_imaged or tile.image == floor_tile_imagee or tile.image == floor_tile_imagef:
                if coyote_lava >= 8:
                    coyote_lava = 0
                    for tile in tiles:
                        if tile.image == spawn_tile2:
                            spawn_x = tile.x-(10*32)+16
                            spawn_y = tile.y-(10*32)+TILE_SIZE+16#-player.height
                            for tile in tiles:
                                tile.x -= spawn_x
                                tile.y -= spawn_y
                            break
                else:
                    coyote_lava += 1
def check_tile_collision_x():
    tile = check_tile_collision()
    if tile is not None:
        if player.velocity_x < 0:# or player.direction == "right":
            player.x = tile.x+tile.width
        elif player.velocity_x > 0:# or player.direction == "left":
            player.x = tile.x-player.width
        player.velocity_x = 0

def check_tile_collision_y():
    global BACKGROUND_Y
    global coyote_time
    feet_rect.height = player.height+2
    if player2.crouching:
        feet_rect2.height = TILE_SIZE+2
    else:
        feet_rect2.height = player.height+2
    lava_rect.height = player.height+8
    #feet_rect.y = player.crouching_y if player.crouching else player.standing_y
    for tile in tiles:
        if feet_rect.colliderect(tile):
            if tile.image == spawn_tile:
                for i in tiles:
                    if i.image == spawn_tile2:
                        i.image = spawn_tile
                tile.image = spawn_tile2
            else:
                touching_tile_feet = True
                break
        else:
            touching_tile_feet = False
    tile = check_tile_collision()
    if tile is not None:
        coyote_time = 0
        if player.velocity_y < 0:
            player.jumping = True
            player.y = tile.y+tile.height
        elif player.velocity_y > 0:
            player.y = tile.y-player.height#going down by .8
            if player.jumping:
                if player.crouching:
                    BACKGROUND_Y += 1.3
                else:
                    BACKGROUND_Y += .6
                player.jumping = False
                BACKGROUND_Y = round(BACKGROUND_Y,1)
        player.velocity_y = 0
    elif not touching_tile_feet:
        if coyote_time >= 8 and not player.jumping:
            player.jumping = True
            coyote_time = 0
        elif not player.jumping:
            coyote_time += 1
    else:
        coyote_time = 0
    #print(coyote_time)

def move():
    global BACKGROUND_Y
    if abs(player.velocity_x) <= FRICTION:
        player.velocity_x = 0
    elif player.velocity_x > 0:
        player.velocity_x -= FRICTION
    elif player.velocity_x < 0:
        player.velocity_x += FRICTION
    player.x += player.velocity_x
    check_tile_collision_x()
    for tile in tiles:
        tile.x -= player.velocity_x
    check_tile_collision_x()
    player.x = player.crouching_x if player.crouching else player.standing_x
    check_lava_collision()
    #y movement
    if player.jumping:
        player.velocity_y += GRAVITY
    player.velocity_y = round(player.velocity_y,1)
    check_tile_collision_y()
    player.y += player.velocity_y
    for tile in tiles:
        if tile.image == bg:
            BACKGROUND_Y = tile.y/25
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
    '''
    velocity_backup_y = 0
    if player.velocity_y == 0:
        velocity_backup_y = 1
    if not player.crouching:
        if player.y > player.standing_y:
            player.y -= player.y/player.standing_y*(player.velocity_y+velocity_backup_y)
            center.y -= player.y/player.standing_y*(player.velocity_y+velocity_backup_y)
            for tile in tiles:
                tile.y -= player.y/player.standing_y*(player.velocity_y+velocity_backup_y)
        elif player.y < player.standing_y:
            if player.y > 106:
                player.y += player.y/player.standing_y*-(player.velocity_y-velocity_backup_y)
                center.y += player.y/player.standing_y*-(player.velocity_y+velocity_backup_y)
                for tile in tiles:
                    tile.y += player.y/player.standing_y*-(player.velocity_y-velocity_backup_y)
            else:
                player.y += 106/player.standing_y*-(player.velocity_y-velocity_backup_y)
                center.y += 106/player.standing_y*-(player.velocity_y+velocity_backup_y)
                for tile in tiles:
                    tile.y += 106/player.standing_y*-(player.velocity_y-velocity_backup_y)
        if player.y == player.standing_y+1:
            player.y -= 1
            center.y -= 1
            for tile in tiles:
                tile.y -= 1
        if player.y == player.standing_y-1:
            player.y += 1
            center.y += 1
            for tile in tiles:
                tile.y += 1
    else:
        if player.y > player.crouching_y:
            player.y -= player.y/player.crouching_y*(player.velocity_y+velocity_backup_y)
            center.y -= player.y/player.crouching_y*(player.velocity_y+velocity_backup_y)
            for tile in tiles:
                tile.y -= player.y/player.crouching_y*(player.velocity_y+velocity_backup_y)
        elif player.y < player.crouching_y:
            if player.y > 106:
                player.y += player.y/player.crouching_y*-(player.velocity_y-velocity_backup_y)
                center.y += player.y/player.crouching_y*-(player.velocity_y-velocity_backup_y)
                for tile in tiles:
                    tile.y += player.y/player.crouching_y*-(player.velocity_y-velocity_backup_y)
            else:
                player.y += 106/player.crouching_y*-(player.velocity_y-velocity_backup_y)
                center.y += 106/player.crouching_y*-(player.velocity_y-velocity_backup_y)
                for tile in tiles:
                    tile.y += 106/player.crouching_y*-(player.velocity_y-velocity_backup_y)
        if player.y == player.crouching_y+1:
            player.y -= 1
            center.y -= 1
            for tile in tiles:
                tile.y -= 1
        if player.y == player.crouching_y-1:
            player.y += 1
            center.y += 1
            for tile in tiles:
                tile.y += 1
    '''
    if player.crouching:
        feet_rect.x = player.crouching_x+2
        feet_rect.y = player.crouching_y
        lava_rect.x = player.crouching_x+14
        lava_rect.y = player.crouching_y
        lava_rect2.x = player.crouching_x-5
        lava_rect2.y = player.crouching_y+(player.height/2)
    else:
        feet_rect.x = player.standing_x+2
        feet_rect.y = player.standing_y
        lava_rect.x = player.standing_x+14
        lava_rect.y = player.standing_y
        lava_rect2.x = player.standing_x-5
        lava_rect2.y = player.standing_y+(player.height/2)
    check_lava_collision()
    player.y = player.crouching_y if player.crouching else player.standing_y

def read_pos(str):
    s = str.strip()
    parts = s.split(",")
    if len(parts) != 4:
        print(f"error: {repr(s)}")
        return None
    x_str, y_str, v_str, crouch_str = parts
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
    return f"{tup[0]},{tup[1]},{tup[2]},{tup[3]}"

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
    player2.update_image()
    window.blit(player2.image,player2)
    if keys[pygame.K_o]:
        debug = True
    elif keys[pygame.K_p]:
        debug = False
    if debug:
        pygame.draw.rect(window, (255, 255, 255), player, 2)
        pygame.draw.rect(window, (255, 255, 255), player2, 2)
        pygame.draw.rect(window, (255, 0, 0), feet_rect, 2)
        pygame.draw.rect(window, (255, 0, 0), feet_rect2, 2)
        pygame.draw.rect(window, (0, 255, 0), lava_rect, 2)
        pygame.draw.rect(window, (0, 255, 0), lava_rect2, 2)
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
        rand_int = random.randint(0,47-i) #generate random map
        if i == 24 and j == 24:
            level_str += "2"
            continue
        if rand_int == 0:
            level_str += "1"
        else:
            level_str += "0"
    level_list.append(level_str)
test_map = ["00000000000000000000000000000000000000000000000000000000000000001", 
            "00000000000000000000000000000000000000000000001000000000000000001", 
            "0000000000000000000000!0001000000000000000000010000010000100001!4", 
            "00000000000001000010000000000000001000000000001100000000000000004", 
            "@0000000000010000000000100001100000000000001001000000000000001004", 
            "00000000000000000000000000000000000000001001000000000000000000004", 
            "0000000000#0000000000000000000000!0001001001000000000000000010004", 
            "44444111111111111111111111111111110111111111111100000000000000014", 
            "7cefd822222222222222222222222222220222222222222200000000000100004", 
            "33333333333333333333333333333333330333333333333310000000000000004", 
            "33333333333333333333333333333333330333333333333300000000001000004", 
            "33333333333333333333333333333333300333333333333300000000000000004", 
            "33333333333333333333333333333333303333333333333310000000010000004", 
            "33333333333333333333333333333333303333333333333300000000000000004",
            "00000000000000000000000000000000000000000000000000000000100000004",
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
            "000000000000000000000000000000000000000000000000000000000000004",
            "44444444444444444444444444444444444444444444444444444444444444"]
level_dump = json.dumps(test_map)
level.write_text(level_dump)
global  coyote_time
coyote_time = 0
tiles = []
create_map()
n = Network()
startPos = read_pos(n.getPos())
player = Player()
player.player = 1
player2 = Player()
player2.player = 2
player2.direction = "right"
'''
for tile in tiles:
    if tile.image == spawn_tile:
        x_shift = tile.x
        player.y = tile.y-PLAYER_HEIGHT
        for i in tiles:
            i.x -= x_shift-(10*32)+16
'''
player.x = startPos[0]
player.y = startPos[1]
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
lava_rect.x = player.standing_x+(player.width/2)
lava_rect.y = player.standing_y
lava_rect.height = PLAYER_HEIGHT+8
lava_rect.width = 2
lava_rect2 = Player()
lava_rect2.x = player.standing_x-2
lava_rect2.y = player.standing_y+(player.height/2)
lava_rect2.height = 2
lava_rect2.width = PLAYER_WIDTH+10
feet_rect2 = Player()
feet_rect2.x = player2.standing_x+2
feet_rect2.y = player2.standing_y
feet_rect2.height = player2.height+2
feet_rect2.width = player2.width-4
touching_tile_buffer = False
player2_crouching = False
global debug
debug = False
global coyote_lava
coyote_lava = 0
'''
if player.crouching:
    player.x = player.crouching_x
    player.y = player.crouching_y
else:
    player.x = player.standing_x
    player.y = player.standing_y
'''

while True: #game loop
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
        feet_rect2.height = player.height+2
    '''
    player2Pos = read_pos(n.send(make_pos((spawn_x,spawn_y,player.velocity_x,player.crouching))))
    player2.x = spawn_x-player2Pos[0][0]+(10*32)-16
    player2.y = spawn_y-player2Pos[0][1]+(10*32)-16-(player2.height+TILE_SIZE)
    player2.velocity_x = player2Pos[1]
    player.crouching = player2Pos[2]
    player2.update()
    '''
    out_str = make_pos((spawn_x, spawn_y, player.velocity_x, player.crouching))
    response = n.send(out_str)
    x, y, vx, crouch = read_pos(response)
    player2.x = spawn_x-x+(10*32)-16
    player2.y = spawn_y-y+(10*32)-16-(player2.height + TILE_SIZE)
    player2.velocity_x = vx
    player2.crouching = crouch
    if player2.velocity_x > 0:
        player2.direction = "right"
    elif player2.velocity_x < 0: 
        player2.direction = "left"
    feet_rect2.x = spawn_x-x+(10*32)-16+2
    feet_rect2.y = spawn_y-y+(10*32)-16-(player2.height + TILE_SIZE)
    for tile in tiles:
        if feet_rect2.colliderect(tile):
            player2.jumping = False
            break
        else:
            player2.jumping = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicks the X button in window
            pygame.quit()
            exit()

        #KEYDOWN - key was pressed, KEYUP - key was pressed/release
    keys = pygame.key.get_pressed()
    '''
    if keys[pygame.K_r]:
        for tile in tiles:
            if tile.image == spawn_tile2:
                x_shift = tile.x
                player.y = tile.y-(10*32)+TILE_SIZE+16
                for i in tiles:
                    i.x -= x_shift-(10*32)+16
    '''
    if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and not player.crouching:
        for tile in tiles:
            if feet_rect.colliderect(tile):
                touching_tile_feet = True
                break
            else:
                touching_tile_feet = False
        for tile in tiles:
            if lava_rect.colliderect(tile):
                touching_tile_buffer = True
                break
            else:
                touching_tile_buffer = False
        if not player.jumping and not player.crouching:
            for tile in tiles:
                tile.y -= PLAYER_VELOCITY_Y
            player.velocity_y = PLAYER_VELOCITY_Y
            player.jumping = True
            touching_tile_buffer = False
    if touching_tile_buffer and not player.jumping and not player.crouching:
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
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) or force_crouch:
        touching_tile_buffer = False
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
                    player.y -= PLAYER_HEIGHT-PLAYER_CROUCH_HEIGHT
            CROUCH_FRICTION = 1
            player.width = PLAYER_WIDTH
            player.height = PLAYER_HEIGHT
            player.crouching = False
            if not player.jumping:
                player.crouch_jump = False
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        '''
        if FRICTION > 0:
            FRICTION -= .1
        else:
            FRICTION = 0
        '''
        if player.velocity_x < 0:
            BACKGROUND_X += .08
        player.velocity_x = -PLAYER_VELOCITY_X//CROUCH_FRICTION
        '''
        if player.crouching:
            player.x = player.crouching_x
        else:
            player.x = player.standing_x
        '''
        player.direction = "left"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
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
    move()
    draw()
    pygame.display.update()
    clock.tick(60) #frames per second (fps)
