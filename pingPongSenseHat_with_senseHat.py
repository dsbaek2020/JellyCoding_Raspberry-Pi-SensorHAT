from sense_hat import SenseHat
from time import sleep

sense = SenseHat() #센스햇 클래스의 생성자를 호출하고 생성된 객체는  sense 이름으로 가리켜(바인딩) 진다.

#sense.show_message('hello world')
sense.clear()

sense = SenseHat()
#sense.set_pixel(0,2,0,0,255)
#sense.set_pixel(7,4,255,0,0)
white = (255,255,255)
bat_y = 2

ball_position = [1, 3]
ball_velocity = [1, 1]

ai_y = 3


def draw_bat():
    sense.set_pixel(0, bat_y, (100, 100, 0))
    sense.set_pixel(0,bat_y+1,(100, 0, 0)  )
    sense.set_pixel(0,bat_y-1,(0, 100, 0)  )

#draw_bat()


def move_up(event):
  global bat_y
  if event.action == 'pressed' and bat_y > 1  :
    bat_y -= 1

def move_down(event):
  global bat_y
  if event.action == 'pressed' and bat_y < 6:
    bat_y += 1

def draw_ball():
  ball_position[0] += ball_velocity[0]
  ball_position[1] += ball_velocity[1]

  if ball_position[0] == 7 or  ball_position[0] == 0:
    if check_collision(0, bat_y)  == False and  check_collision(0, ai_y) == False :
      ball_velocity[0] = -ball_velocity[0]

  if ball_position[1] == 7 or  ball_position[1] == 0:
    ball_velocity[1] = -ball_velocity[1]

  if ball_position[0] == 0  and check_collision(0, bat_y)== False:
    sense.show_message('YOU LOSE')
  
  sense.set_pixel(ball_position[0],ball_position[1],(50,0,100))

def draw_bat_AI():
  sense.set_pixel(7, ai_y, (100, 100, 0))
  sense.set_pixel(7, ai_y+1, (100, 100, 0))
  sense.set_pixel(7, ai_y-1, (100, 100, 0))



def check_collision(x, y):
  if y-1<=ball_position[1]<=y+1 and x == 0:
    return True
  else:
    return False




sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while True:
   sense.clear() 
   draw_bat()
   draw_ball()
   draw_bat_AI()
   if check_collision(0, bat_y) or check_collision(7, ai_y):
     ball_velocity[0] = -ball_velocity[0]

   sleep(0.5)






