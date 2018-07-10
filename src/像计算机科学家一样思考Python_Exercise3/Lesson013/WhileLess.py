#coding=UTF-8
#largest and minimum factor or prime
#最大公约数或是素数(质数)

def showMaxFactor(num): 
    for eachNum in range(2, num): 
        count = eachNum // 2 
        while count > 1: 
            if (eachNum % count == 0): 
                print ('largest factor of',eachNum,'is', count)
                break 
            count = count - 1  
        else: 
            print (eachNum, 'is prime' )
        
def minimumPrintPrime(num):
    i = 2
    while(i < num):
        j = 2
        while(j <= (i/j)):
            if not(i%j): 
                print ('minimum factor of',i,'is', j)
                break
            j = j + 1
        else: 
            print (i, 'is prime' ), "是素数(质数)its prime"
        i = i + 1
        
if __name__ == '__main__':
    from time import clock
    start=clock()
#     minimumPrintPrime(10000)'faster then showmaxfactor
    showMaxFactor(10000) 
    finish=clock()
    print (finish-start)

   
#     start=clock()
# #     for eachNum in range(2, 501): 
#    
#         
#     finish=clock()
#     print (finish-start)