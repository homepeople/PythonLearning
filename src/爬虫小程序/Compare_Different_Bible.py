# -*- coding: utf-8 -*-

'''
compare different version of Bible by each verse,and put the different verse together, 
if the verse content are same then the verse print once and plus their version info together
比较不同版本的圣经的每一节经文，并将不同版本的同一节经文放在一起，相同经文只打印一次并把版本信息合并
1.如果不同版本的同节经文完全一致，则该经文只打印一次，但版本号会在该节经文后叠加
2.如果不同版本的同一章经文节数不同，则没有经文的节数会显示为None(例如：马可福音16章，约翰福音8章)
'''

import urllib.request
import requests
#  from bs4 import BeautifulSoup
import bs4
import re
import time
import itertools
import http

'''
Regular Expression function to solve string
'''
def get_left_number(tmpStr):#input string,return all number of string at left side,return a string.输入字符串，返回靠左连续数字的位数
    for numberLength in range(len(tmpStr),0,-1):
        tmpStr = tmpStr[0:numberLength]
        
        if tmpStr.isdigit():
            return numberLength


def cut_string_out(StrA,StrB,Tstr):#find the value between StrA and StrB within Tstr,return a string.在Tstr中截取StrA到StrB之间的值
    result = re.findall(".*%s(.*)%s.*" %(StrA,StrB),Tstr)

    for i in result:#result is a list,return i as string
        return i


'''
    Get Information from Original URL
'''
def get_version(url):#get language + version of Bible from original url,return a string
    
    version = '('+ cut_string_out('lp-','/\d+/\d+',url) + ')'   
    return version  


def get_book_number(url):#get BookNumber of Bible from original url,return it as a string.从原URL中获取圣经书籍数字，并返回该数字的
    
    BookNumber = cut_string_out('/\w+/','/\d+',url)
    return BookNumber


def get_chapter_number(url):#get Chapter of Bible from original url,return a string
    
    ChapterNumber = cut_string_out('/\d+/','#study=discover',url)   
    return ChapterNumber


'''
Get Text from Html of URL
'''
def get_Chapter_text_Tuple(url):#get Text from html by BeautifulSoup,return tuple
    
    CodeType = 'UTF-8'
    TargetTitle = 'div'
    TargetID = "article"
    
    htmls = connect_URL_test(get_html,url) 

    bf =bs4.BeautifulSoup(htmls,"html.parser")
    
    texts = bf.find_all(TargetTitle, id=TargetID) 

    ChapterTextTuple = divide_string_by_begin_Number_of_senctence_withException(texts[0].text,url)#divide text by firstNumber to get each verse in chapter

    return ChapterTextTuple

def connect_URL_test(get_html_fun,url):
    try:
        print("Now loading : %s" % url)
        html = get_html_fun(url)
    except urllib.request.HTTPError as exp:
        print(exp.code)
    except urllib.request.URLError as exp:
        print(exp.reason)
    else:
        print("loaded: %s" % url);
        return html
    
def get_decode_html(url,CodeStyle):#Decode Html from URL with codeType，return StringHtml

    response = urllib.request.urlopen(url)
    
    htmlBytes = response.read()
    
    StringHtml = htmlBytes.decode(CodeStyle)
    
    return StringHtml


def get_html(url):#get Html Without decode,return html

    response = urllib.request.urlopen(url)
    
    html = response.read()
    
    return html


