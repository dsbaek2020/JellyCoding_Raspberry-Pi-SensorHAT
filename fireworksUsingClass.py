'''
created by JellyCoding(BAEK DAE SEONG)
name: 불꽃놀이 (Fireworks)
description: 불꽃놀이를 표현하였습니다.
hardware: rpi + senseHAT
date: 2021.1.28

base code : raindropUsingClass.py
'''

from sense_hat import SenseHat
from time import sleep
from random import *

sense = SenseHat()

class light (object):
    def __init__(self, x, y, r,g,b):
        self.startX = x
        self.startY = y
        
        self.x = self.startX
        self.y = self.startY
        self.vx = uniform(-0.5,0.5)
        self.vy = uniform(-0.5,0.5)
        self.rgb = (r,g,b)
        
    def draw(self):
        for i in range(4):
            y= self.y - (self.vy*i)
            x= self.x - (self.vx*i)
            if 0<= y <=7 and 0<= x <=7:
                sense.set_pixel(int(x), int(y), self.rgb)
             
    def move(self):
        self.x +=self.vx
        self.y +=self.vy 
        
        # -2, 9는 senseHat에 LED 범위를 벗어난 가상의 LED 위치이며, 선으로 표현된 빛이
        # 화면에서 사라질때까지 표시되도록 하기 위함
        if int(self.y) == -2 or int(self.y) == 9 \
            or int(self.x) == -2 or int(self.x) == 9:
            self.restart()    
            
    def restart(self):
        self.x = self.startX
        self.y = self.startY
        self.vx = uniform(-0.5,0.5)
        self.vy = uniform(-0.5,0.5)


        
class boom(object):
    def __init__(self, x, y):
      self.startX =x
      self.startY =y
      self.light1 = light(self.startX,self.startY,100,100,150)
      self.light2 = light(self.startX,self.startY,150,100,100)
      self.light3 = light(self.startX,self.startY,100,150,100)
      
    def draw(self):
      self.light1.draw()
      self.light2.draw()
      self.light3.draw()
      
    def move(self):
      self.light1.move()
      self.light2.move()
      self.light3.move()
      
      
b1 = boom(4,4)
b2 = boom(3,3)
      
while True:
    sense.clear()
    b1.draw()
    b2.draw()
    b1.move()
    b2.move()
    sleep(0.1)
