import sys
import turtle
import math
import random
from datetime import datetime
import PIL.Image as Image
import argparse
class Spiro(object):
    '''
    用来绘制单个繁花曲线，且可复用
    '''
    def __init__(self,x,y,R,r,l,col):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.step = 1
        self.DrawComplete = False
        self.SetParams(x,y,int(R),int(r),float(l),col)
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
        for a in range(0,360*self.nRot+1,self.step):
            a = math.radians(a)
            self.t.setpos(self.x + self.getx(a),self.y + self.gety(a))
        self.DrawComplete = True
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
        """获取随机繁花曲线参数"""
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
        """逐步画"""
        NumOfSpiros = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.DrawComplete:
                NumOfSpiros += 1
        if NumOfSpiros == len(self.spiros):
            self.restart()
        return True
    def restart(self):
        """清空画布，重新随机生成繁花曲线参数"""
        for spiro in self.spiros:
            spiro.clear()
        self.spiros = []
        for i in range(random.randint(1,10)):
            self.spiros.append(Spiro(*self.GetRandomParams()))
def SaveDrawing():
    """
    保存图片至png格式
    依靠Ghostscript，如果没有会出问题
    未测试
    """
    DateStr = datetime.now().strftime("%d-%b-%Y--%H-%M-%S")
    FileName = "spiro-" + DateStr
    Canvas = turtle.getcanvas()
    Canvas.postscript(file=FileName+".eps")
    Img = Image.open(FileName+".eps")
    Img.save(FileName+".png","png")
def main():
    ArgParser = argparse.ArgumentParser()
    ArgParser.add_argument("--sparams",nargs=3,dest="sparams",required=False,help="输入R、r、l") # 设定参数
    args = ArgParser.parse_args() # 分析参数
    turtle.setup(width=0.8, height=0.8)
    turtle.title("Spirograph")
    turtle.onkey(SaveDrawing,"s") # 按s保存图片
    turtle.listen()
    if args.sparams:
        s = Spiro(0,0,*[float(x) for x in args.sparams],(0,0,0))
        s.Draw()
    else:
        sa = SpiroAnimator(random.randint(1,10))
        while sa.update(): pass
    turtle.exitonclick()
if __name__ == '__main__':
    main()