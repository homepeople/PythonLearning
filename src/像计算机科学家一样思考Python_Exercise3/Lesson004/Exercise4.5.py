#coding=utf-8
#Exercise4.5
import turtle
import math
import threading
from turtledemo.lindenmayer import draw
turtle.Turtle().screen.delay(0)
Fred=turtle.Turtle()

def polyline(t,nside,length,angle):
    for i in range(nside):#range括号内只能用integer
         t.fd(length)
         t.lt(angle)
        
def arc(t,r,angle):     
     arc_length=2*math.pi*r*angle/360
     nside=int(arc_length/3)+1
     step_length=arc_length/nside
     step_angle=float(angle)/nside
     polyline(t, nside, step_length, step_angle)

def  Achimedeanspiral(t,v,w,ti):
     for i in range(ti):
         arc(t,v*i,w)
#      t.lt(90)#螺线变相封口
#      t.fd(v*w) #螺线封口 划线

def draw_spiral(t,nside,length=8,a=0.05,b=0.0002): 
    theta=0.0
    for i in range(nside):
         t.fd(length)
         dtheta=1/(a+b*theta)
         print(dtheta)
         t.lt(dtheta)
         theta+=dtheta
        
draw_spiral(Fred, 200)
# Achimedeanspiral(Fred,2,40,50)
turtle.mainloop()