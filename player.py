import pygame
import os

PLAYER_WIDTH = 28
PLAYER_HEIGHT = 64
PLAYER_X = 306
PLAYER_Y = 208
GAME_WIDTH = 640#512
GAME_HEIGHT = 480#512
PLAYER_CROUCH_WIDTH = 28
PLAYER_CROUCH_HEIGHT = 32
PLAYER_JUMP_WIDTH = 28
PLAYER_JUMP_HEIGHT = 64
keys = pygame.key.get_pressed()
PLAYER_VELOCITY_X = 6

def load_image(image_name,scale=None):
    image = pygame.image.load(os.path.join("Test Sprites",image_name))
    if scale is not None:
        image = pygame.transform.scale(image,scale)
    return image
player_image_right = load_image("Test Sprite-right.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_right2 = load_image("Test Sprite-right2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT)) #resizes player
player_image_left = load_image("Test Sprite-left.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_left2 = load_image("Test Sprite-left2.png.png",(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_jump_right = load_image("Test Sprite-jump-right.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image("Test Sprite-jump-left.png.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_crouch_right = load_image("Test Sprite-crouch-right.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_left = load_image("Test Sprite-crouch-left.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_right2 = load_image("Test Sprite-crouch-right2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))
player_image_crouch_left2 = load_image("Test Sprite-crouch-left2.png.png",(PLAYER_CROUCH_WIDTH,PLAYER_CROUCH_HEIGHT))

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
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
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