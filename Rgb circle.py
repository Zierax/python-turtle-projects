from turtle import *
import colorsys
speed(15000)
bgcolor("black")
h = 1
pensize(4)

def main():
    global h
    for i in range(4):
        c=colorsys.hsv_to_rgb(h,1,1)
        fillcolor(c)
        h+=0.004
        begin_fill()
        fd(150)
        rt(60)
        fd(120)
        rt(27)
        end_fill()
for j in range(600):
    main()
    goto(0,0)
    rt(20)
done()