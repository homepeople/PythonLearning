#coding=utf-8
#Exercise5.2
def check_fermat(a,b,c,n):
    a=int(a)
    b=int(b)
    c=int(c)
    n=int(n)
    if n <= 2:
        result='n need bigger than 2'
    else:
        if a**n+b**n==c**n :
             result='Fermat was wrong!'
        else:
            result='Fermat are correct'
    print(result)
    
check_fermat(3.1, 4.4, 5, 3.2)