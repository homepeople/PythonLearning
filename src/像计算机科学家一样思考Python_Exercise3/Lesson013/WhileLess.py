#coding=UTF-8
#Max and minimum factor or prime
#最大公约数或是素数(质数)

def showMaxFactor(num): 
    for eachNum in range(2, num): 
        count = eachNum // 2 
        while count > 1: 
            if (eachNum % count == 0): #if not(eachNum % count)
                print ('Max factor of',eachNum,'is', count)
                break
            count = count - 1
        else:
            print (eachNum, 'is prime' )

# def showMaxFactor(num): #while slower then for each
#     eachNum = 2
#     while(eachNum <= num):
#         count = eachNum // 2 
#         while count > 1: 
#             if (eachNum % count == 0): #if not(eachNum % count)
#                 print ('Max factor of',eachNum,'is', count)
#                 break 
#             count = count - 1  
#         else: 
#             print (eachNum, 'is prime' )  
#         eachNum = eachNum + 1  
    
def minimumPrintPrime(num):
    for eachNum in range(2, num+1):
        count = 2
        while(count <= (eachNum/count)):
            if (eachNum % count== 0) : #if (eachNum % count== 0)    
                print ('minimum factor of',eachNum,'is', count)
                break
            count = count + 1
        else: 
            print (eachNum, 'is prime' )# 是素数(质数)its prime

# def minimumPrintPrime(num):
#     eachNum = 2
#     while(eachNum <= num):
#         count = 2
#         while(count <= (eachNum/count)):
#             if (eachNum % count== 0) : #if (eachNum % count== 0)    
#                 print ('minimum factor of',eachNum,'is', count)
#                 break
#             count = count + 1
#         else: 
#             print (eachNum, 'is prime' )# 是素数(质数)its prime     
#         eachNum = eachNum + 1

if __name__ == '__main__':
    from time import clock
    start=clock()
    minimumPrintPrime(3000000)#faster then showmaxfactor
#     showMaxFactor(100) 
   
    finish=clock()
    print (finish-start)

   
#     start=clock()
# #     for eachNum in range(2, 501): 
#     finish=clock()
#     print (finish-start)