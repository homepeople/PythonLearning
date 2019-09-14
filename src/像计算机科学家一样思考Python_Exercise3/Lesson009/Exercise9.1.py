#coding=utf-8
#Exercise9.1
#需求：比较2个相似文件的每一行，如果不同就把两句话都打印出来
#注意：2个源文件格式不100%相似，因此需要先更改格式为每句话1行，然后逐行进行对比。
pOld = 'E:\Programming\Bible\创世纪bi12.txt'#文本存放的路径
pNew = 'E:\Programming\Bible\创世纪nwt新.txt'
PResult='E:\Programming\Bible\创世纪比较结果.txt'
import re
#比较2个类似文件，并把不同处输出到第三个新文件内
def compare2files(path1,path2,resultpath):
    #file1 = open('E:\Programming\Bible\创世纪nwt.txt','r', encoding='UTF-8')#使用这种方法只能得到第一行的数据
    #file2 = open('E:\Programming\Bible\创世纪bi12.txt','r', encoding='UTF-8')
    line1 = 0
    dlines = 0
    Tmp_list=[]
    for value1 in open(path1,'r', encoding='utf-8').readlines():
        #word1 = str(value1).split()
        line2 = 0
        line1 = line1 + 1

        for value2 in open(path2,'r', encoding='utf-8').readlines():
            line2 = line2 + 1 
            #word2 = str(value2).split()
            #str1 =removePunctuation("".join(word1))
            #str2 =removePunctuation("".join(word2))
            str2 =removePunctuation(str(value2))
            str1 =removePunctuation(str(value1))
            if line1 == line2 and str1 != str2:
               print(str1)
               print(str2)
               #Tmp_list.append(str1)
               #Tmp_list.append(str2)
               dlines+=1
    print(dlines)
    #Tmp_list.append('本章共'+str(dlines)+'节经文不同')
    #writeLinF(Tmp_list,resultpath)


#更改文件每行开头为数字（因为经文每行开头都有数字，但是需要和句子中的数字区分开来）
#注意几种情况，1开头不为数字，2数字在句子内（一般在量词），3超过个位数的数字如何处理
#思路：1每节经文开头有数字，但是不一定是在句号后，因此不能通过句号判断是否是开头。
#      2因为数字一般出现在量词前，因此可以通过量词来屏蔽不需要的数字。
#      3因为经文一般不会超过3位数，因此可以根据情况进行过滤。
def changeStyle(pathOld,pathNew):
    tmpStr = ''#空字符（中间不加空格）
    banlist=["人","岁","天","年","肘尺","日","夜","个","头","只","次","匹","颗","块"]
    for value1 in open(pathOld,'r', encoding='UTF-8').readlines():#打开文件夹，并把文件变为String
        word1 = str(value1).replace(' ','')
        word1 = str(word1).replace('\n','')
        tmpStr += word1
    #tmpStr = ''.join(tmpStr)
    #print(tmpStr)
    positionN = 0
    positionL = 0
    Tmp_list = []
    for x in tmpStr:#有数字开头的分行，然后打印出来

        if x.isdigit() and positionN > 0 :  #如果用isnumeric那么中文的数字也算进去了
           
           if  tmpStr[positionN-1].isdigit() == False:#只有1位数和2位数才能分行 
              if  tmpStr[positionN+2].isdigit() == False:#3位数不分行
                  if any(tmpStr[positionN+1] in s for s in banlist) != True and any(tmpStr[positionN+2] in s for s in banlist) != True:#有单位的数字不排头
                       Tmp_list.append(tmpStr[positionL:positionN])
                       positionL = positionN
        positionN += 1
    writeLinF(Tmp_list,pathNew)
    #for y in Tmp_list:
    #    print(y)

#去除汉字，字母，数字以外的所有符号
def removePunctuation(text):
   
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",text)

    return sub_str
def test():
    tmpStr="哈哈，你好，世界，12"
    positionN = 0
    positionL = 0
    Tmp_list = []

    for x in tmpStr:
       
        if x.isdigit()==True:  
           
           if  tmpStr[positionN-1].isdigit() == False:#只有1位数和2位数才能分行 
               Tmp_list.append(tmpStr[positionL:positionN])
               positionL = positionN
               #print(x)
        positionN += 1
    for y in Tmp_list:
        print(y)    

#将list写入文件，并分行
def writeLinF(lists,fileName):

       fp = open(fileName,'w', encoding='UTF-8')
       for line in lists:
           fp.write(line+'\n')
  
       fp.close()

if __name__ == '__main__':
     compare2files(pOld,pNew,PResult)
     #changeStyle(pOld,pOld)
     #test()
     #text = "123我123456abcdefgABCVDFF？/ ，。,.:;:''';'''[]{}()（）《》"
     #print(removePunctuation(text))