#coding=utf-8
#Exercise4.2
import math
import turtle
turtle.Turtle().screen.delay(0)
turtle.color("White") #为了不让开始出现的箭头有颜色
Fred=turtle.Turtle()
Fred.hideturtle()

def triangle(t,topAngle,length,bLen):#等腰三角形
    t.fd(length)
    t.rt(180-(180-topAngle)/2)
    t.color("Red") #三角形底线的颜色
    t.fd(bLen)
    t.rt(180-(180-topAngle)/2)
    t.color("Red") #最后一个边为黑色
    t.fd(length)
    t.color("White") #第一个三角形的第一个边是黑，其他的都是白
    
def polygon(t,nside,r):
    topAngle=360/nside
    bLen=2*r*math.sin(math.pi/nside)
    #2选1，太阳(乌龟)还是扇形
#     bLen=-bLen*3#乌龟公式,bLen为负数,nside5为乌龟，多了就是太阳
    nside=int(nside/1.2)#扇形的话除以一个大于1的数,圆形则为1(可试试2,3）
    ###
    t.color("Red") #第一根线的颜色
    for i in range(nside):
        t.lt(180)
        triangle(t, topAngle, r, bLen)
        
if __name__ == '__main__':        
    polygon(Fred,60,100)
    # triangle(Fred, 60, 20,20)
    
    turtle.mainloop()