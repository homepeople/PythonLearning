#coding=utf-8
#Exercise5.5
import turtle
Fred=turtle.Turtle()
#draw a branch
def draw(t,length,n):
    if n==0:
        return
    angle=50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)
    
if __name__ == '__main__':
    draw(Fred,2,7)
    turtle.mainloop()
