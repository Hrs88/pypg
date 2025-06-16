import turtle
import math
import random
class LogarithmicSpiral():
    def __init__(self,x,y,a,b,col):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.step = 1
        self.DrawComplete = False
        self.SetParams(x,y,a,b,col)
        self.restart()
    def SetParams(self,x,y,a,b,col):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.col = col
        self.nRot = random.randint(3,100)
        self.getx = lambda ra : self.a * math.e**(self.b * ra) * math.cos(ra)
        self.gety = lambda ra : self.a * math.e**(self.b * ra) * math.sin(ra)
    def restart(self):
        self.DrawComplete = False
        self.t.up()
        self.t.setpos(self.x + self.getx(0.0), self.y + self.gety(0.0))
        self.t.down()
        self.t.color(*self.col)
    def Draw(self):
        for i in range(0,360*self.nRot,self.step):
            i = math.radians(i)
            self.t.setpos(self.x + self.getx(i), self.y + self.gety(i))
        self.DrawComplete = True
def main():
    ls = LogarithmicSpiral(0,0,20,0.05,(0,0,0))
    ls.Draw()
    turtle.exitonclick()
if __name__ == '__main__':
    main()