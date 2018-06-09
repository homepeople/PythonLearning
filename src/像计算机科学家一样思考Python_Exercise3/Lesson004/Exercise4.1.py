#coding=utf-8
#Exercise4.1
import turtle
import math

# turtle.speed(0)
turtle.Turtle().screen.delay(0)
bob=turtle.Turtle()
bob.hideturtle()
def polyline(t,nside,length,angle):
    for i in range(nside):#range括号内只能用integer
        t.fd(length)
        t.lt(angle)   
           
def polygon(t,nside,length):
    angle=360/nside
    polyline(t, nside, length, angle)
    
def circle(t,r):
     circumference=2*math.pi*r
     nside=50
     angle=360/nside
     length=circumference/50
     polygon(t, nside, length)

def arc(t,r,angle):     
     arc_length=2*math.pi*r*angle/360
     nside=int(arc_length/3)+1
     step_length=arc_length/nside
     step_angle=float(angle)/nside
     polyline(t, nside, step_length, step_angle)
     
def arc_leaf(t,r,angle):
    arc(t,r,angle)
    t.lt(180-angle)#减去偏转的角度
    arc(t,r,angle)
    
def arc_flower(t,r,angle,nleaf):
    step_angle=360/nleaf
    for i in range(nleaf):
        t.lt(step_angle+180-angle)#因为要回头所以要加上180
        arc_leaf(t,r,angle)

arc_flower(bob,200,60,12)
turtle.mainloop()