#coding=utf-8
#Exercise5.5
import turtle
import time


turtle.color("White") #为了不让开始出现的箭头有颜色
# turtle.speed(0)
Fred=turtle.Turtle()  #Fred为turtle的实例
Fred.speed(0)         #Fred这头乌龟的速度，注意如果Fred实例之前对turtle的速度修改，但实例化后Fred的速度是turtle的默认值，和turtle修改的值无关
Fred.pensize(2)  
Fred.screen.delay(0) 
# Fred.color("White")
Fred.hideturtle()

#Koch spiral recursion

def Koch(t,length,miniLength):
    if abs(length) < abs(miniLength):
         t.fd(length)
    else:
         Koch(t,length/3,miniLength)
         t.lt(60)
         Koch(t,length/3,miniLength) 
         t.rt(120)
         Koch(t,length/3,miniLength)
         t.lt(60)
         Koch(t,length/3,miniLength)

#Draw a snowflake by Koch spiral
def snowflake(t,length,minilength):
    t.color("black", "cyan")  
    t.begin_fill() 
    for i in range(3):
         Koch(t, length,minilength)
         t.rt(120)
    t.end_fill()
#To use snowflake to draw 6 flake,it will draw more Koch spiral than fastsixflake.The whole Koch spiral would be 23       
def slowsixflake(t,length,minilength):
     t.color("black", "cyan") 
     for i in range(6):
        t.begin_fill()
        snowflake(t,-length,minilength)
        t.end_fill()
        if i <5:#with this "if" it would draw 5 more Koch spiral than fastsixflake，without this "if" it'll be 6 more              
             Koch(t,-length,minilength)#return to the connection point of next flake，without this line 6 flake will stick together through the first point
             t.lt(60)  
             
#fastsixflake only use Koch to draw the 6 flake.The whole Koch spiral will be 18            
def fastsixflake(t,length,minilength):
    #The color of outside Koch spiral
     t.color("black", "cyan") 
     t.begin_fill()
    #draw the outside Koch spiral
     for i in range(6):
         Koch(t,length,minilength)
         t.rt(120)
         Koch(t,length,minilength)
         t.lt(60)
     t.end_fill()
    #The color of inside Koch spiral
     t.color("black", "white") 
     t.begin_fill()
    #draw the inside Koch spiral
     for i in range(6):
         Koch(t,-length,minilength)
         t.lt(60)
     t.end_fill()
#      t.hideturtle()

#      t.penup()
#      t.fd(-200)
#      t.pendown()
#      time.sleep(1)
#      t.color("black")
#      t.write("look! everything was futile, a chasing after the wind.",font = ("Times", 18, "bold")) 
#      t.penup()
#      t.lt(90)
#      t.fd(20)
#      t.pendown()
#      t.color("red")
#      t.write("ECCLESIASTES 1:14",font = ("Times", 18, "bold")) 
#      t.hideturtle()

# Koch(Fred,200,20) 
Fred.penup()
Fred.lt(90)
Fred.fd(150)
Fred.lt(90)
Fred.backward(100)
Fred.rt(180)
Fred.pendown()

# v
if __name__=='__main__':
    from time import clock
    start=clock()
#     for i in range(6):
#         snowflake(Fred, 200, 5)
#         Fred.lt(60)
#     slowsixflake(Fred,200, 5)
    fastsixflake(Fred, 200, 5)
    finish=clock()
    print (finish-start)

# 葵花sunflower
# def sunflower(t,times,length,angle):
#     t.hideturtle()
#     t.color("purple")
#     for i in range(times):
#         t.forward(length)  
#         t.right(angle)  # 右转角度
#     t.color("red")
#     t.write("SunFlower")
#     t.hideturtle()
#     
# sunflower(Fred, 40, 200, 110)
# 作者：Python玩法收集者
# 链接：https://www.zhihu.com/question/26708591/answer/211758902

# def sunflower2(t,times,length,angle):
#     t.color("red", "yellow") 
#     t.begin_fill()
#     for _ in range(times):
#       t.forward(length)
#       t.left(angle)
#     t.end_fill()
# 
# sunflower2(Fred, 40, 200, 110)
# turtle.mainloop()

#6边形和6角星各种组合，随着i和j的不同range个数而改变
#      for i in range(6):
#          t.fd(length/3)
#          t.lt(120)
#          t.fd(length/3)
#          t.rt(60)     
#      for j in range(10):
#         t.fd(length/3)
#         t.rt(60)
#      Koch(t,length)