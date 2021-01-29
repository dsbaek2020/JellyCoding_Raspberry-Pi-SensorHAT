#!/bin/python3

'''
Author : Baek Dae Seong, Jelly Coding 
         (south korea, kyungsangnam-do, changwon-si)
         
This code inspired 'Flappy Astronaut' from Code Club.
https://projects.raspberrypi.org/en/projects/flappy-astronaut

Web based IDE and Simulator 
https://trinket.io/embed/python/6e4cb01c6b

Sense HAT quick guide
https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/9
'''

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

class bird(object):
  def __init__(self):
    self.x = 0
    self.y = 3
    self.vy =0
    self.g = 0.1
    self.a = 0
    
    self.color = (0,100,0)
    
  def draw(self):
    sense.set_pixel(self.x, int(self.y), self.color)
    
  def move(self):
    print('acc:', self.a,'spd:', self.vy,'y:', self.y)
    
    self.vy = self.vy + self.g + self.a
    self.y+=self.vy
    if self.y > 7:
      self.y =7
    if self.y < 0:
      self.y =0
    
    
  def move_up(self,event):
    if event.action == 'pressed':
      self.a = -0.5
    if event.action == 'released':
      self.a = 0
      
  def move_down(self,event):
    if event.action == 'pressed':
      self.a = 0.5
    if event.action == 'released':
      self.a = 0
    
  def checkCollision(self):
    return 0

yourBird = bird()
    
sense.stick.direction_up = yourBird.move_up
sense.stick.direction_down = yourBird.move_down

while True:
  sense.clear()
  yourBird.move()
  yourBird.draw()
  sleep(0.5)
  



