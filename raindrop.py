'''
name: Rain Art
hardware: RPI sensor HAT 
author : CHOI SY
support : BAEK DS
edit: 2020.1.20
'''
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()


#case1
g = (0,0,0)
a = (50,50,50)
b = (100,100,100)
c = (170,170,170)
d = (255,255,255)

#case2
e = (0,0,0)#start
f = (50,50,50)
q = (100,100,100)

h = (150,150,150)
i = (200,200,200)
j = (255,255,255)


while True:
    x = randint(0,7)
    #무한 반복 
    for y in range(11):
       
        rain = [{'xy':(x,0+y), 'color':j},
                {'xy':(x,-1+y), 'color':i},
                {'xy':(x,-2+y), 'color':h},
                {'xy':(x,-3+y), 'color':q}]


        '''
        drops =[g,a,g,a,g,a,g,e,
                g,g,g,g,g,g,g,f,
                g,b,g,b,g,b,g,q,
                g,g,g,g,g,g,g,h,
                g,c,g,c,g,c,g,i,
                g,g,g,g,g,g,g,j,
                g,d,g,d,g,d,g,g,
                g,g,g,g,g,g,g,g ]
        '''
        drops =[g for i in range(64)]
        #반복 4번
        for part in rain:
            x = part['xy'][0]
            y = part['xy'][1]
            if( 0<= y <=7):
                n = x + (y*8)
                drops[n] = part['color'] 
         
        sense.clear()
        sense.set_pixels(drops)
        sleep(0.1)
