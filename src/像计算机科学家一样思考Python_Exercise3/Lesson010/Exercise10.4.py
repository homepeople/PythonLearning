#coding=utf-8
#Exercise10.4
def chop(list):
    del list[0]
    del list[len(list)-1]
    print(list)
    return None

list=[1,2,3,4]
chop(list)