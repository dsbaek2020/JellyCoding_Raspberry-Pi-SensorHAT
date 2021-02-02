#author KimDS
#2021.2.1
#Thread Test
#Joystick Event Test

from sense_hat import SenseHat
from time import sleep
from random import *
import threading

#https://trinket.io/embed/python/b328848f53

r = (100, 0,0)
o = (255, 128,0)
y = (255, 255,0)
g = (0, 100,0)
b = (0, 0,100)
n = (0, 0,102)
v = (204, 0,204)
e = (0,0,0)

wall = n
steaveColor = v
enemyColor=g
badItemColor=y

map1 =[
    e,e,e,e,e,e,e,e,
    e,n,n,n,n,n,n,e,
    e,e,e,e,e,n,e,e,
    e,e,y,e,n,e,e,e,
    e,e,e,n,e,e,e,e,
    e,e,n,e,e,e,e,e,
    e,n,n,n,n,n,n,e,
    e,e,e,e,e,e,e,e
    ]

steaveX =0
steaveY =0

enemyX = 7
enemyY = 7




sense = SenseHat()

def collision(x, y):
    return  map1[x + (y*8)] == wall

def badItem(x, y):
    return  map1[x + (y*8)] == badItemColor

def draw_map():
    sense.set_pixels(map1)
    

def draw_steave():
    sense.set_pixel(steaveX,steaveY, steaveColor)

def draw_enemy():
    sense.set_pixel(enemyX,enemyY, enemyColor)


def move_up(event):
    global steaveY
    #collision detection and avoidance
    # 0<= Y <=7
    if event.action == 'pressed':
        if steaveY>0 and collision(steaveX, steaveY-1) == False:
            steaveY-=1
 
def move_down(event):
    global steaveY
    #collision detection and avoidance
    # 0<= Y <=7and
    if event.action == 'pressed':
        if steaveY<7 and collision(steaveX, steaveY+1) == False:
            steaveY+=1
        
def move_left(event):
    global steaveX
    #collision detection and avoidance
    # 0<= Y <=7
    if event.action == 'pressed':
        if steaveX>0 and collision(steaveX-1, steaveY) == False:
            steaveX-=1
        
def move_right(event):
    global steaveX
    #collision detection and avoidance
    # 0<= Y <=7
    if event.action == 'pressed':
        if steaveX<7 and collision(steaveX+1, steaveY) == False:
            steaveX+=1

timer =0
def itemMain():
    global steaveX, steaveY, timer
    if badItem(steaveX, steaveY):
        timer+=1
        if(timer == 10):
          steaveX, steaveY =0 ,0
          timer =0
        

        
    
    
    
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_left = move_left
sense.stick.direction_right = move_right

#flagLedScreen = 0  # 0: not used, 1 = used
redotStatus =0
def game_main():
    while True:
        sense.clear()
        draw_map()
        draw_steave()
        itemMain()
        draw_enemy()
        
        if redotStatus == 1 :
            sense.set_pixel(0,7,(100,0,0))
        
        sleep(0.1)
    
#def displayStatus():
    
def redDot():
    global redotStatus
    while True:
        timer =0
        while  timer < 10:
            #sense.set_pixel(0,7,(100,0,0))
            redotStatus = 1
            sleep(0.1)
            timer+=1
            
        timer =0   
        while  timer < 10:
            #sense.set_pixel(0,7,(0,0,0))
            redotStatus = 0
            sleep(0.1)
            timer+=1

gameThread = threading.Thread(target = game_main)
#DisplayThread = threading.Thread(target = displayStatus)
gameThread.start()
#DisplayThread.start()
redThread = threading.Thread(target = redDot)
redThread.start()



