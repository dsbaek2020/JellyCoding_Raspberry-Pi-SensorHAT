#Author : kim yl, jellycoding

from guizero import App, Box, PushButton, Text
from sense_hat import SenseHat
from time import sleep
from random import randint



def clearLED(senseHAT):
    senseHAT.clear()
    


def clear_LED_Button(senseHAT):
    
    clearLED(senseHAT)
    
    new_board = [[None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None]]
    
    for x in range(8):
        for y in range(8):
            button = PushButton(board, text="", grid=[x,y],
                                width=3, command=draw_dot, args=[x,y])

            new_board[x][y] = button
            
    return new_board
            
def draw_dot(x,y):
    board_squares[x][y].text="@"
    board_squares[x][y].disable()
    
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    sense.set_pixel(x,y,(r,g,b))
    
    

sense = SenseHat()
clearLED(sense)

app = App("LED Matrix Canvas")

board = Box(app,layout="grid")
board_squares = clear_LED_Button(sense)
    
clear_button = PushButton(app,
                          text="Clear LEDs",
                          command=clearLED,
                          args=[sense]) 



app.display()

