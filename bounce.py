import py5

pos_x = 0
pos_y = 250
direction_x = 5
direction_y = 1

def setup ():
    py5.size(480, 500)

def draw():
    global pos_x, pos_y, direction_x,direction_y
    py5.background(120)
    py5.fill(0,100,0)
    py5.no_stroke()
    py5.ellipse( pos_x, pos_y , 60 , 60)
    pos_x = pos_x + direction_x
    pos_y = pos_y + direction_y
    if   pos_x > 450 :
        direction_x = -5
    if pos_x == 30 :
        direction_x = 5
    if pos_y > 470:
        direction_y = -1
    if pos_y == 30 :
        direction_y = 1  
        


py5.run_sketch()




 