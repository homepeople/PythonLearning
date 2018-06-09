#coding=utf-8
#Exercise6.2
import time
def ack(m,n):
     if m==0:
         return n+1
     elif m>0 and n==0:
         return ack(m-1,1)
     elif m>0 and n>0:
         result=ack(m-1,ack(m,n-1))
#          print(m,n,result)
         return result
if __name__=='__main__':    
    start_time = time.time()
#     for i in range(10):
    print(ack(3,6))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'seconds')     
