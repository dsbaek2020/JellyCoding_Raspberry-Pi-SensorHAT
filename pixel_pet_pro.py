from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

g = (140, 140, 180) #background
t = (150, 200, 250) #tail
b = (130, 130, 200) #body
l = (128,128,128) #leg

h = (150, 200, 250) #horn
f = (255, 255, 153) #face
e = (50,50,50) #eye
x =(10,10,10)

head = {
'ear' : { 'color' : h,
      'dot': [(4,2), (6,2) ,(4,3)]
        },

'face' : { 'color' : f,
           'dot': [(4,4),(5,3),(5,5),(6,3),(6,4),(6,5),(7,4)]
        },
           

'eye' : { 'color' : e,
      'dot': [(5,5)] }  }

body = {
'leg' : { 'color' : l,
      'dot': [(1,6), (3,6) ,(5,6)] },

'body' : { 'color' : b,
      'dot': [(1,4), (1,5), (2,3), (2,4), (2,5),
              (3,3), (3,4), (3,5), (4,5)] },
           
'tail' : { 'color' : t,
      'dot': [(0,2),(1,2), (1,3)] }     
}

'''
i=0
while(i<len(head['ear']['dot'])
    #do something
    pos = head['ear']['dot'][i]
    sense.set_pixel(pos[0], pos[1], rgb)
    i+=1;

for pos in head['ear']['dot']:
    sense.set_pixel(pos[0], pos[1], rgb)
    
'''

bg =[ x for i in range(64)]

def drawHead():
    
    for part in head:
        y=-7 # y value in virtual screen 
        while(y!=0):
            sense.clear()  #지우기 
            #그래픽 리스트에 있는 64개의 배경 을 한번에 그린다. set_pixels를 이용
            sense.set_pixels(bg)
            
            for pos in head[part]['dot']:  #모양 그리기 
                rgb = head[part]['color']
                if(pos[1]+y >=0):   # 수직 좌표가0이상이면 그려라  
                    sense.set_pixel(pos[0], pos[1]+y, rgb)
            y+=1 #좌표를 한칸 밑으로 내리기 
            sleep(0.5) #0.5초 쉬기 
        #최종 위치에 그려진 그림을 배경 리스트에 저장한다.
        for pos in head[part]['dot']:
            n = pos[0] + (pos[1] * 8)
            bg[n] = head[part]['color']
        
 
            
        
def drawBody():
    
    for part in body:
        for pos in body[part]['dot']:
            rgb = body[part]['color']
            sense.set_pixel(pos[0], pos[1], rgb)
            sleep(0.3)
'''
        
    for pos in head['face']['dot']:
        rgb = head['face']['color']
        sense.set_pixel(pos[0], pos[1], rgb)
        
    for pos in head['nose']['dot']:
        rgb = head['nose']['color']
        sense.set_pixel(pos[0], pos[1], rgb)
    
    for pos in head['eye']['dot']:
        rgb = head['eye']['color']
        sense.set_pixel(pos[0], pos[1], rgb)
        
        '''
    
    

sense.clear()
drawHead()
drawBody()




