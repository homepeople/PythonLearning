# -*- coding: UTF-8 -*-
def get_Prime_Fast(MinNum,MaxNum):#get all Prime in Range(MinNum,MaxNum),print out
    try:
        MinNum = int(float(MinNum))
        MaxNum = int(float(MaxNum))
    except  ValueError:
        print('请输入大于2的整数')
      
    if MinNum <2 or MaxNum <2:
       print("MinNum and MaxNum must not less than 2")
       return False
  
    if MinNum > MaxNum:
        MinNum,MaxNum=MaxNum,MinNum  
        
    n=1    
    for i in range(MinNum,MaxNum):
       if is_Prime(i):
           print(n,i)
           n += 1
   
def is_Prime(num):#num is a Prime or not,return boolean
    if num==2 or num ==5:# 2 and 5 are Prime
        return True 
    if is_even(num) or num%10 ==5 :#Prime Not Even and last num Not 5
        return False 
    
    global mag
    for i in range(3,num,2):#already remove even,so start at 3 step 2
        if(num%i == 0):
            return False
#          if speedUp_Prime(i,num):
#              return True
#          if i > num //mag:#speedUp_Prime is slower then this,they are same but why this is faster?
#              if find_value_inDict(num,gDict)  == False:
#                  return True   
    else:#After calculate all num
        return True
    

def speedUp_Prime(i,num):#Shall we have to divide all num?
        #num divide 3 to speed up除去1个数，且不等于所有小于这个数的所有质数的两两乘积,由于已经除去了2，和3，还有5，因此质数可以从7开始
    if i > num //mag:
            #//10 !=49,//14 !=121,//16 !=77 !=143 !=169,//19 !=91,//21 !=289 !=187 !=221,//22 !=323 !=361,//23 !=247 
#              if num !=49 and num !=121 and num!=77 and num!=143 and num!=169 and num!=91 and num !=289 and num!=187 and num!=221 and num!=323 and num!= 361 and num!=247:
        if find_value_inDict(num,gDict) == False:
            return True
       
def is_even(num):#num is Even or not,return boolean
    if num % 2 ==0:
        return True
    else:
        return False
      
def get_Prime_Slow(MinNum,MaxNum):#get all Prime in Range(MinNum,MaxNum),return list of prime
 
    primeList=[]
    for i in range(MinNum,MaxNum):
       for j in range(2,i):
          if(i % j == 0):
             break
       else:
          primeList.append(i)
    return primeList    

def get_Primes_product(PrimeList):#递归得质数乘法表，4次递归太慢了，因此3次幂最理想，480倍的加速，嘎嘎
    global gPrimeLst
    if PrimeList==[]:
        return
    get_Primes_product(PrimeList[:-1])
    for i in PrimeList:
        gPrimeLst.append(i*PrimeList[-1])   
        for j in PrimeList:
            gPrimeLst.append(j*i*PrimeList[-1])
#              for x in PrimeList:
#                  gPrimeLst.append(x*j*i*PrimeList[-1])
                
def find_value_inDict(value,dicts): 

    if value in dicts:
        return True
    else:
        return False
      
if __name__=='__main__':
    import time
    start = time.time()
#      get_Prime_Slow(2,10000)
    mag=480#如果mag=69 则343,即7**3会被漏掉，mag=481,则会漏掉2401，7**4,规律为mag为7的n次幂的5分之一，大于5分支1则会出现下1次幂的数，4次幂的递归太慢了，因此3次幂最理想，480倍的加速，嘎嘎
    PrimeList=get_Prime_Slow(7,mag)
    gPrimeLst=[]
    gDict={}
    get_Primes_product(PrimeList)
    gDict = dict(zip(gPrimeLst,gPrimeLst))
    
    get_Prime_Fast(2,1000000) 

    end = time.time()
    print (end-start)
    