'''
Arrange The Text and combine some different Bible as one as getting the some verse together
'''
def divide_string_by_begin_Number_of_senctence_general(tmpStr,url): #divide a long string to a Tuple by the number at begging of sentence,return new Tuple，根据每句开头数字分行建立新表,并返回分行后的新表
    positionN = 0  #N是Next，切片下一次的开始位置
    positionL = 0  #L是Last，切片上一次的结束位置
    Tmp_Tuple = ()
    chaNum = 0
    verNum = 0
  
    tmpStr = tmpStr.replace('\n','').replace('+','').replace('*','').replace('. ','.').replace('。 ','。').replace('? ','?').replace('! ','!')
      
    for char in tmpStr:#有数字开头的分行
          
        if char.isdigit() and positionN > 0 :                  #如果用isnumeric那么非阿拉伯数字也会算进去
              
            pat = u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])" 
            if  re.match(pat,tmpStr[positionN-1]) != None or chaNum == 0 : #右边边不是数字，字符，中文字等一切符号或者是第一次调入
                  
                chaNum=get_chapter_number(url)                            #Get chapter number as string from url
  
                numberLength = get_left_number(tmpStr[positionN:positionN+3])  
                  
                if numberLength < 4:                                      #length of chapter and verse number is less than 4,章节数小于4位   
                     
                    aheadstr = tmpStr[positionN:positionN + numberLength]    
                      
                    if aheadstr == str(verNum + 1) or (aheadstr == chaNum and verNum == 0): #first Number is number of verse or chapter句头数字等于节数或章数
                          
                        Tmp_Tuple += (tmpStr[positionL:positionN],)
                        positionL = positionN  
                        verNum += 1                        
        positionN += 1
   
    Tmp_Tuple += (tmpStr[positionL:positionN],)#add the last line 加入最后一行数据
    return Tmp_Tuple
  
  
def divide_string_by_begin_Number_of_senctence_withException(tmpStr,url): #divide a long string to a Tuple by the number at begging of sentence,return new Tuple，根据每句开头数字分行建立新表,并返回分行后的新表
    positionN = 0  #N is Next,Mean Next slice position. N是Next，切片下一次的开始位置
    positionL = 0  #L is Last,Mean Last slice position. L是Last，切片上一次的结束位置
    Tmp_Tuple = ()
    chaNum = 0
    verNum = 0
  
    tmpStr = tmpStr.replace('\n','').replace('+','').replace('*','').replace('. ','.').replace('。 ','。').replace('? ','?').replace('! ','!')
   
    for char in tmpStr:
          
        if char.isdigit() and positionN > 0 :                  #if use isnumeric: no only 0-9 also count all kind of number like Chinese number.如果用isnumeric那么非阿拉伯数字也会算进去。
            pat = u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])" 
            
            if  re.match(pat,tmpStr[positionN-1]) != None or chaNum == 0 :  #left position is not number,character,Chinese Word                   
                chaNum = get_chapter_number(url)  
                numberLength = get_left_number(tmpStr[positionN:positionN+3])  
                
                if numberLength < 4:                                      #length of chapter and verse number is less than 4,章节数小于4位   
                     
                    aheadstr = tmpStr[positionN:positionN + numberLength]
                     
                    if  int(aheadstr) - verNum == 1 or (aheadstr == chaNum and verNum == 0): #first Number is number of verse or chapter句头数字等于节数或章数
                        if  len(tmpStr[positionN:]) > 8:#for Numbers chapter 20 verse 29
                            Tmp_Tuple += (tmpStr[positionL:positionN],)
                            positionL = positionN
                            verNum += 1
                              
                    elif len(tmpStr[positionL:positionN]) < 5 and verNum == 1:#THE Exception for book 43 chapter 8 only,because the chapter start at verse 12 #小于5因为最大章数为3位数然后加1个空格，适用于所有开始节数大于2的章
                        Tmp_Tuple += (tmpStr[positionL:positionN],)
                        
                        while len(Tmp_Tuple) < int(aheadstr) :
                            verNum += 1
                            Tmp_Tuple += (verNum,)
                            
                        positionL = positionN 
                        verNum += 1                          
        positionN += 1
   
    Tmp_Tuple += (tmpStr[positionL:positionN],)#add the last line 加入最后一行数据
    return Tmp_Tuple


