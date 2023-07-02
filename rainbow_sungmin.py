
'''

print('hello')

print(3+7)

answer = int(input('당신의 나이는?'))

cpu_age = 12

if answer > cpu_age:
  print('나보다 형이군요')

else:
  print('나보다 어리군요')


print('bye~~')



'''

from sense_hat import SenseHat
sense = SenseHat()

#while True:
#for i in range(2):
#  sense.show_message("what is 2309487239845720920893472098475208934*0?",text_colour=(255, 255, 0),back_colour=(0, 0, 255), scroll_speed=(0.05))
#  sense.show_message("YOU MUST KNOW THIS QUESTIONS ANSWER.")
#  sense.show_message("bro its 0 lol")

sense.clear()

R = [255, 0, 0]
O = [255, 165, 0]
Y = [255, 255, 0]
G = [0, 128, 0]
B = [0, 0, 255]
I = [25, 25, 112]
V = [238, 130, 238]
X = [0, 0, 0]


#from time import sleep

#all_color = [R, O, Y, G, B, I, V]

#for i in range(7):
# print( i )
# sense.clear( all_color[i] )
# sleep(0.1)

# sense.clear()
# sleep(0.2)



rainbow = [
R, R, R, R, R, R, R, R,
R, O, O, O, O, O, O, O,
R, O, Y, Y, Y, Y, Y, Y,
R, O, Y, G, G, G, G, G,
R, O, Y, G, B, B, B, B,
R, O, Y, G, B, I, I, I,
R, O, Y, G, B, I, V, V,
R, O, Y, G, B, I, V, X
]


sense.set_pixels(rainbow)
while True:
  temp = sense.get_temperature()
  sense.show_message(str(temp))


