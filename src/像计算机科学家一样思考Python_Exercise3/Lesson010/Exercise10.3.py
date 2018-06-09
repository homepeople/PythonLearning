#coding=utf-8
#Exercise10.3
def middle(list):
    del list[0]
    del list[len(list)-1]
    print(list)

list=[1,2,3,4]
middle(list)