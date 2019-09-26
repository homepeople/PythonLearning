#coding=utf-8
#需求：比较2个相似文件的每一行，如果不同就把两句话都打印出来,比较结果输入到新的文件
#注意：2个源文件格式不100%相似，因此需要先更改格式为每句话1行，每行以章节序号开头，然后才能开始对相同序号的进行对比。
ChapterName='士师记'
pOld = 'D:/Programming/Bible/'+ChapterName+'bi12.txt'#老版本圣经存放的路径
pNew = 'D:/Programming/Bible/'+ChapterName+'nwt.txt'#新版本圣经存放的路径
PResult='D:/Programming/Bible/'+ChapterName+'比较结果.txt'#比较结果存放路径
#禁止的量词单位
'''
量词单位前的数字不排头,杜绝量词单位排头的可能性，因为不知道量词具体的数目，因此根据需要增加或减少
问题：有些非量词单位，但是和量词为同一个词开头的情况下就会出现屏蔽错误，比如：箴言12:25人心担忧，郁郁寡欢；听见良言，心里欢喜。
'''
banlist=["舍客勒","贺梅珥","季拉","件","套","下","人","岁","天","年","尺","日","夜","个","十","百","千","万","头","只","次","匹","颗","块","座","欣","罗格","皮姆","伊法","细亚","俄梅珥","罢特","歌珥","罗革","肘尺"]

import re
'''
比较2个类似文件的相同行，并把不同处输出到第三个新文件内
'''
def compare2files(path1,path2,resultpath):

    line1 = 0   #文件1当前行数
    diflines = 0#不同行的总行数
    allLines = 0#总行数
    Tmp_list=[] #临时表
    
    #检查2个文件相同行是否有不同之处
    for value1 in open(path1,'r', encoding='utf-8').readlines():    
        
        line2 = 0#文件2当前行数
        line1 = line1 + 1
        
        for value2 in open(path2,'r', encoding='utf-8').readlines():
            line2 = line2 + 1 
            
            if line1 == line2:#比较相同序号的行
                
                str2 =removePunctuation(str(value2))#去掉除数字，字母，汉字以外的所有符号
                str1 =removePunctuation(str(value1))
                
                if str1 != str2:#内容不相同，输出到Tmp_list
                    
                    print(str1)
                    print(str2)
                    Tmp_list.append(str1)
                    Tmp_list.append(str2)
                    diflines += 1
                    
        allLines += 1
        
    print(ChapterName+'共'+str(allLines)+'节经文'+',其中'+str(diflines)+'节不同')
    
    Tmp_list.append(ChapterName+'共'+str(allLines)+'节经文'+',其中'+str(diflines)+'节不同')
    
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
    
    for cha in tmpStr:#有数字开头的分行，然后打印出来
 
        if cha.isdigit() and positionN > 0 :                  #如果用isnumeric那么中文的数字也算进去了
            if  tmpStr[positionN-1].isdigit() == False:       #判断右边是数字就是超过1位数的不分行 
                if  tmpStr[positionN+2].isdigit() == False:   #3位数不分行
                    if findChsWordsInaList(tmpStr,positionN+1)==False and findChsWordsInaList(tmpStr,positionN+2)==False:#在量词单位前的数字不排头
                       Tmp_list.append(tmpStr[positionL:positionN])
                       positionL = positionN
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

