#coding=utf-8
#Exercise7.1
import math

def newtonmothod(a,x):
    epsilon=0.00000000000000000000000000000000000000000000000000000001

    while True: 
#         print(x)
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
            break
        x=y
    return y
#     x="%.30f" % x  
#     math.sqrt(x)
#     x="%.30f" % x
#     print(x)

def print_sqrt(x):
    print('a     mysqrt(a)   math.sqrt(a)     diff')
    print('--    --------   ------------     -----')
    a = 1
    while a <= 9:
        a=a+1
        diff=math.sqrt(a)-newtonmothod(a, x)
        print(a,newtonmothod(a, x),math.sqrt(a),diff)
        
print_sqrt(1)
