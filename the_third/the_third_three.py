from turtle import Turtle, TurtleScreen, Screen

# 创建画布
screen = Screen()

# 创建画笔
pen = Turtle()

# 设置画笔的颜色和线条宽度
pen.color("red")
pen.pensize(2)

# 设置TurtleScreen
ts = TurtleScreen(screen)

# 绘制五角星
for i in range(5):
    pen.forward(100)
    pen.right(144)

# 隐藏画笔
pen.hideturtle()

# 关闭画布
ts.bye()
