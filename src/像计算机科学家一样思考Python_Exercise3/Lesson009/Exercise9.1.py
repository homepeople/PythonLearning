#coding=utf-8
#需求：比较2个相似文件的每一行，如果不同就把两句话都打印出来,比较结果输入到新的文件
#注意：2个源文件格式不100%相似，因此需要先更改格式为每句话1行，每行以章节序号开头，然后才能开始对相同序号的进行对比。
ChapterName='以西结书'
pOld = 'D:/Programming/Bible/bi12/'+ChapterName+'bi12.txt'#老版本圣经存放的路径
pNew = 'D:/Programming/Bible/nwt/'+ChapterName+'nwt.txt'#新版本圣经存放的路径
PResult='D:/Programming/Bible/result/'+ChapterName+'比较结果.txt'#比较结果存放路径
#禁止的量词单位
'''
量词单位前的数字不排头,杜绝量词单位排头的可能性，因为不知道量词具体的数目，因此根据需要增加或减少
问题：有些非量词单位，但是和量词为同一个词开头的情况下就会出现屏蔽错误，比如：箴言12:25人心担忧，郁郁寡欢；听见良言，心里欢喜。
'''
banlist=["弥拿","塔兰特","舍客勒",'银','多',"贺梅珥","季拉",'米','公里',"倍","点","代","张","片","件","辆","套","拃","掌","下","岁","天","年","尺","日","夜","个","十","百","千","万","头","只","次","匹","颗","块","座","欣","罗格","皮姆","伊法","细亚","俄梅珥","罢特","歌珥","罗革","肘尺"]
import sys
import re
'''
比较2个类似文件的相同行，并把不同处输出到第三个新文件内
'''
def compare2files(path1,path2,resultpath):
    
    line1 = 0  #文件1当前行数
    diflines = 0#不同行的总行数
    allLines = 0#总行数
    Tmp_list=[] #临时表
    
    #检查2个文件相同行是否有不同之处
    for value1 in open(path1,'r', encoding='utf-8').readlines():    

        lines  = open(path2,'r', encoding='utf-8').readlines()
        if line1 < len(lines):
            value2=lines[line1]
            line1 += 1   
            str2 =removePunctuation(str(value2))#去掉除数字，字母，汉字以外的所有符号
            str1 =removePunctuation(str(value1))
          
            if str1 != str2:#内容不相同，输出到Tmp_list
                if  str1[:1] != str2[:1]:#第一个字符不相等，则退出程序
                    print('首序列号不同'+str1[:1]+str2[:1])
                    sys.exit(0)
                    
                elif str1[1:2].isdigit() and str2[1:2].isdigit() and str1[1:2] != str2[1:2]:#第二位若都为数字，且不相等，则退出程序
                    print('次序列号不同'+str1[:2]+str2[:2])
                    sys.exit(0)   
                    
                print(str1)
                print(str2)
                Tmp_list.append(str1)
                Tmp_list.append(str2)
                diflines += 1
        
        allLines += 1
        
    print(ChapterName+'共'+str(allLines-1)+'节经文'+',其中'+str(diflines)+'节不同')
    
    Tmp_list.append(ChapterName+'共'+str(allLines-1)+'节经文'+',其中'+str(diflines)+'节不同')
    
    writeLinF(Tmp_list,resultpath)#输出比较结果到文件


