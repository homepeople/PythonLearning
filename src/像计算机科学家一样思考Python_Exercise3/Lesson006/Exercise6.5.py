#coding=utf-8
#Exercise6.2
def is_divisible(a,b):
    if a%b==0:
        return True
    else:
        return False
def gcd(a,b):
    if b==0:
        return a
    if a==0:
        return b
    r = a % b 
    if  gcd(b,r) - gcd(a,b)==0:
        return r
    else:
        return gcd(a-1,b)
print(gcd(2,4))