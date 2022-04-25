from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')


def fault(button):
    if button.pin.number==14:
        print(left_name+' you are fault')
    else:
       print(right_name+' you are fault')
       

def pressed(button):
    if button.pin.number==14:
        print(left_name+' won the game')
    else:
       print(right_name+' won the game')
    #exit()
    



for i in [1, 2, 3, 7, 2]:
for i in range(0,5):
    right_button.when_pressed = fault
    left_button.when_pressed = fault
    print('start game')
    led.on()
    sleep(uniform(5, 10))
    led.off()
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    sleep(3)
    print('i value is', i)
