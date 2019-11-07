#coding=utf-8
#需求：比较2个相似文件的每一行，如果不同就把两句话都记录,如果相同就记录1句，比较结果输入到新的文件
#注意：2个源文件格式不100%相似，因此需要先更改格式为每句话1行，每行以章节序号开头，然后才能开始对相同序号的进行对比。
import sys
import re
import requests

ChapterName='创世纪 1 online'
VersionName1='nwt'
VersionName2='bi12'
'''
'创世纪','出埃及记','利未记','民数记','申命记',
'约书亚记','士师记','路得记','撒母耳记上','撒母耳记下',
'列王纪上','列王纪下','历代志上','历代志下',
'以斯拉记','尼希米记','以斯帖记',
'约伯记',"诗篇","箴言","传道书",'雅歌',
'以赛亚书',"耶利米书","耶利米哀歌","以西结书",'但以理书',
'何西阿书','约珥书','阿摩司书','俄巴底亚书','约拿书',
'弥迦书','那鸿书','哈巴谷书','西番雅书','哈该书',
'撒迦利亚书','玛拉基书',

'马太福音','马可福音','路加福音','约翰福音',
'使徒行传','罗马书','哥林多前书','哥林多后书',
'加拉太书','以弗所书','腓立比书','歌罗西书',
'帖撒罗尼迦前书','帖撒罗尼迦后书','提摩太前书','提摩太后书',
'提多书','腓利门书','希伯来书','雅各书',
'彼得前书','彼得后书','约翰一书','约翰二书','约翰三书',
'犹大书','启示录'
'''
pOld = 'D:/Programming/Bible/'+ChapterName+'bi12.txt'#老版本圣经存放的路径
pNew = 'D:/Programming/Bible/'+ChapterName+'.txt'#新版本圣经存放的路径
PResult='D:/Programming/Bible/result/'+ChapterName+'(nwt，bi12合参本).txt'#比较结果存放路径
#禁止的量词单位
# '''
# 量词单位前的数字不排头,杜绝量词单位排头的可能性，因为不知道量词具体的数目，因此根据需要增加或减少
# 问题：有些非量词单位，但是和量词为同一个词开头的情况下就会出现屏蔽错误，比如：箴言12:25人心担忧，郁郁寡欢；听见良言，心里欢喜。
# '''


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
          
            value1=str(value1) #合参本，保存标点符号
            value2=str(value2)
            str2 =removePunctuation(value2)#去掉除数字，字母，汉字以外的所有符号
            str1 =removePunctuation(value1)
            if str1 != str2:#内容不相同，输出到Tmp_list
                if  str1[:1] != str2[:1]:#第一个字符不相等，则退出程序
                    print('首序列号不同'+str1[:1]+str2[:1])
                    sys.exit(0)
                    
                elif str1[1:2].isdigit() and str2[1:2].isdigit() and str1[1:2] != str2[1:2]:#第二位若都为数字，且不相等，则退出程序
                    print('次序列号不同'+str1[:2]+str2[:2])
                    sys.exit(0)       
#                 print(value1)
#                 print(value2)
                Tmp_list.append(value1.replace("\n", ""))
                Tmp_list.append(value2)
                diflines += 1
            else:#合参本，如果相同经文只收录一行
#                 print(str1)
                Tmp_list.append(value1)
        
        allLines += 1
        
    print(ChapterName+'共'+str(allLines-1)+'节经文'+',其中'+str(diflines)+'节不同')
    
    Tmp_list.append(ChapterName+'共'+str(allLines-1)+'节经文'+',其中'+str(diflines)+'节不同')

    writeLinF(Tmp_list,resultpath)#输出比较结果到文件


#更改文件每行开头为数字（因为经文每行开头都有数字，但是需要和句子中的数字区分开来）
'''
改变格式，每一行为一节经文，每行开头为经文章节数
# 注意几种情况，1开头不为数字，2数字在句子内（一般在量词前），3超过个位数的数字如何处理
# 思路：   1每节经文开头有数字，但是不一定是在句号后，因此不能通过句号判断是否是开头。
#       2因为数字一般出现在量词前，因此可以通过量词来屏蔽不需要的数字。
#      3因为经文一般不会超过3位数，因此可以根据情况进行过滤。(除了诗篇)
'''
def changeStyle(pathOld,pathNew):

    tmpStr = ''    #空字符（中间不加空格）
    
    for value1 in open(pathOld,'r', encoding='UTF-8').readlines():#打开文件，去换行，并把文件变为String
