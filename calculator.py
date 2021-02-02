#calculator program
#made by lim dong ha
#build date: 2021 2 2
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

sense.show_message('hi ~:)')



print('This is calculator')
print('''
                           __ _..._ _ 
                           \ `)    `(/
                           /`       \
                           |   d  b  |
             .-"````"=-..--\=    Y  /=
           /`               `-.__=.'
    _     / /\                 /o
   ( \   / / |                 |
    \ '-' /   &gt;    /`""--.    /
     '---'   /    ||      |   \\
             \___,,))      \_,,))     asciiart.cc


''')


def drawHeart():
  print('''
        __________  __________
       /           \/           \
      |             |             |
      |                           |
      |                           |
      \                           /
       \                         /
  ''')
  
heart = [
    '#@####@#',
    '@#@##@#@',
    '@##@@##@',
    '@######@',
    '@######@',
    '#@####@#',
    '##@##@##',
    '###@@###'
    ]


def drawHeart2():
    sense.clear()
    for y in range(8):
        line = heart[y]
        
        for x in range(8):
            if line[x] == '@':
                sense.set_pixel(x,y, (100,200,50))
    

#drawHeart2()
    
    
'''
a = input('Type any number:')
a = int(a)


c = a + 5
c = a * 2


print('result = ', c)

if c > 10:
 
'''  


#input first number, save number to a
a= input('Type any number: ')
a= int(a)
#input second number, save number to b
b= input('Type any number: ')
b= int(b)


#input operation (+, -, / , *, %)
#calculation c = (a )operation (b)
operation= input('Type your operation')


if operation == '+':
  c = a + b
elif operation == '-':
  c = a-b
elif operation == '*':
  c = a*b
  
print(c, '=', str(a)+operation+str(b))


    


#print result
#if c % 10 == 0, then print heart shape

if c%10 == 0:
    drawHeart2()
    



