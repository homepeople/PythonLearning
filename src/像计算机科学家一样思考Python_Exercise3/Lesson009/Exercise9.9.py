#coding=utf-8
#Exercise9.9
def nlen(word,n): 
     if len(word)<n:
         word='0' + word
     else:
         return word
     return nlen(word,n)
 
def is_palindrome(word1,word2):
     word1=nlen(word1,2)
     word2=nlen(word2,2)
     if word1==word2[::-1]:
         return True
     else:
         return False
     
def palindrome_age(diff):
     mage=15
     t=0
     while mage <100:
         bage=mage-diff
         if is_palindrome(str(mage),str(bage)):
             t=t+1
             if t==6:
                 bage6=bage
             if t>7:
                 print(bage6)
                 return True  
         mage +=1
     return False
 
def diffs():
     diff=10
     while diff <70:
         if palindrome_age(diff):
             print(diff)
         diff += 1
# diffs()
palindrome_age(18)
