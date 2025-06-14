import turtle
from main import Point
from main import DrawLine
def Drawtri(a,b,c,t):
    """绘制三角"""
    DrawLine(a, b, t)
    DrawLine(b, c, t)
    DrawLine(c, a, t)
def _DrawSPtri(a,b,c,t):
    p1 = Point((a.x + b.x) / 2, (a.y + b.y) / 2)
    p2 = Point((b.x + c.x) / 2, (b.y + c.y) / 2)
    p3 = Point((c.x + a.x) / 2, (c.y + a.y) / 2)
    Drawtri(p1,p2,p3,t)
    d = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
    if d > 10:
        _DrawSPtri(a,p3,p1,t)
        _DrawSPtri(c,p2,p3,t)
        _DrawSPtri(b,p1,p2,t)
def DrawSPtri(a,b,c,t):
    """绘制谢尔平斯基三角"""
    Drawtri(a,b,c,t)
    _DrawSPtri(a,b,c,t)
def main():
    t = turtle.Turtle()
    t.hideturtle()
    a = Point(-100, 0)
    b = Point(0, -173.2)
    c = Point(100, 0)
    DrawSPtri(a,b,c,t)
    turtle.Screen().exitonclick()
if __name__ == '__main__':
    main()