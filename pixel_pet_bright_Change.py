'''
 author: NaKyungHoon, dabaek
 Change pixel pet bright up/down 
'''

from sense_hat import SenseHat
from random import randint, choice
from time import sleep

sense = SenseHat()
sense.clear()

x = (0,0,0)
p = (218, 160,221)
b = (70, 130,180)
y = (255, 255,0)
w = (240, 255,255)

dog = [x,x,x,x,x,x,x,x,
       p,x,x,x,x,x,x,x,
       x,p,x,x,p,x,p,x,
       x,p,b,b,p,y,y,x,
       x,b,b,b,y,w,y,b,
       x,b,b,b,b,y,y,x,
       x,b,x,b,x,b,x,x,
       x,x,x,x,x,x,x,x]


while True:
    #밝기 증가 ------------------------------------
    bright = 0
    for i in range(200):
        #print(i,  bright)
        kkkk =[]
        for dot in dog:
            abc = ( int(bright*dot[0]), int(bright*dot[1]), int(bright*dot[2]) )
            kkkk.append(abc)
            
        sense.set_pixels(kkkk)
        
        bright = bright + 0.005
        
        
        sleep(0.005) #0.005초 기다리기 
        #sense.set_pixels(dog2)
        #sleep(0)

    #밝기 감소 ------------------------------------
    bright = 1
    for i in range(200):
        #print(i,  bright)
        kkkk =[]
        for dot in dog:
            abc = ( int(bright*dot[0]), int(bright*dot[1]), int(bright*dot[2]) )
            kkkk.append(abc)
            
        sense.set_pixels(kkkk)
        
        bright = bright - 0.005
        
        
        sleep(0.005) #0.005초 기다리기 

