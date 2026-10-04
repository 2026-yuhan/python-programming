# 터틀 그래픽과 반복을 사용하여 싸인(sine) 그래프를 그려보자.
# 거북이를 싸인값에 따라서 움직이면 된다.

import turtle
import math

t = turtle.Turtle()

t.shape("turtle")
t.color("orange")

for degree in range(360):
    radian = math.pi * degree / 180
    y = math.sin(radian) * 100

    t.goto(degree, y)

turtle.done()