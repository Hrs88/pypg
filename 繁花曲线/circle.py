import turtle
import math
def DrawCircle(x,y,r,t):
    t.up()
    t.setpos(x + r, y)
    t.down()
    for i in range(0,365,1):
        rad = math.radians(i)
        t.setpos(x + r*math.cos(rad), y + r*math.sin(rad))
def main():
    t = turtle.Turtle()
    t.hideturtle()
    DrawCircle(0,0,100,t)
    turtle.exitonclick()
if __name__ == '__main__':
    main()