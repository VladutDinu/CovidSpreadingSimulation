import turtle
import random
FONT = ("Arial", 15, "bold")
def draw_rectangle(board,x,y,width,height,size,color):
  board.pencolor(color)
  board.pensize(size)
  board.setheading(0)
 
  board.up()
  board.speed(0)
  board.goto(x,y)
  board.down()
  # draw top
  board.forward(width)
  # draw right
  board.right(90)
  board.forward(height)
  # draw bottom
  board.right(90)
  board.forward(width)
  # draw left
  board.right(90)
  board.forward(height)
  board.end_fill()
def initturtles():
    x=[turtle.Turtle() for x in range(10)]
    r=random.randint(0,9)
    for balls in x:
        balls.shape('circle')
        balls.penup()
        balls.speed(1)
        balls.color('white')
    x[r].color("green", "green")
    return x

def gotolocation(balls, locations):
    for x in balls:
        t=random.randint(1, len(locations))
        #x._tracer(10,20)
        x.goto(locations[t][0]+25,locations[t][1]-25)
    

        

def drawLocations(FONT):
    drawer=turtle.Turtle()
    draw_rectangle(drawer, 300, 300, 50, 50, 2, 'blue')
    drawer.write('Lidl', align="center", font=FONT)
    draw_rectangle(drawer, -300, 300, 50, 50, 2, 'blue')
    drawer.write('Carrefour', align="center", font=FONT)
    draw_rectangle(drawer, 300, -300, 50, 50, 2, 'blue')
    drawer.write('Kaufland', align="center", font=FONT)
    draw_rectangle(drawer, -300, -300, 50, 50, 2, 'blue')
    drawer.write('Facultate', align="center", font=FONT)
    draw_rectangle(drawer, -25, 25, 50, 50, 2, 'blue')
    drawer.write('Acasa', align="center", font=FONT)

wn=turtle.Screen()
wn.tracer(1, 1)
wn.screensize(480,640)
wn.bgcolor('black')
wn.title('pula')


arr={1:[300,300], 2:[-300,300], 3:[300, -300], 4:[-300,-300]}
drawLocations(FONT)
balls=initturtles()
wn.ontimer(gotolocation(balls, arr), 1)


wn.mainloop()