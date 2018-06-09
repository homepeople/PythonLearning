#coding=utf-8
#Exercise9.3
import string
def avoids(word,banstr):
     if  banstr not in word:
         return True
     
def manywordsisnotbaned(banstr):
     m=0
     n=0
     fin=open('D:\编程\Python\Mobywords.txt')
     fin.readline()
     for line in fin:
         word=line.strip()
         if avoids(word, banstr):
             n=n+1
     
#      print(n)
     return n
def inputbanletter():
     banstr=input('请输入需要在单词内禁止的字符:')
     manywordsisnotbaned(banstr)
def returnsmaller(m1,m2):    
     if m1<m2:
         return m1
def find5lessletter():
     m=0
     for banstr in string.ascii_lowercase:
         n=manywordsisnotbaned(banstr)
         if m<1:
             m1=n
             b1=banstr
         elif m<2:
             m2=n
             b2=banstr
         elif m<3:
             m3=n
             b3=banstr
         elif m<4:
             m4=n
             b4=banstr
         elif m<5:
             m5=n
             b5=banstr
         else:
             if n<m1:#有问题，因为不知道最后一个是否为已知5个数里面的最大，这样挤下去的可能是中间数,需要排序
                 m1=n
                 b1=banstr
             elif n<m2:
                 m2=n
                 b2=banstr
             elif n<m3:
                 m3=n
                 b3=banstr
             elif n<m4:
                 m4=n
                 b4=banstr
             elif n<m5:
                 m5=n
                 b5=banstr       
         m=m+1
     print(b1,m1,b2,m2,b3,m3,b4,m4,b5,m5)
# inputbanletter()
find5lessletter()
