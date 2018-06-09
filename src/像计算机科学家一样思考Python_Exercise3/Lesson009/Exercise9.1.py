#coding=utf-8
#Exercise9.1
def openfile():
     fin=open('D:\编程\Python\Mobywords.txt')
     fin.readline()
     for line in fin:
         word=line.strip()
         if len(word)>20:
             print(word)

openfile()