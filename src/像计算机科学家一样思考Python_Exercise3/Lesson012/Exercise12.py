#coding=utf-8
#Exercise12
# def fun_args(arg, *args):  
#     print ("arg:", arg) 
#     for val in args:  
#         print ("another arg:", val)  
#    
# args = [[2,3,4,5],[6,7], "my", 4.5]  
# #fun_args(1, args)  #调用方式1，常见的方式  
# fun_args(1, *args) #调用方式2，明示args是多参数方式  
# fun_args(1, [2,3,4,5],[6,7], "my", 4.5) #调用方式3  

#Input any tuple and sum all of them,all the object need be the same type in the tuple
def sumall(typeofarg,*args): #Have to put typeofarg in front of *args，else it would be a tuple
    sumall=typeofarg         #make sure the type, the type need to be same in a tuple 
    for i in args:
        sumall=i+sumall
    return sumall
   
print(sumall(1,2,3))
print(sumall('c','b','a','d'))

# def EvenorOdd(*args):#separate Even and Odd from a Tuple
#     args=list(tuple(args))#Transform Tuple to List
def EvenorOdd(args):   
    even=[]
    odd=[]
    while len(args)>0:
        number=args.pop(0)#without 0 its from end to begin,else its oppsite
        if number %2 ==0:
            even.append(number)
        else:
            odd.append(number)
    print('Even =',even,'Odd =', odd)
    
# EvenorOdd(1,2,3,4)
EvenorOdd([1,2,3,4])
# def has_match(t1 , t2 ) :
#     for x , y in zip (t1 , t2) :
#         print(x,y)
#     for pair in zip(t1,t2):
#         print(pair)
# t1= (0,1,2)
# t2= (2,1,0)
# has_match(t1, t2)
# print(t1 == t2)

# directory={}
# last='Fred'
# first='Zeng'
# number=15972973836
# directory[last,first]=number
# for (last, first) in directory:
#      print(last,first,directory[last,first])
      
# for index,element in enumerate('abc'):
#    print(index,element) 
# d={'a':0,'c':2,'b':1}
# t=d.items()
# print(t)

# for key,value in d.items():
#     print(key,value)
# d=dict(zip(t,range(3)))
# print(d)
# t=[('a',0),('c',2),('b',1)]
# d=dict(t)
# print(d)

