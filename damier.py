import py5




def setup():
    py5.size(800,800)
    py5.no_loop()

def draw():
   
    py5.background(255,255,0)
    for i in range(0,py5.height,100):
        for j in range(0, py5.width, 100):
            if (i/100)%2 == 0:
                if (j/100)%2 == 0:
                    py5.fill(255,255, 255)
                    py5.rect(j, i, 100, 100)
                elif (j/100)%2 != 0:
                    py5.fill(0,0,0)
                    py5.rect(j, i, 100, 100)
            elif (i/100)%2 != 0: 
                if (j/100)%2 != 0:
                    py5.fill(255,255, 255)
                    py5.rect(j, i, 100, 100)
                elif (j/100)%2 == 0:
                    py5.fill(0,0,0)
                    py5.rect(j, i, 100, 100)



py5.run_sketch()