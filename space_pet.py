from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

g = (140, 140, 180) #background
t = (150, 200, 250) #tail
b = (130, 130, 200) #body
l = (128,128,128)  #leg

h = (150, 200, 250) #horn
f = (255, 255, 153) #face
e = (50,50,50) #eye

head = {
'ear' : { 'color' : h,
      'dot': [(4,2), (6,2) ,(4,3)]
        },

'face' : { 'color' : f,
           'dot': [(4,4),(5,3),(5,5),(6,3),(6,4),(6,5),(7,4)]
           
           
           
           
        },
           
'eye' : { 'color' : e,
          'dot': [(5,4)]
        }
    }

body = {
'leg' : { 'color' : l,
          'dot': [(1,6), (3,6) ,(5,6)]
        },

'body' : { 'color' : b,
           'dot': [(1,4), (1,5), (2,3), (2,4), (2,5),
                   (3,3), (3,4), (3,5), (4,5)]
        },
           
'tail' : { 'color' : t,
           'dot': [(0,2),(1,2), (1,3)]
           }     
    }
sense.clear()
'''

i=0
while i<len(head['ear']['dot']):
    pos = head['ear']['dot'][i]
    rgb = head['ear']['color']
    sense.set_pixel(pos[0], pos[1], rgb)
    i+=1
'''
for pos in head['face']['dot']:
    sense.set_pixel(pos[0], pos[1], head['face']['color'])
for pos in head['ear']['dot']:
    sense.set_pixel(pos[0], pos[1], head['ear']['color'])
    
for pos in body['body']['dot']:
    sense.set_pixel(pos[0], pos[1], body['body']['color'])
for pos in body['tail']['dot']:
    sense.set_pixel(pos[0], pos[1], body['tail']['color'])
for pos in body['leg']['dot']:
    sense.set_pixel(pos[0], pos[1], body['leg']['color'])




def drawHead():
    
    for part in head:
        for pos in head[part]['dot']:
            rgb = head[part]['color']
            sense.set_pixel(pos[0], pos[1], rgb)
        
def drawBody():
    
    for part in body:
        for pos in body[part]['dot']:
            rgb = body[part]['color']
            sense.set_pixel(pos[0], pos[1], rgb)


'''     
    for pos in head['face']['dot']:
        rgb = head['face']['color']
        sense.set_pixel(pos[0], pos[1], rgb)
    
    for pos in head['eye']['dot']:
        rgb = head['eye']['color']
        sense.set_pixel(pos[0], pos[1], rgb)
      
    '''
    
'''
sense.clear()
drawHead()
drawBody()
'''