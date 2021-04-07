
import math
import  numpy as np
from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

b = (0, 0, 0)
r = (180, 0, 0)
p = (150, 100, 100)
g = (0,150,0)
y = (150,150,0)

# 원본 그림 
figIn = [[b, b, b, b, b, b, b, b], 
         [b, b, b, b, b, y, b, b],
         [b, p, r, g, r, r, b, b], 
         [b, r, r, r, r, r, b, b],
         [b, r, r, r, y, r, b, b], 
         [b, r, r, r, r, r, b, b],
         [b, b, b, b, b, b, b, b], 
         [b, b, b, b, b, b, b, b]]

class Image(object):

  def __init__(self, Img):
    self.inputImg = Img
    self.outImg = [ [b for j in range(8)] for i in range(8)]

  def clearOutImg(self):
     #clear figOut
    for i in range(8):   # row index of 2D list.
        for j in range(8): # column index of 2D list.
            self.outImg[i][j] = b

  def rotation(self, th):

    self.clearOutImg()
    for i in range(8):   # row index of 2D list.
      for j in range(8): # column index of 2D list.


        color = self.inputImg[i][j]

        x = j-3
        y = -i+3

        #print (x,y)

        v = np.array([[x],[y]])

        v1x = math.cos(math.radians(th))
        v1y = math.sin(math.radians(th))
        v2x = -1 * math.sin(math.radians(th))
        v2y = math.cos(math.radians(th))

        M = np.array([[v1x, v2x], [v1y, v2y]])

        v_out = M.dot(v)

        #print (v_out)

        x_o = v_out[0][0]
        y_o = v_out[1][0]

        #print(x_o,y_o)

        j_o = x_o+3
        i_o = -y_o+3

        j_o = int(round(j_o))  
        i_o = int(round(i_o))

        if 0 <= j_o <=7 and 0<= i_o <=7:
          self.outImg[i_o][j_o] = color 



img1 =  Image(figIn) 

while True:
  for degree in range(0,360,1):
    img1.rotation(degree)
    #sense.set_pixels([pixel for line in figOut for pixel in line])
    sense.set_pixels(sum(img1.outImg,[]))
    #sleep(0.01)




