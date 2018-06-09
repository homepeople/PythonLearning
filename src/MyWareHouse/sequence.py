#coding=utf-8
#sequence
'''
1. 列表
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字- 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
列表的一般用法：
'''
list1 = ['frui','male',1989,'python',[2016,2017],'c'] #list内元素的数据类型可以不同,也可以是另外一个list
list2 = ['']
print (list1)

#使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：
print (list1[:])
print (list1[0],list1[1])
print (list1[-1],list1[-2])
print (list1[0:3]) #切片,此操作顾头不顾尾
print (list1[:3])
print (list1[-3:]) #切片，从后向前数索引，也只能从左往右切片，同样是顾头不顾尾。（这样会无法取到最后一个元素，思考怎么办？）
print (list1[0:-1:2]) #按步长切片
print (list1[::2]) #按步长切片

list1.append("linux") #在列表末尾追加元素
list1.insert(1,"linux") #直接把元素插入的指定位置
list1[0] = "jay" #（改）直接替换某个位置元素

#delete
list1.pop() #删除list末尾的元素
list1.pop(1) #删除指定位置的元素
del list1[0]
list1.remove("python") #此种方法和前两种的区别是什么？

print (list1)
print (list1.index(1989)) #查找已知元素的索引
print (list1[list1.index(1989)])

print (list1.count(1989)) #打印某元素在列表中的数量

list1.reverse() #反转整个列表
# list1.sort() #排序 按ASCII码顺序排序,若元素中有list类型，则无法排序，为什么？

list2 = [1,2,3,4]
list1.extend(list2) #列表合并
print (list1)
# list1.clear() #清除整个列表
del list2 #删除整个变量
#列表的深浅copy
#浅拷贝只能拷贝最外层，修改内层则原列表和新列表都会变化。
#深拷贝是指将原列表完全克隆一份新的。
import copy
list1 = ['frui','male',1989,'python',[2016,2017],'c'] 
list2 = list1.copy() #浅copy
print(id(list1))
print(id(list2))
list3 = copy.copy(list1) #浅copy，同list1.copy()效果相同
list4 = copy.deepcopy(list1) #深copy，会和list1占用同样大小的内存空间
print(id(list3))
print(id(list4))


list1[0] = '自由'
list1[4][0] = 2015
print (list1,'\n',list2,'\n',list3,'\n',list4)
#列表的循环：逐个打印列表元素
list1 = ['frui','male',1989,'python',[2016,2017],'c'] 
for i in list1:
    print (i)
'''    
2. 元组
元组也是存一组数据，只是一旦创建，便不能修改，所以又叫只读列表。元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''
tup1 = (1,2,3,4,5)
tup2 = ('frui', 27)
tup3 = "a", "b", "c", "d";
tup4 = () #创建空元组
# 元组中只包含一个元素时，需要在元素后面添加逗号

tuple5 = (50,) #元组中只包含一个元素时，需要在元素后面添加逗号
tuple6 = (50)
#如果不加逗号，则定义的不是tuple，是50这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算。
# 元组只有两个方法：count和index
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

'''
3. 字典
3.1 字典的使用
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值对()用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
'''
# d = {key1 : value1, key2 : value2 }
# 键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

info = {
    'stu1':"Xiao Ming",
    'stu2':"Xiao Liang",
    'stu3':"Xiao Hong",
    'stu4':"Xiao Rui",
}
print (info)
#修改
info['stu2'] = "Xiao Hu" 
#增加
info['stu5'] = "Xiao Fang"

#删除
info.pop('stu2')
del info['stu1']
info.popitem() #随机删一个
print (info)
info.clear() #清空字典所有条目

#查找
print ('stu2' in info) #判断是否存在，存在则返回True，否则返回False
# print (info['stu1']) #如果一个key不存在，就报错，get不会，不存在只返回None

#dict.get(key, default=None)
#返回指定键的值，如果值不在字典中返回default值
#比较安全的查找方法
print (info.get('stu6')) 


#其他
print (info.values()) #打印所有的值(即除了key)
print (info.keys()) #打印所有的key
print (info.items()) #把字典转化为列表


# dict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
info.setdefault ('class3',{'Xiao Rui', 15})
print (info)
info.setdefault ('class1',{'Xiao Hong', 16})
print (info)

#循环打印
for i in info:
    print (i,info[i])

for k,v in info.items():
    print (k, v)
#多级字典嵌套及操作
info = {
    'class1':{
        'stu1':["Xiao Ming",16]
    },

    'class2':{
        'stu2':["Xiao Liang",17]
    }
}
info['class1']['stu1'][1] = 18
print (info)
#dict.fromkeys(seq[, val]))
# 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
# eg:
print (dict.fromkeys([6,7,8],'test'))
c = dict.fromkeys([6,7,8],[1,{'name':'frui'}])
c[6][1]['name'] = 'sorui'
print (c)
#update方法
info = {
    'stu1':"Xiao Ming",
    'stu2':"Xiao Liang",
    'stu3':"Xiao Hong",
    'stu4':"Xiao Rui",
}
b = {
    'stu1': "Xiao Dong",
    1:3,
    2:4
}
print (info)
info.update(b)
'''
为什么dict查找速度这么快？
因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。dict就是第二种实现方式。
和list比较，dict有以下几个特点：
无序
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''
'''
4. 集合
集合是一个无序的，不重复的数据组合，它的主要作用如下：

去重，把一个列表变成集合，就自动去重了
关系测试，测试两组数据之前的交集、差集、并集等关系
常用操作
'''
#去重
list1 = [3,2,1,4,5,6,5,4,3,2,1]
print (list1, type(list1))
list1 = set(list1)
print (list1, type(list1))

list2 = set([4,5,6,7,8,9])

#交集
print (list1.intersection(list2))

#并集
print (list1.union(list2))

#差集
print (list1.difference(list2))
print (list2.difference(list1))

#子集、父集
print (list1.issubset(list2))
print (list1.issuperset(list2))

list3 = set([4,5,6])
print (list3.issubset(list2))
print (list2.issuperset(list3))

#对称差集
print (list1.symmetric_difference(list2))

#Return True if two sets have a null intersection
list4 = set([1,2,3])
print (list3.isdisjoint(list4)) 
#交集
print (list1 & list2)
#union
print (list2 | list1)
#difference
print (list1 - list2)
#对称差集
print (list1 ^ list2)
#添加
list1.add(999) #添加一项
print (list1)
list1.update([66,77,88]) #添加多项
print (list1)
print (list1.add(999)) #猜猜打印什么？为什么

#删除
list1.remove(999)
print (list1)

#remove and return arbitrary set element
print (list1.pop()) 

#Remove an element from a set if it is a member.If the element is not a member, do nothing.
print (list1.discard(888)) 