#coding=utf-8
#Exercise9.4 9.5
from getpass import fallback_getpass
def uses_only(word,str):
     for i in word:
         if i not in str:
             return False
     return True
 
def uses_all(word,str):
     for sinchar in str[0:len(str)]:
         if sinchar not in word:
             return False
     return True

def abc_words():
     fin=open('D:\编程\Python\Mobywords.txt')
     for line in fin:
         word=line.strip() 
         if uses_all(word,'aeiou'):
             print(word)
             
# abc_words()

