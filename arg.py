import os
import sys
import math
import random
import pygame
from pygame.locals import *
pygame.init()

fps = 60
clock = pygame.time.Clock()
width,height = 480, 360
screen = pygame.display.set_mode((width,height))

def title_screen_animation():
    pass
def main_menu():
    pass
def test_level():
    temp = pygame.Rect(0,170,480,20)
    pygame.draw.rect(screen,"#ffffff",temp)
    temp = pygame.Rect(230,0,20,360)
    pygame.draw.rect(screen,"#ffffff",temp)

while True:
    screen.fill("#000000")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    title_screen_animation()
    main_menu()
    test_level()
    pygame.display.update()
    clock.tick(fps)