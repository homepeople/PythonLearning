#coding=utf-8
#Exercise6.2
def first(word):
     return word[0]
def last(word):
     return word[-1]
def middle(word):
     return word[1:-1]
# print(first('2113'))
# print(last('2113'))
# print(middle("2113"))

# def is_palindrome(word):#recursion
#      global result
#      if word!='' and len(word)>1:
#          if  first(word)!=last(word): 
#              return False
#          elif is_palindrome(middle(word))!=False:
#              return True
#          else:
#              return False
result=True
def is_palindrome(word):#recursion
     global result
     if word!='' and len(word)>1 and result==True:
         if  first(word)==last(word)and is_palindrome(middle(word))!=False: 
             result=True
         else:
             result=False
     return result
         
             
def is_pal(word):#for
    times=len(word)//2
    for i in range(times):
         if  first(word)!=last(word):
              return False
         else:
             if len(word)>1:
                  word=middle(word)
    return True
#print(is_pal('12345678987654321'))
print(is_palindrome('12345678987654322'))