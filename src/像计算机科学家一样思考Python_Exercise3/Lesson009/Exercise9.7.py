#coding=utf-8
#Exercise9.7
# from __future__ import print_function, division
def is_tripdouble(word):
     i = 0
     count = 0
     while i < len(word)-1:
         if word[i] == word[i+1]:
             count = count + 1
             if count == 3:
                 return True
             i = i + 2
         else:
             count = 0
             i = i + 1
     return False

def find_tripdouble():
     fin=open('D:\编程\Python\Mobywords.txt')
     for line in fin:
         word= line.strip()
         if is_tripdouble(word):
             print(word)

find_tripdouble()
