#coding=utf-8
#Exercise5.4
#n为整数且不能小于0，否则递归为死循环
def recurse(n,s):
    if n==0:
        print("s=" + str(s),"n=" + str(n))
    else:
        print("n=" + str(n),"s=" + str(s))
        recurse(n-1, n+s)
        print("s=" + str(s),"n=" + str(n))
        
if __name__ == '__main__':
    recurse(3, 0)
    #recurse(-1, 0)#its wrong,debug it please
