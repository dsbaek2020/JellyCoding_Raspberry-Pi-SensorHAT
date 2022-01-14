#author : kim minseo, support: baek daeseong
#date: 22. 1. 14

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear()

yello =(100, 100, 0)


def blinkStar():
    
    x = randint(0,7)
    y = randint(0,7)
    #--decreation -------
    bright = 1
    for i in range(10):     
        r = yello[0] * bright
        g = yello[1] * bright
        b = yello[2] * bright       
        print(r,g,b)      
        sense.set_pixel(x, y, (int(r),int(g),int(b)))      
        bright = bright - 0.1      
        sleep(0.2)
 
    #
    bright = 0
    for i in range(10):     
        r = yello[0] * bright
        g = yello[1] * bright
        b = yello[2] * bright       
        print(r,g,b)      
        sense.set_pixel(x, y, (int(r),int(g),int(b)))      
        bright = bright + 0.1      
        sleep(0.2)
        

while True:
    print('new star')
    sleep(1)
    blinkStar()
    sleep(1)
