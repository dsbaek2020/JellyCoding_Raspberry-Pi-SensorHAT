from sense_hat import SenseHat
from random import randint
from random import choice
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

dog2 = [x,x,x,x,x,x,x,x,
       x,x,x,x,x,x,x,x,
       p,p,x,x,p,x,p,x,
       x,p,b,b,p,y,y,x,
       x,b,b,b,y,w,y,b,
       x,b,b,b,b,y,y,x,
       x,x,b,x,b,x,x,x,
       x,x,x,x,x,x,x,x]

while True:
    bright = 0
    for i in range(200):
        #print(i,  bright)
        kkkk =[]
        for dot in dog:
            abc = ( int(bright*dot[0]), int(bright*dot[1]), int(bright*dot[2]) )
            kkkk.append(abc)
            
        sense.set_pixels(kkkk)
        
        bright = bright + 0.005
        
        
        sleep(0.005)
        #sense.set_pixels(dog2)
        #sleep(0)

    bright = 1
    for i in range(200):
        #print(i,  bright)
        kkkk =[]
        for dot in dog:
            abc = ( int(bright*dot[0]), int(bright*dot[1]), int(bright*dot[2]) )
            kkkk.append(abc)
            
        sense.set_pixels(kkkk)
        
        bright = bright - 0.005
        
        
        sleep(0.005)
    
    
    
'''
sense.set_pixel(0,1, (218, 160,221) )
sense.set_pixel(1,2, (218, 160,221) )
sense.set_pixel(1,3, (218, 160,221) )
sense.set_pixel(1,4, (70, 130,180) )
sense.set_pixel(1,5, (70, 130,180) )
sense.set_pixel(1,6, (70, 130,180) )
sense.set_pixel(1,6, (70, 130,180) )
sense.set_pixel(2,3, (70, 130,180) )
sense.set_pixel(2,4, (70, 130,180) )
sense.set_pixel(2,5, (70, 130,180) )
sense.set_pixel(3,3, (70, 130,180) )
sense.set_pixel(3,4, (70, 130,180) )
sense.set_pixel(3,5, (70, 130,180) )
sense.set_pixel(3,6, (70, 130,180) )
sense.set_pixel(4,2, (218, 160,221) )
sense.set_pixel(4,3, (218, 160,221) )
sense.set_pixel(4,4, (255, 255,0) )
sense.set_pixel(4,5, (70, 130,180) )
sense.set_pixel(5,3, (255, 255,0) )
sense.set_pixel(5,4, (240, 255,255) )
sense.set_pixel(5,5, (255, 255,0) )
sense.set_pixel(5,6, (70, 130,180) )
sense.set_pixel(6,2, (218, 160,221) )
sense.set_pixel(6,3, (255, 255,0) )
sense.set_pixel(6,4, (255, 255,0) )
sense.set_pixel(6,5, (255, 255,0) )
sense.set_pixel(7,4, (70, 130,180) )
'''
