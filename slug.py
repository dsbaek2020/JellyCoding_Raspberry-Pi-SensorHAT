#This file make Slug game, with SenseHat
#author : Kim Min-seo, Jung En-Jun, Lee Min-Hung, kim min-ji
#advisor: Baek Dae-Seong
#2022.08. ~ 22.09.30
from sense_hat import SenseHat
from time import sleep
from random import randint


sense = SenseHat()
slug = [[5,3], [6,3],[7,3]]
directionkey = 'left'
score = 0
appleColor = (243,36,14)


def check_meet_apple():
    slug_x = slug[0][0]
    slug_y = slug[0][1]
    
    if a_x == slug_x and a_y == slug_y:
      return 'meet'
    else:
      return 'noting'

#make draw_apple
def draw_apple(x,  y):
  sense.set_pixel(x, y, appleColor )


apple_y = (0,7)
apple_x = (0,7)


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
        sense.set_pixel(x, y, (100,0,50))


def move_slug():
    global slug, directionkey, k
    #head = slug[0]
    head_x = slug[0][0]
    head_y = slug[0][1]
   
    if directionkey == 'down':
        head_y += 1
    elif directionkey == 'up': 
        head_y -= 1
    elif directionkey == 'left':
        head_x -= 1
    else:
        head_x += 1
               
    slug.insert(0, [head_x, head_y])
    k = slug.pop()
    
    if head_y == 8 or head_y == -1 or \
       head_x == 8 or head_x == -1 :
        return 'game over'
    else:
        return 'I am happy'

       
sense.stick.direction_up = change_up
sense.stick.direction_down = change_down
sense.stick.direction_left = change_left
sense.stick.direction_right = change_right


a_x = randint(0, 7)
a_y = randint(0, 7)

while True:
    sense.clear()
    draw_slug()
    draw_apple(a_x, a_y)
    
    status = move_slug()
    if status  == 'game over':
      sense.show_message('game over')
      print('game over')
      break
    
    if check_meet_apple() == 'meet':
      score += 1
      a_x = randint(0, 7)
      a_y = randint(0, 7)
    
    print(score)
    sleep(0.5)