#更改文件每行开头为数字（因为经文每行开头都有数字，但是需要和句子中的数字区分开来）
'''
# 注意几种情况，1开头不为数字，2数字在句子内（一般在量词前），3超过个位数的数字如何处理
# 思路：   1每节经文开头有数字，但是不一定是在句号后，因此不能通过句号判断是否是开头。
#      2因为数字一般出现在量词前，因此可以通过量词来屏蔽不需要的数字。
#      3因为经文一般不会超过3位数，因此可以根据情况进行过滤。(除了诗篇)
'''
def changeStyle(pathOld,pathNew):

    tmpStr = ''    #空字符（中间不加空格）
    
    for value1 in open(pathOld,'r', encoding='UTF-8').readlines():#打开文件，去空格和换行，并把文件变为String
        word1 = str(value1).replace(' ','')
        word1 = str(word1).replace('\n','')
        tmpStr += word1
    
    positionN = 0  #N是Next，切片下一次的开始位置
    positionL = 0  #L是Last，切片上一次的结束位置
    Tmp_list = []
    chaNum = 0
    secNum = 0
    lastSec='0'
    for cha in tmpStr:#有数字开头的分行，然后打印出来
        
        if cha.isdigit() and positionN > 0 :                  #如果用isnumeric那么中文的数字也算进去了
            if  tmpStr[positionN-1].isdigit() == False:       #判断左边是否是数字，是则不分行，
                if  tmpStr[positionN+2].isdigit() == False:   #3位数及以上不分行
#                     if findChsWordsInaList(tmpStr,positionN+1)==False and findChsWordsInaList(tmpStr,positionN+2)==False :#屏蔽量词单位前的数字  
  
                        if tmpStr[positionN+1].isdigit(): #是双位数
                            if tmpStr[positionN:positionN+2]==str(chaNum+1) or tmpStr[positionN:positionN+2] ==str(secNum+1):
                                '''92-99行和104-112类似，可以考虑写个方法'''
                                Tmp_list.append(tmpStr[positionL:positionN])
                                positionL = positionN
                                if int(tmpStr[positionN:positionN+2])-int(lastSec) != 1 and tmpStr[positionN:positionN+2]==str(chaNum+1):
                                    secNum = 0
                                if secNum == 0 :
                                    chaNum += 1
                                secNum += 1
                                lastSec=tmpStr[positionN:positionN+2]
                             
                        else:                             #是单位数
                            if tmpStr[positionN]==str(chaNum+1) or tmpStr[positionN] ==str(secNum+1):#本位置等于下一章数或下一节数
                                '''92-99行和104-112类似，可以考虑写个方法'''
                                Tmp_list.append(tmpStr[positionL:positionN])
                                positionL = positionN
                                #如果本位置等于下一章数，而且与上一节的差不等于1，则节secNum归0重新开始计算节数
                                if tmpStr[positionN]==str(chaNum+1) and int(tmpStr[positionN])-int(lastSec) != 1 :    
                                    secNum = 0
                                if secNum == 0 :#每次节数归0，则章节加1，不可取消判断，否则第一次章节不会
                                    chaNum += 1
                                secNum += 1
                                lastSec=tmpStr[positionN]
                                
                            if  int(cha) == 2 and lastSec == str(chaNum+1) and secNum != 1 and chaNum !=1:#如果上一章的最后1节数刚好和上一章的数字一致，则从第2节开始重新计算新章节数
                                Tmp_list.append(tmpStr[positionL:positionN])
                                positionL = positionN
                                secNum = 2
                                chaNum += 1
                                lastSec=tmpStr[positionN]   
                      
        positionN += 1
        
    Tmp_list.append(tmpStr[positionL:positionN])#加入最后一行数据
    writeLinF(Tmp_list,pathNew)
    
'''
去除汉字，字母，数字以外的所有符号
'''
def removePunctuation(text):
   
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",text)

    return sub_str

'''
#在一个表aList内制定位置，查找并比较字长相等的词（该词来自于banlist），如果找到返回True，否则返回False
'''
def findChsWordsInaList(aList,wordBeginPosition):

    for ChsWord in banlist:   #banlist is Public
        word=aList[wordBeginPosition:wordBeginPosition+len(ChsWord)]#Word的长度根据ChsWord的长度而定。
        if word==ChsWord:
            return True
        
    return False

'''
将list写入文件，并分行
'''
def writeLinF(alist,fileName):

       tmpFile = open(fileName,'w', encoding='UTF-8')
       for line in alist:
           tmpFile.write(line+'\n')
  
       tmpFile.close()
       

if __name__ == '__main__':
    changeStyle(pNew,pNew)
    changeStyle(pOld,pOld)
    compare2files(pOld,pNew,PResult)
  
