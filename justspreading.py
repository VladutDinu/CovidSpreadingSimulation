import turtle
import random
import threading
import names
from time import sleep
FONT = ("Arial", 15, "bold")
ARR={1:[800,400], 2:[-800,400], 3:[800, -300], 4:[-800,-300], 5:[0,400], 6:[0,-400], 7:[800,0], 8:[-800, 0]}
VEC=[[5,5],[-5,5],[5,-5],[-5,-5],[0,5],[0,-5],[5,0],[-5,0]]
INF=[]
HEAL=[]
NOPEOPLE=50
NOITERATIONS=10
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


class myTurtle (threading.Thread):
    def __init__(self, x, y):
        threading.Thread.__init__(self)
        self.noel = turtle.Turtle()
        self.x=x+25
        self.y=y-25
        self.backx=0
        self.backy=0
        self.chance=random.randint(0,100)
        self.infected=False
        self.name=names.get_first_name()
        self.time=0
    def modify(self, x, y):
        self.x=x
        self.y=y
    def runLocations(self, distance):
        self.noel.goto(self.x+distance[0]+random.randint(0,75), self.y-distance[1]-random.randint(0,75))
        
    def runHome(self):
        self.noel.goto(self.backx+random.randint(-40,40), self.backy-random.randint(-40,40))

def initturtles():
    x=[]
    INFECTED={1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[],8:[]}
    PEOPLE={1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[],8:[]}
    rr=random.randint(0,NOPEOPLE-1)
    R={}
    R=set(R)
    for t in range(NOPEOPLE):
        r=random.randint(1,8)
        #print(r, ARR[r][0], ARR[r][1])
        x.append(myTurtle(ARR[r][0], ARR[r][1]))
        PEOPLE[r].append(x[t])
        if t == rr:
            INFECTED[r].append(x[rr])
            x[rr].infected=True
            x[rr].noel.shapesize(1.5,1.5,1)
            x[rr].time+=1
            R.add(r)
    
    for balls in x:
        balls.noel.shape('circle')
        balls.noel.penup()
        balls.noel.speed(1)
        balls.noel.color('white')
    x[rr].noel.color("green", "green")
    f.write("{},{}\n".format(1,NOPEOPLE-1))
    #print('INFECTED: ',INFECTED)
    #print('PEOPLE: ',PEOPLE)
    #print()
    return x, INFECTED, PEOPLE, R

def gotolocation(PEOPLE):
    for x in PEOPLE:
        for t in range(len(PEOPLE[x])):
            PEOPLE[x][t].runLocations(VEC[(t-1)%6])


def drawLocations(FONT):
    drawer=turtle.Turtle()
    draw_rectangle(drawer, 800, 400, 125, 125, 2, 'blue')
    drawer.write('Lidl', align="center", font=FONT)
    draw_rectangle(drawer, -800, 400, 125, 125, 2, 'blue')
    drawer.write('Carrefour', align="center", font=FONT)
    draw_rectangle(drawer, 800, -300, 125, 125, 2, 'blue')
    drawer.write('Kaufland', align="center", font=FONT)
    draw_rectangle(drawer, -800, -300, 125, 125, 2, 'blue')
    drawer.write('Facultate', align="center", font=FONT)
    draw_rectangle(drawer, 0, 400, 125, 125, 2, 'blue')
    drawer.write('Mall', align="center", font=FONT)
    draw_rectangle(drawer, 0, -400, 125, 125, 2, 'blue')
    drawer.write('Munca', align="center", font=FONT)
    draw_rectangle(drawer, 800, 0, 125, 125, 2, 'blue')
    drawer.write('Taboo', align="center", font=FONT)
    draw_rectangle(drawer, -800, 0, 125, 125, 2, 'blue')
    drawer.write('Firma', align="center", font=FONT)
    draw_rectangle(drawer, -50, 50, 100, 100, 2, 'blue')
    drawer.write('Caminescu te pup', align="center", font=FONT)

def days(balls, INFECTED, PEOPLE, R):
    for day in range(NOITERATIONS):
        inf=0
        heal=0
        for x in balls:
            if x.infected:
                inf+=1
                x.time+=1
            else:
                heal+=1
        for x in balls:
            x.runHome()
        for x in balls:
            if x.time>=5:
                balls.remove(x)
                x.noel.ht()

        print(len(balls))
        for number in INFECTED:
            if len(INFECTED[number])!=0:
                for x in PEOPLE[number]:
                    if x.chance<=4 and x.infected==False:
                        x.noel.color('green', 'green')
                        x.noel.shapesize(1.5,1.5,1)
                        x.infected=True
        R={}
        R=set(R)
        INFECTED={1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[],8:[]}
        PEOPLE={1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[],8:[]}
        for t in range(len(balls)):
            r=random.randint(1,8)
            #print(r, ARR[r][0], ARR[r][1])
            #print('t=',t)
            #print('r=', r)
            balls[t].modify(ARR[r][0]+25, ARR[r][1]-25)
            balls[t].chance=random.randint(0,100)
            PEOPLE[r].append(balls[t])
            if balls[t].infected:
                INFECTED[r].append(balls[t])
                R.add(r)
        #print('INFECTED: ',INFECTED)
        #print('PEOPLE: ',PEOPLE)
        #print()
        f.write("{},{}\n".format(inf, heal))
        gotolocation(PEOPLE)
       
    for x in balls:
            x.runHome()
        
    return
        


wn=turtle.Screen()
wn.tracer(1, 0)
wn.screensize(1920,1080)
wn.bgcolor('black')
wn.title('Python Covid Spreading Simulation')


with open("data.csv", "w") as f:
    f.write("Infected, Healthy\n")
    drawLocations(FONT)
    balls, INFECTED, PEOPLE, R=initturtles()
    gotolocation(PEOPLE)

    days(balls, INFECTED, PEOPLE, R)
    #print("tepup")
f.close()
wn.mainloop()