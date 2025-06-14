import sys
import turtle
import math
import random
class Spiro(object):
    '''
    用来绘制单个繁花曲线，且可复用
    '''
    def __init__(self,x,y,R,r,l,col):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.step = 1
        self.DrawComplete = False
        self.SetParams(x,y,R,r,l,col)
        self.restart()
    def SetParams(self,x,y,R,r,l,col):
        '''
        设置繁花曲线的中心、大圆半径、小圆半径、指定轨迹、轨迹颜色
        计算k、nRot等所需值
        '''
        self.x = x
        self.y = y
        self.R = R
        self.r = r
        self.l = l
        self.col = col
        self.k = r / R
        self.a = 0
        Gcd = math.gcd(self.R,self.r)
        self.nRot = r // Gcd
        self.getx = lambda a : self.R*((1-self.k)*math.cos(a) + self.l*self.k*math.cos((1-self.k)*a/self.k))
        self.gety = lambda a : self.R*((1-self.k)*math.sin(a) - self.l*self.k*math.sin((1-self.k)*a/self.k))
    def restart(self):
        '''
        清空状态，并将海龟置于起始位置
        '''
        self.DrawComplete = False
        self.t.up()
        self.t.setpos(self.x + self.getx(0.0),self.y + self.gety(0.0))
        self.t.down()
        self.t.color(*self.col)
    def Draw(self):
        '''一次性画完'''
        self.DrawComplete = True
        for a in range(0,360*self.nRot+1,self.step):
            a = math.radians(a)
            self.t.setpos(self.x + self.getx(a),self.y + self.gety(a))
    def update(self):
        '''逐步画'''
        if self.DrawComplete:
            return
        self.a += self.step
        a = math.radians(self.a)
        self.t.setpos(self.x + self.getx(a),self.y + self.gety(a))
        if self.a > 360*self.nRot:
            self.DrawComplete = True
    def clear(self): self.t.clear()
class SpiroAnimator(object):
    def __init__(self,N):
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        self.spiros = []
        for i in range(N):
            self.spiros.append(Spiro(*self.GetRandomParams()))
    def GetRandomParams(self):
        R = random.randint(50,min(self.width,self.height)//2)
        r = random.randint(10,9*R//10)
        l = random.uniform(0.1,0.9)
        x = random.randint(-self.width//4,self.width//4)
        y = random.randint(-self.height//4,self.height//4)
        col = (
            random.random(),
            random.random(),
            random.random()
        )
        return (x,y,R,r,l,col)
        # return (0,0,220,65,0.8,(0,0,0))
    def update(self):
        NumOfSpiros = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.DrawComplete:
                NumOfSpiros += 1
        if NumOfSpiros == len(self.spiros):
            self.restart()
        return True
    def restart(self):
        for spiro in self.spiros:
            spiro.clear()
        self.spiros = []
        for i in range(random.randint(1,10)):
            self.spiros.append(Spiro(*self.GetRandomParams()))
def main():
    sa = SpiroAnimator(2)
    while sa.update():
        pass
    turtle.exitonclick()
if __name__ == '__main__':
    main()