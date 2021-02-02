#Date: 21.02.2
#author: rain Class ChoiSY
#        bar Class JungYS

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
class bar(object):
    def __init__(self,x,y,r,g,b):
        self.x = x
        self.y = 7
        self.ax = 0.0
        self.vx = 0.0
        self.rgb = (r,g,b)
        
    def draw(self):
        for i in range(3):
            x =  self.x - i
            if 0<= x <=8:
                sense.set_pixel(int(x),self.y, self.rgb)
                
    def move_left(self,event):
        if event.action =='pressed':
            self.ax = -0.005
            sleep(0.5)
            self.ax =0
            #print('left, self.ax = ', self.ax)
            #print('left, self.vx = ', self.vx)
            #print('left, self.x = ', self.x)
        
    def move_right(self,event):
        if event.action == 'pressed':
            self.ax = 0.005
            sleep(0.5)
            self.ax = 0
            #print('right, self.ax = ', self.ax)
            #print('right, self.vx = ', self.vx)
            #print('right, self.x = ', self.x)
            
    def move_middle(self,event):
        if event.action == 'pressed':
            self.ax = 0
            self.vx = 0
            #print('middle, self.ax = ', self.ax)
            #print('middle, self.vx = ', self.vx)
            #print('middle, self.x = ', self.x)

    def move(self):
        self.vx += self.ax
        self.x += self.vx

bucket = bar(3,7,100,0,0)
sense.stick.direction_left = bucket.move_left
sense.stick.direction_right = bucket.move_right
sense.stick.direction_middle = bucket.move_middle
    
class rain (object):
    def __init__(self, x, y, vy, r,g,b):
        self.x = x
        self.y = y
        self.vy = vy
        self.rgb = (r,g,b)                         
    def draw(self):
        '''
        if 0<= self.y <=7:
            sense.set_pixel(self.x, self.y, self.rgb)
        if 0<= self.y <=7:
            sense.set_pixel(self.x, self.y-1, self.rgb)
        '''  
        for i in range(4):
            y= self.y - i
            if 0<= y <=8:
                sense.set_pixel(self.x, int(y), self.rgb)
             
    def drop(self):
        self.y +=self.vy
        if int(self.y) == 8:
            self.restart()    
    def restart(self):
        self.x = randint(0,7)
        self.y = 0

rain1 = rain(4,4,0.5   ,100,100,150)
rain2 = rain(4,4,0.25  ,150,100,100)
rain3 = rain(4,4,0.2  ,100,150,100)







while True:
    sense.clear()
    rain1.draw()
    rain1.drop()
    rain2.draw()
    rain2.drop()
    
    rain3.draw()
    rain3.drop()
    
    bucket.move()
    bucket.draw()
    
    sleep(0.1)
    
#print(rain1.x)
    
    

