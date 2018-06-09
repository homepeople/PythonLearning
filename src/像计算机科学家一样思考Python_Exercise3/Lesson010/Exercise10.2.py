#coding=utf-8
#Exercise10.2
def cumsum(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
        list[i]=sum
    return list

t=[1,2,3,4,5,6]
print(cumsum(t))     