#coding=utf-8
#Exercise9.6
import string
       
def is_abecedarian(word):
     letter_list = string.ascii_lowercase
     i=0
     count=0
     while i<len(word):          
         if word[i] == letter_list[i+count]:
             count=count
         elif i>0 and word[i] == letter_list[i+count-1]:
             count=count+1
         else:
            return False
         i += 1 
     return True
def abc_words():
     fin=open('D:\编程\Python\Mobywords.txt')
     for line in fin:
         word=line.strip() 
         if is_abecedarian(word):
             print(word)
abc_words()