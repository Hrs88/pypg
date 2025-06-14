import turtle
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def DrawLine(begin,end,t):
    # 绘制线段
    t.up()
    t.setpos(begin.x, begin.y)
    t.down()
    t.setpos(end.x, end.y)
def DrawKSF(a,b,t):
    # 绘制科赫雪花
    # 计算p1,p2,p3
    d = ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5
    r = d / 3
    h = r * 3**0.5 / 2
    n = Point((b.y - a.y) / d, (a.x - b.x) / d)
    c = Point((a.x + b.x) / 2, (a.y + b.y) / 2)
    p1 = Point((a.x*2 + b.x) / 3, (a.y*2 + b.y) / 3)
    p3 = Point((a.x + b.x*2) / 3, (a.y + b.y*2) / 3)
    p2 = Point(c.x + h * n.x, c.y + h * n.y)
    if d > 10:
        # 如果像素大于10，进入递归
        DrawKSF(a,p1,t)  # 计算第一条边
        DrawKSF(p1,p2,t) # 计算第二条边
        DrawKSF(p2,p3,t) # 计算第三条边
        DrawKSF(p3,b,t)  # 计算第四条边
    else:
        # 如果像素小于10，绘制并退出递归
        DrawLine(a,p1,t)  # 绘制第一条边
        DrawLine(p1,p2,t) # 绘制第二条边
        DrawLine(p2,p3,t) # 绘制第三条边
        DrawLine(p3,b,t)  # 绘制第四条边
def main():
    t = turtle.Turtle() # 创建海龟对象
    t.hideturtle()  # 隐藏海龟
    # 构建起始三角
    a = Point(-100,0)
    b = Point(0,-173.2)
    c = Point(100,0)
    # 绘制各边
    DrawKSF(a,b,t)
    DrawKSF(b,c,t)
    DrawKSF(c,a,t)
    #turtle.mainloop() # 保存绘布
    turtle.Screen().exitonclick() # 用户单击后退出
if __name__ == '__main__':
    main()