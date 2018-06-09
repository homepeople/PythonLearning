#coding=utf-8
#Exercise10.1
tryalist = ['html', 'js', 'css', 'python']
      # 方法1
print('遍历列表方法1：值历遍')
for i in tryalist:
    print ("序号：%s   值：%s" % (tryalist.index(i) + 1, i))
 
print('\n遍历列表方法2：序号历遍')
     # 方法2
for i in range(len(tryalist)):
    print ("序号：%s   值：%s" % (i + 1, tryalist[i]))

     # 方法3
print('\n遍历列表方法3：双历遍，枚举')
for i, val in enumerate(tryalist):
    print ("序号：%s   值：%s" % (i + 1, val))
 
     # 方法3
print ('\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：')
for i, val in enumerate(tryalist, 2):
     print ("序号：%s   值：%s" % (i + 1, val)) 


def num_sum(alist):#sum list within only number, return the total value
    sum=0
    for num in alist:
        sum += num
    return sum

def nested_sum(alist):#sum list within only nested list, return the total value
    res=[]
    for i in alist:
        res.extend(i)
    sum =num_sum(res)
    return sum

def add_all(alist):#sum list combine within number and list, return the total value
     sum=0
     for i in range(len(alist)):
         if type(alist[i])==list:
             sum +=num_sum(alist[i])
         else:
             sum +=alist[i]
     return sum

# NumberOnly=[1,2,3,4]
# print(num_sum(NumberOnly))

# ListOnly=[[1,2],[3,4],[9,10]]
# print(nested_sum(ListOnly))

NumberWithList=[1,3,2,[7,8],[],[0]]
result='Sum '+str(NumberWithList)+' to get '+str(add_all(NumberWithList))
print('\n'+result)