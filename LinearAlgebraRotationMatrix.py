#회전행렬을 이용한 이미지데이터 회전하기
#준비물:
   #라즈베리파이 + SenseHat Board
#만든사람: KYL, BDS
#아직 라즈베리파 센스햇에 되지 않습니다. (알고리즘 만들 있는중)

from sense_hat import SenseHat
from time import sleep
#참고자료: 
 #MIT 선형대수학 강의
 #https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/lecture-30-linear-transformations-and-their-matrices/

 #칸아카데미 강의
 #https://ko.khanacademy.org/math/linear-algebra/matrix-transformations/lin-trans-examples/v/linear-transformation-examples-rotations-in-r2


 
from sense_hat import SenseHat
from time import sleep
from random import randint
import numpy as np
import math


sense = SenseHat()

b = (0, 0, 0)
r = (80, 0, 0)
p = (150, 100, 100)
g = (0,100,0)
y = (100,100,0)


figIn = [[b, b, b, b, b, b, b, b], 
         [b, b, b, b, b, b, b, b],
         [b, p, r, g, r, r, b, b], 
         [b, r, r, r, r, r, b, b],
         [b, r, r, r, y, r, b, b], 
         [b, r, r, r, r, r, b, b],
         [b, b, b, b, b, b, b, b], 
         [b, b, b, b, b, b, b, b]]

'''
figIn = [[b, b, b, b, p, b, b, b], 
         [b, b, b, b, p, b, g, b],
         [b, b, b, b, p, g, b, b], 
         [b, b, b, b, y, y, y, y],
         [b, b, b, b, r, b, b, b], 
         [b, b, b, b, b, r, b, b],
         [b, b, b, b, b, b, b, b], 
         [b, b, b, b, b, b, b, b]]
'''

#figOut = [[]]
figOut = [ [b for j in range(8)] for i in range(8)]


def rotation(th):
    
    global figOut
    
    #clear figOut
    for i in range(8):   # row index of 2D list.
        for j in range(8): # column index of 2D list.
            figOut[i][j] = b

     # th : rotation degree

    for i in range(8):   # row index of 2D list.
      for j in range(8): # column index of 2D list.

        x = j-3
        y = -i+3
        v = np.array([[x],[y]])

        v1x = math.cos(math.radians(th))
        v1y = math.sin(math.radians(th))
        v2x = -1 * math.sin(math.radians(th))
        v2y = math.cos(math.radians(th))
        M = np.array([[v1x, v2x], [v1y, v2y]])

        v_out = M.dot(v)



        #print ('v=', v, '\n', 'v_out=', v_out)

        v_outX = v_out[0][0]
        v_outY = v_out[1][0]


        j_out =  v_outX + 3
        i_out = -v_outY + 3

        j_out = int(round(j_out))
        i_out = int(round(i_out)) 

        color = figIn[i][j]
        #print(color)

        #print(round(i_out))
                 

        if 0<= j_out <= 7 and 0<= i_out <=7:
          #print(i_out, j_out) 
          #print(color)
          figOut[i_out][j_out] = color


    #print(figOut)
          
for th in range(0,360,1):
    #print('theta=', th)
    rotation(th)
    sense.clear()
    #sense.set_pixels([pixel for line in figOut for pixel in line])
    sense.set_pixels(sum(figOut,[]))
    sleep(0.01)


