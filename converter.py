import os
import sys
import math
import random
import pygame
from pygame.locals import *
pygame.init()

FPS = 60
FPS_CLOCK = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 360
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class sprite():
    w = 100
    h = 100
    x = 240+w/2
    y = 180+h/2
    image = pygame.transform.scale(pygame.image.load(os.path.join('image.png')).convert_alpha(),(w,h))
    angle = 0
    step = 100
    def move(a):
        sprite.x += a * math.cos(sprite.angle * math.pi / 180)
        sprite.y += a * math.sin(sprite.angle * math.pi / 180)
    def turn(a):
        sprite.angle += a
    def goto(x,y):
       sprite.x = x
       sprite.y = y
    def glide(x,y,vel):
        if sprite.step != vel:
            sprite.x += (round(x) - round(sprite.x)) / vel * sprite.step
            sprite.y += (round(y) - round(sprite.y)) / vel * sprite.step
            sprite.step += 1
        else:
            sprite.step = 0
            main.rand()
    def point(a):
        sprite.angle = a
    def point_towards_mouse_pointer():
        mouse_pos = pygame.mouse.get_pos()
        sprite.angle = 360 - math.atan2((mouse_pos[1] - (sprite.y + sprite.h / 2)), (mouse_pos[0] - (sprite.x + sprite.w / 2))) * (180 / math.pi)

class main():
    def show(surf,image,topleft,angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
        surf.blit(rotated_image, new_rect.topleft)
    def rand():
        global randX, randY
        randX = random.randint(50,430)
        randY = random.randint(50,310)

main.rand()
while True:
    SCREEN.fill("#FFFFFF")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main.show(SCREEN,sprite.image,(sprite.x,sprite.y),sprite.angle)
    sprite.glide(randX,randY,100)
    sprite.point_towards_mouse_pointer()
    pygame.display.flip()
    FPS_CLOCK.tick(FPS)