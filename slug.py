#This file make Slug game, with SenseHat
#author : Jung En-Jun, Lee Min-Hung
#advisor: Baek Dae-Seong
#2022.08. ~ 22.09.24
from sense_hat import SenseHat
from time import sleep

#define global variavle---------------
sense = SenseHat()
slug = [[5,3], [6,3],[7,3]]
directionkey = 'up'
v = [0,0]

#define functions--------------------
def change_up(event):
    global directionkey
    if event.action == 'pressed':
        print('up')
        directionkey = 'up'
        
def change_down(event):
    global directionkey
    if event.action == 'pressed':
         print('down')
         directionkey = 'down'
         #print('____directionkey= ', directionkey)
    
def change_right(event):
    global directionkey
    if event.action == 'pressed':
         directionkey = 'right'
         
def change_left(event):
    global directionkey
    if event.action == 'pressed':
         directionkey = 'left'

def draw_slug():
  for part in slug:
    x=part[0]
    y=part[1]
    print(x, y)
    sense.set_pixel(x, y, (100,0,50))
    
def move_slug():
  global v, directionkey
  v[0] = slug[1][0]
  v[1] = slug[1][1]
  slug[2][0] = v[0]
  slug[2][1] = v[1]

  v[0] = slug[0][0]
  v[1] = slug[0][1]
  slug[1][0] = v[0]  
  slug[1][1] = v[1]


  print('directionkey= ', directionkey)
  
  if directionkey == 'down':
    print('hello')
    slug[0][1] += 1
  elif directionkey == 'up':
    slug[0][1] -= 1
  elif directionkey == 'left':
    slug[0][0] -= 1
  else:
    slug[0][0] += 1
    
sense.stick.direction_up = change_up
sense.stick.direction_down = change_down
sense.stick.direction_left = change_left
sense.stick.direction_right = change_right

while True:
  sense.clear()
  draw_slug()
  move_slug()
  sleep(0.5)