#         word1 = str(value1).replace(' ','')
        word1 = str(value1).replace('\n','')
        tmpStr += word1
    
    positionN = 0  #N是Next，切片下一次的开始位置
    positionL = 0  #L是Last，切片上一次的结束位置
    Tmp_list = []
    chaNum = 0
    secNum = 0
    lastSec='0'
    for cha in tmpStr:#有数字开头的分行，然后打印出来 
        if cha.isdigit() and positionN > 0 :                  #如果用isnumeric那么中文的数字也算进去了
            #左边不是数字和字符的标点符号,开始有章节题目，章节没有标点，可能会存在标点后面接数字且数字和下一节或下一章相等的bug
            if  re.match(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])",tmpStr[positionN-1]) != None or chaNum==0 :    
                
                digitNum = digitNumber(tmpStr[positionN:positionN+3])   #没有4位数以上的章节,因此只判断4位数 
                if digitNum != 4:                               #没有4位数以上的章节   
                       
                    aheadstr = tmpStr[positionN:positionN+digitNum]
                    #如果数字刚好等于下一章或下一节的数字 
                    if aheadstr==str(chaNum+1) or aheadstr ==str(secNum+1):
                           
                        Tmp_list.append(tmpStr[positionL:positionN])
                        positionL = positionN
                        #如果数字和上一节的差不等于1，而且等于下一章的数，那么就是新章节开头第一句
                        if int(aheadstr)-int(lastSec) != 1 and aheadstr==str(chaNum+1):
                            secNum = 0
                        if secNum == 0 :
                            chaNum += 1
                        secNum += 1
                        lastSec=aheadstr
                     
                        #如本章数等于上一章最后1节加1，则第2节经文，需重置节数和章数加1，第一章除外
                    if  int(aheadstr)==2 and lastSec == str(chaNum+1) and secNum != 1 and chaNum > 1:
                        Tmp_list.append(tmpStr[positionL:positionN])
                        positionL = positionN
                        secNum = 2
                        chaNum += 1
                        lastSec=aheadstr   
        positionN += 1

    Tmp_list.append(tmpStr[positionL:positionN])#加入最后一行数据
    writeLinF(Tmp_list,pathNew)
'''
判断一个定长字符串有几位数字，返回位数
''' 
def digitNumber(tmpStr):
    for digitNum in range(len(tmpStr),0,-1):
        tmpStr=tmpStr[0:digitNum]
        if tmpStr.isdigit():
            return digitNum
        
'''
去除汉字，字母，数字以外的所有符号
'''
def removePunctuation(text):
   
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",text)

    return sub_str

'''
#在一个表aList内指定位置，查找并比较字长相等的词，如找到返回True，否则返回False
'''
# banlist=["弥拿","塔兰特","舍客勒",'银','多',"贺梅珥","季拉",'米','公里',"倍","点","代","张","片","件","辆","套","拃","掌","下",
# "岁","天","年","尺","日","夜","个","十","百","千","万","头","只","次","匹","颗","块","座","欣","罗格","皮姆","伊法","细亚","俄梅珥",
# "罢特","歌珥","罗革","肘尺"]
# def findChsWordsInaList(aList,wordBeginPosition):
# 
#     for ChsWord in banlist:   #banlist is Public
#         word=aList[wordBeginPosition:wordBeginPosition+len(ChsWord)]#Word的长度根据ChsWord的长度而定。
#         if word==ChsWord:
#             return True
#         
#     return False

'''
将list写入文件，分行并加入空行
'''
def writeLinF(alist,fileName):
    tmpFile = open(fileName,'w', encoding='UTF-8')
    for line in alist:
        tmpFile.write(str(line)+'\n'*2)
        
    tmpFile.close()

def getWebInfo(pathNew):
    urlinfo='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/nwt/CHS/2019/1/1#study=discover'
    req = requests.get(urlinfo).text
#     r = re.findall('<script src="(.*?)"></script>', req.text)  # (.*?) 非贪婪匹配
    print(req)
    tmpFile = open(pathNew,'w', encoding='UTF-8')
    tmpFile.write(str(req)+'\n'*2)
    tmpFile.close()
    
if __name__ == '__main__':
#     changeStyle(pNew,pNew)
#     changeStyle(pOld,pOld)
#     compare2files(pOld,pNew,PResult)
    getWebInfo(pNew)