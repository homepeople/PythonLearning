#coding=utf-8
#像计算机科学家一样思考Python-Exercise3.3
def print_row(x,y,fmark,smark):#画出一行
    for tx in range(x):
        if tx < x-1:
             print(fmark,end=' ')#不换行
             for ty in range(y):
                print(smark,end=' ')
        else:
             print(fmark,end='\r')#最后一个换行
       
def print_box(nplus,nRow,nCol):#nplus加号个数，nRow横线个数，nCol纵线个数
    for i in range(nplus):
        print_row(nplus,nRow,'+','-')
        if i < nplus-1:#放弃最后一次循环
            for j in range(nCol):
                print_row(nplus,nRow,'|',' ')
                 
print_box(4,5,5)