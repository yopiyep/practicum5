import turtle
import math

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(xc, yc - r)
t.pendown()
t.circle(r)

t.penup()
t.goto(x, y)
t.pendown()
t.dot(10, "red")

dis = math.sqrt((x - xc)**2 + (y - yc)**2)

if dis == r:
    print("Точка находится на окружности")
elif dis < r:
    print("Точка находится внутри окружности")
else:
    print("Точка находится за пределами окружности")


turtle.done()