def combine_Tuples(versionT,tupleChapter): #zip tuples as a list with dictionary item,return the list,if version number is one ,this function would be faster
    printList = [] 
    newList = [] 

    for tup in itertools.zip_longest(*tupleChapter):#zip tuples to list with dictionary item
        n = 0
        for line in tup:
#              line=" ".join(line.split())#replace \xa0 if print as dictionary
            tmpDicA = {line:versionT[n]}
            printList.append(tmpDicA)
            n += 1 
            
            if len(printList) == len(versionT) and len(versionT) != 1 :
                
                for x in printList[::len(versionT)]:#merge same content of different version(content are keys,version are value of dictionary) from many dictionary
                    newList.append(merg_dict(printList[:len(versionT)]))
                    printList = printList[len(versionT):]
                    newList.append('')
                    
            elif len(versionT) == 1:
                printList.append('')
                
    if len(versionT) != 1:
        return newList
    else:
        return printList
    
    
def combine_Tuples_simple(versionT,tupleChapter): #exactly same as combine_Tuples can do,just read it easier
    printList = [] 
    newList = [] 

    for tup in itertools.zip_longest(*tupleChapter):#zip tuples to list with dictionary item
        n = 0
        for line in tup:
            tmpDicA = {line:versionT[n]}
            printList.append(tmpDicA)
            n += 1 
            
    for x in printList[::len(versionT)]:#merge same content of different version(content are keys,version are value of dictionary) from many dictionary
        newList.append(merg_dict(printList[:len(versionT)]))
        printList = printList[len(versionT):]
        newList.append('')
        
    return newList


def print_dict_unit_within_list(newList):#Print every List Unit which is Dictionary 
    for dict in newList:#print result 
        if dict != '':
            for key,value in dict.items():
                print('{key} {value}'.format(key = key, value = value))
        else:
            print(dict)


def merg_dict(list):#merg many dictionary of a list,return a dictionary
    dict2 = {}
    for dict1 in list:
        dict2 = dict_union(dict1, dict2)
        
    return dict2   


def dict_union(dica, dicb):#unite 2 dictionary to new one,plus value of same key,return dictionary
    newDic = {}
    for key in dica:
        if dicb.get(key):#if key are same,plus their value
            newDic[key] = dica[key] + dicb[key]
        else:
            newDic[key] = dica[key]
            
    for key in dicb:
        if dica.get(key):
            pass
        else:
            newDic[key] = dicb[key]

    return newDic


def get_textT_from_URLT(get_str_from_Url,urlTuple):#get text tuple from url tuple,return a tuple
    textTuple = ()  
    
    for url in urlTuple:
        tempStr = get_str_from_Url(url)
        textTuple = (tempStr,) + textTuple
        
    return textTuple   


def call_main(url):
    
    versionTuple = get_textT_from_URLT(get_version,url)#get version as tuple

    ChapterTextTuple = get_textT_from_URLT(get_Chapter_text_Tuple,url)#get chapter text as tuple

    newList = combine_Tuples(versionTuple,ChapterTextTuple)
    
    print_dict_unit_within_list(newList)


'''
 UI interface backward #draft
'''


if __name__ == '__main__':

    BOOK='43'         #BOOK 1 is Genesis ，66 is Revelation,and so on
    TempChap = 0
    CHAPTER ='' 
    Chapters=("8",)
    while TempChap < len(Chapters):
        CHAPTER = Chapters[TempChap]
        url1='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/nwt/'+BOOK+'/'+CHAPTER+'#study=discover'
        url2='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/bi12/'+BOOK+'/'+CHAPTER+'#study=discover'
        url3='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/sbi1/'+BOOK+'/'+CHAPTER+'#study=discover'
        url4='https://wol.jw.org/en/wol/b/r1/lp-e/nwt/'+BOOK+'/'+CHAPTER+'#study=discover'
        TempChap += 1
        tupOfUrl=(url1,url4)
        call_main(tupOfUrl)