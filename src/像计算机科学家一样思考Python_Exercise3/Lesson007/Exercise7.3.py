#coding=utf-8
#Exercise7.1
import  math
from functools import total_ordering
from sklearn.cluster.mean_shift_ import estimate_bandwidth
def factorial(n):
    if n==0:
        return 1
    else:
        recurse= factorial(n-1)
        result= n*recurse
        return result
    
def estimate_pi():
     total=0
     k=0
     factor =2*math.sqrt(2)/9801
     while True:
          num=factorial(4*k)*(1103+26390*k)
          den=factorial(k)**4*369**(4*k)
          term=factor*num/den
          total += term
          if abs(term)< 1e-15:
             break
          k += 1
     return total

print(estimate_pi()-1/math.pi)