#coding=utf-8
#Exercise9.8
import string
def is_palindrome(word):
     if word==word[::-1]:
         return True
     else:
         return False
def sixlen(word):
     if len(word)<6:
         word='0' + word
     else:
         return word
     return sixlen(word)
# print(sixlen('999'))  
     
def CarTalkPalindrome():
    orgnum=199999
    for x in range(orgnum,0,-1):
         step1=sixlen(str(x))[2:6]
         if is_palindrome(step1):
             step2=sixlen(str(x+1))[1:6]
             if is_palindrome(step2):
                 step3=sixlen(str(x+2))[1:5]
                 if is_palindrome(step3):
                     step4=sixlen(str(x+3))[0:6]
                     if is_palindrome(step4):
                         print(x)
                     
CarTalkPalindrome()   