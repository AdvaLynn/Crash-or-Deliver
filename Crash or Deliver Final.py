#Adva Masliah, Rainny Qiu
#Pyton3.3
#Mr. Nouvkovitch
#March 31 2015

import pygame
from pygame.locals import *
pygame.mixer.pre_init(22050, -16, 2, 1024) 
pygame.init()

import random
import time
import Screen

x = 917
y = 630

screen = pygame.display.set_mode((x, y))#Size of screen is set which is approximately the size of the road
img = pygame.image.load('Five-lane Road.jpg').convert()
img_rect = img.get_rect()

Screen.draw(x,y)


car = pygame.image.load('car.bmp')

pylon = pygame.image.load('pylon.bmp')


def obstacle():#All the coordinates the pylons can start
    n_lane = random.randint(1, 5)
    if n_lane == 1:
        py1_rect = pylon.get_rect()
        py1_rect.topleft = (0,0)
        return py1_rect
    if n_lane == 2:
        py2_rect = pylon.get_rect()
        py2_rect.topleft = (0, y*0.2)
        return py2_rect 
    if n_lane == 3:
        py3_rect = pylon.get_rect()
        py3_rect.topleft = (0, y*0.4)
        return py3_rect
    if n_lane == 4:
        py4_rect = pylon.get_rect()
        py4_rect.topleft = (0, y*0.6)
        return py4_rect
    if n_lane == 5:
        py5_rect = pylon.get_rect()
        py5_rect.topleft = (0, y*0.8)
        return py5_rect

        
def lane(number):# all the coordinates the car can be
    car_rect = car.get_rect()
    if number == 1:
        box1_rect = car.get_rect()
        box1_rect.topright = (x,y*0)
        return box1_rect
    if number == 2:
        box2_rect = car.get_rect()
        box2_rect.topright = (x,y*0.2)
        return box2_rect
    if number == 3:
        box3_rect = car.get_rect()
        box3_rect.topright = (x,y*0.4)
        return box3_rect
    if number == 4:
        box4_rect = car.get_rect()
        box4_rect.topright = (x,y*0.6)
        return box4_rect
    if number == 5:
        box5_rect = car.get_rect()
        box5_rect.topright = (x,y*0.8)
        return box5_rect

def crash(pylonplacelist, car_rect, lives,mi, ma):# During a crash the game stops and shows a crash symbol and the lives decrease by one
    for number in range(len(pylonplacelist)):
        pylonplace, s = pylonplacelist[number]
        if pylonplace.colliderect(car_rect):
            lives = lives - 1
            pylonplacelist[number] = obstacle(), random.randint(mi, ma)
            bang = pygame.image.load('bang.jpg').convert()
            bang_rect = bang.get_rect()
            bang_rect.center = (917/2,630/2)
            screen.blit(bang, bang_rect)
            pygame.display.flip()
            time.sleep(1)
            
            break      
           
    return lives, pylonplacelist

def show(number, lives,pylonplacelist, mi, ma):#randomly shows pylons
    pn = -1
    screen.blit(img, img_rect)
    for pylonplace, speed in pylonplacelist:
        blit(pylonplace, speed, pn)
        pn = pn +1
        if pylonplace.left >= (x):
            pylonplacelist[pn] = obstacle(), random.randint(mi, ma)

    return number, lives, mi, ma

def blit(pylonp, speed, pn):#moves pylon across screen
    pylonp.left += speed
    screen.blit(pylon, pylonp)

    
def arrowkeys(number):# Moves car up and down lanes
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        if ev.type == KEYDOWN:
            if ev.key == K_UP  and number > 1: #<-- keyboard events have a key property
                number = number - 1      
            elif ev.key == K_DOWN and number < 5:
                number = number +1
    return number
def score1(before, score):# Displays score and lives on screen
    font=pygame.font.Font(None,50)
    scoretext=font.render(before+str(score), 1,(0,0,0))
    return scoretext
    

    
number = 3
clock = pygame.time.Clock()
keep_going = True
lives = 3
pylonplacelist = []
mi = 1
ma = 3

while keep_going:
    clock.tick(30)
    screen = pygame.display.set_mode((960, 540))
    begin = pygame.image.load('Crash or Deliver Intro Page.jpg').convert()
    begin_rect = begin.get_rect()
    screen.blit(begin, begin_rect)# Instructions are shown for 8 seconds    
    pygame.display.set_caption('Crash or Deliver')
    pygame.display.flip()
    time.sleep(8)
    screen = pygame.display.set_mode((x, y))
    Screen.draw(x,y)
    screen.blit(img, img_rect)
    for i in range(4):# 4 pylons can be on the screen at the same time that way at least one lane is open at all times
        pylonplace = obstacle(), random.randint(mi, ma)
        pylonplacelist.append(pylonplace)  
    
    while lives > 0:
        number, lives, mi, ma= show(number, lives, pylonplacelist, mi, ma)
        number = arrowkeys(number)
        car_rect = lane(number)
        screen.blit(car, car_rect)#Car is shown
        seconds = pygame.time.get_ticks()# Time is recieved
        score = seconds // 1000# score is based on time
        scoretext = score1("Score:",score)
        livestext = score1("Lives:",lives)
        screen.blit(scoretext, (20, 20))# Score is shown
        screen.blit(livestext, (760, 20))# lives are shown
        lives, pylonplacelist = crash(pylonplacelist, car_rect, lives, mi ,ma)
        if seconds%10000== 0:# Speed of pylons increases every 10 seconds
            mi += 1
            ma += 1
        pygame.display.flip()
    while lives == 0:# End of Game --> Score is shown
        screen.blit(img, img_rect)            
        scoretext = score1("Score:",score)
        crashsay = pygame.font.Font(None,100).render("You Crashed!" , 1,(0,0,0))
        screen.blit(crashsay, (280, (y/2-100)))
        screen.blit(scoretext, (400, y/2))
        pygame.display.flip()
        
        
        
