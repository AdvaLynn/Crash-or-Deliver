import pygame
from pygame.locals import *

pygame.init()

def draw(x,y):
    screen = pygame.display.set_mode((x,y))
    img = pygame.image.load('Five-lane Road.jpg').convert()
    img_rect = img.get_rect()
    


    
