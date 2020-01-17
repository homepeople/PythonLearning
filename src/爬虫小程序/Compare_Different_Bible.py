#coding=UTF-8
import urllib.request
from bs4 import BeautifulSoup
import re
import time

# import sys
# sys.path.insert(0,'../像计算机科学家一样思考Python_Exercise3/Lesson009')
# import Exercise9_1
version1='(nwtCHS)'
version2='(bi12CHS)'
version3='(sbi1CHS)'
version4='(nwtE)'
def printHtml(url,codeType):#这个方法输入url地址和code类型，则返回Html
    res=urllib.request.urlopen(url)
    htmlBytes=res.read()
    result=htmlBytes.decode(codeType)
#     print(htmlBytes.decode(codeType))
    return result

def arrange_Line_FirstNum(tmpStr,url):    #根据每句开头数字分行
    positionN = 0  #N是Next，切片下一次的开始位置
    positionL = 0  #L是Last，切片上一次的结束位置
    Tmp_list = []
    chaNum = 0
    secNum = 0
    lastSec='0'
    tmpStr = tmpStr.replace('\n','').replace('+','').replace('*','')
    for cha in tmpStr:#有数字开头的分行
        if cha.isdigit() and positionN > 0 :                  #如果用isnumeric那么中文的数字也算进去了
            #左边不是数字和字符的标点符号,开始有章节题目，章节没有标点，可能会存在标点后面接数字且数字和下一节或下一章相等的bug
            if  re.match(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])",tmpStr[positionN-1]) != None or chaNum==0 :    
                chaNum=cut_out('/','#study=discover',url) #Get chapter string from url
                digitNum = digitNumber(tmpStr[positionN:positionN+3])   #没有4位数以上的章节,因此只判断4位数 
                
                if digitNum != 4:                               #没有4位数及以上的章节   
                    aheadstr = tmpStr[positionN:positionN+digitNum]#句头数字
                    
                    if aheadstr ==str(secNum+1) or (aheadstr == chaNum and secNum == 0):      #句头数字等于节数或章数
                        Tmp_list.append(tmpStr[positionL:positionN])
                        positionL = positionN
                        
                    lastSec=secNum     
                    secNum += 1
                               
        positionN += 1
 
    Tmp_list.append(tmpStr[positionL:positionN])#加入最后一行数据
    return Tmp_list

def digitNumber(tmpStr):#输入字符串，返回靠左连续数字的位数
    for digitNum in range(len(tmpStr),0,-1):
        tmpStr=tmpStr[0:digitNum]
        if tmpStr.isdigit():
            return digitNum
        
def cut_out(a,b,string):#find the value between a and b in the string
    result = re.findall(".*%s(.*)%s.*"%(a,b),string)
    for i in result:
       return i
   
def compareLists(list1,*listX):
    for i in range(len(list1)):
        if listX != None:
            for x in range(len(listX)):
                tmpList = listX[x]

def getVersionName(url):
    VersionName=re.findall()
        
if __name__ == '__main__':
#input url where the book and the  chapter should be the same  
    url1='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/nwt/66/2#study=discover'
    url2='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/bi12/66/2#study=discover'
    url3='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/sbi1/66/2#study=discover'
    url4='https://wol.jw.org/en/wol/b/r1/lp-e/nwt/66/2#study=discover'
#     novel=printHtml(target, 'gbk')
    htmls1=printHtml(url1, 'UTF-8')
    htmls2=printHtml(url2, 'UTF-8')
    htmls3=printHtml(url3, 'UTF-8')
    htmls4=printHtml(url4, 'UTF-8')
#     bf = BeautifulSoup(novel)
    bf1 = BeautifulSoup(htmls1,"html.parser")
    bf2 = BeautifulSoup(htmls2,"html.parser")
    bf3 = BeautifulSoup(htmls3,"html.parser")
    bf4 = BeautifulSoup(htmls4,"html.parser")
# #     texts = bf.find_all('div', class_="showtxt") 
    texts1 = bf1.find_all('div', id="article") 
    texts2 = bf2.find_all('div', id="article") 
    texts3 = bf3.find_all('div', id="article") 
    texts4 = bf4.find_all('div', id="article") 
# #     print(texts[0].text.replace('\xa0'*8,'\n\n'))
    list1=arrange_Line_FirstNum(texts1[0].text,url1)
    list2=arrange_Line_FirstNum(texts2[0].text,url2)
    list3=arrange_Line_FirstNum(texts3[0].text,url3)
    list4=arrange_Line_FirstNum(texts4[0].text,url4)
    
    for i in range(len(list1)):
        if list1[i] != list2[i] and list1[i] != list3[i] and list2[i] != list3[i]:
            
            print(list1[i]+version1)
            print(list2[i]+version2)
            print(list3[i]+version3)
  
        elif list1[i] == list2[i] and list1[i] == list3[i]:
            
            print(list3[i]+version1+version2+version3)
             
        elif list1[i] == list2[i] and list1[i] != list3[i]:
            
            print(list1[i]+version1+version2)
            print(list3[i]+version3)
          
        elif list2[i] == list3[i] and list1[i] != list2[i]:
            
            print(list1[i]+version1)
            print(list2[i]+version2+version3)
            
        print(list4[i]+version4)
        print('') 
            
            