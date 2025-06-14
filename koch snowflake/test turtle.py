import turtle
def draw_triangle(x1,y1,x2,y2,x3,y3,t):
    t.up() # 抬起画笔
    t.setpos(x1,y1) # 将画笔放到第一个位置
    t.down() # 放下画笔
    t.setpos(x2,y2) # 将画笔移动到第二个位置
    t.setpos(x3,y3) # 将画笔移动到第三个位置
    t.setpos(x1,y1) # 将画笔移动回第一个位置
    t.up() # 抬起画笔
def main():
    t = turtle.Turtle() # 创建海龟对象
    t.hideturtle() # 隐藏海龟
    draw_triangle(-100,0,0,-173.2,100,0,t) # 绘制三角
    turtle.mainloop() # 保留绘纸
if __name__ == '__main__':
    main() # 调用main