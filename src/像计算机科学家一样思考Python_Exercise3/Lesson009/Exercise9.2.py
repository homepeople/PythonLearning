#coding=utf-8
#Exercise9.2

def has_no_e():
     m=0
     n=0
     fin=open('D:\编程\Python\Mobywords.txt')
     fin.readline()
     for line in fin:
         word=line.strip()
         if "e" not in word:
             print(word)
             n=n+1
         m=m+1
     print(n/m)
     
has_no_e()