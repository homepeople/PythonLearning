#coding=utf-8
#Exercise4.2
import math
import turtle
turtle.Turtle().screen.delay(0)
Fred=turtle.Turtle()
def triangle(t,topAngle,length,bLen):
    t.fd(length)
    t.rt(180-(180-topAngle)/2)
    t.fd(bLen)
    t.rt(180-(180-topAngle)/2)
    t.fd(length)
def polygon(t,nside,r):
    topAngle=360/nside
    bLen=2*r*math.sin(math.pi/nside)
#     bLen=-1*bLen*3#乌龟公式,bLen为负数,nside5为乌龟，多了就是太阳
    nside=int(nside/2.5)#扇形的话除以一个大于1的数
    for i in range(nside):
        t.lt(180)
        triangle(t, topAngle, r, bLen)
        
polygon(Fred,18,50)    
# triangle(Fred, 60, 20,20)

turtle.mainloop()