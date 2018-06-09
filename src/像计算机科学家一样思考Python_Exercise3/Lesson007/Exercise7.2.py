#coding=utf-8
#Exercise7.1
# import math
# import sys  
# print (sys.version) 

def eval_loop():
    while True:
        x = input('> ')
        if x== 'done':
            break
        result = eval(x)
        print (result)
# 
eval_loop()#becareful the parenthesis