#coding=utf-8
#Exercise5.3
def is_triangle(a,b,c):
     if a>b+c:
        r = 'No'
     else:
        r = 'Yes'
     print(r)
    
def is_bigger(a,b,c):
     if a>=b>=c:
         return is_triangle(a,b,c)
     else:
         if b>a:
             is_bigger(b,a,c)    
         elif c>b:#如果是if则出现2个yes或no，调用2次is_bigger
             is_bigger(a,c,b)
         
is_bigger(1,3,3)