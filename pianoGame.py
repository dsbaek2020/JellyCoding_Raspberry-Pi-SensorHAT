#Date: 21.01.27

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

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
        for i in range(3):
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
        
        


class dot(object):
    def __init__(self,x,r,g,b):
        self.x = x
        self.y = 7
        self.rgb = (r,g,b)
        
    def get_x(self):
        return self.x
        
    def draw(self):
        sense.set_pixel(self.x, self.y, self.rgb)
        

    def move_left(self,event):
        if event.action =='pressed'and self.x >= 1:
            self.x -= 1
            
    def move_right(self,event):
        if event.action =='pressed' and self.x <= 6 :
            self.x += 1
    
    def increase(self):
        r = self.rgb[0] + 10
        if r > 255:
            r = 255
            
        self.rgb = (r,self.rgb[1], self.rgb[2])
        
    def DetectCrash(self,rgb):
        if rgb[0] !=0 and rgb[1] != 0 and rgb[2] !=0:
            self.increase()




#author : kim min ji

rain1 = rain(0,0,0.5,100,100,150)
rain2 = rain(7,0,0.25,150,100,100)
rain3 = rain(3,0,1.0,100,150,100)

bucket = dot(3,100,0,0)

sense.stick.direction_left = bucket.move_left
sense.stick.direction_right = bucket.move_right


while True:
    sense.clear()
    
    
    
    rain1.draw()
    rain1.drop()
    rain2.draw()
    rain2.drop()
    
    rain3.draw()
    rain3.drop()
    bucket.draw()
    

    bucket.DetectCrash(sense.get_pixel(bucket.get_x(),6))

    sleep(0.1)
    
#print(rain1.x)
    
    
