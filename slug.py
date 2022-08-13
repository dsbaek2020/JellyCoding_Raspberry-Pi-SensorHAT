from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

slug = [[5,3], [6,3],[7,3]]
directionkey = 'left'

v = [0,0]
def draw_slug():
  for part in slug:
    x=part[0]
    y=part[1]
    print(x, y)
    sense.set_pixel(x,y, (100,0,50))
    
def move_slug():
  global v
  v[0] = slug[1][0]
  v[1] = slug[1][1]
  slug[2][0] = v[0]
  slug[2][1] = v[1]

  v[0] = slug[0][0]
  v[1] = slug[0][1]
  slug[1][0] = v[0]
  slug[1][1] = v[1]


  if directionkey == 'down':
    slug[0][1] += 1
  elif directionkey == 'up':
    slug[0][1] -= 1
  elif directionkey == 'left':
    slug[0][0] -= 1
  else:
    slug[0][0] += 1
    
while True:
  sense.clear()
  draw_slug()
  move_slug()
  sleep(0.5)

#while True:
  #move slug()
  #sleep(0.2)
