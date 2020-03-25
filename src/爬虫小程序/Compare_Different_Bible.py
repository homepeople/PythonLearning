# -*- coding: utf-8 -*-
'''
compare different version of Bible by each verse,and put the different verse together, 
if the verse content are same then the verse print once and plus their version info together
比较不同版本的圣经的每一节经文，并将不同版本的同一节经文放在一起，相同经文只打印一次并把版本信息合并
'''
import urllib.request
from bs4 import BeautifulSoup
import re
import time
#  from tkinter import *
from Tk import Tkinter


'''
Regular Expression function to solve string
'''
def getLeftNumber(tmpStr):#input string,return all number of string at left side.输入字符串，返回靠左连续数字的位数
    for digitPos in range(len(tmpStr),0,-1):
        tmpStr=tmpStr[0:digitPos]
        if tmpStr.isdigit():
            return digitPos

def cut_out(StrA,StrB,Tstr):#find the value between StrA and StrB from Tstr.在Tstr中截取StrA到StrB之间的值
    result = re.findall(".*%s(.*)%s.*" %(StrA,StrB),Tstr)
    for i in result:
       return i

'''
    Get Information from Original URL
'''
def getVersion(url):#get language + version of Bible from original url,return a string
    version='('+ cut_out('lp-','/\d+/\d+',url) + ')'   
    return version  

def getBookNumber(url):#get BookNumber of Bible from original url,return it as a string.从原URL中获取圣经书籍数字，并返回该数字的
    BookNumber=cut_out('/\w+/','/\d+',url)
    return BookNumber

def getChapterNumber(url):#get Chapter of Bible from original url,return a string
    ChapterNumber=cut_out('/\d+/','#study=discover',url)   
    return ChapterNumber

'''
Get Text from Html of URL
'''
def get_TupleofChapter_FromUrl(url,CodeStyle,TagetTitle,TagetID):#get Text from html by BeautifulSoup,return tuple
    htmls=getHtmlWithDecode(url, CodeStyle)#with or without decode,which one is better?
    bf = BeautifulSoup(htmls,"html.parser")
    texts = bf.find_all(TagetTitle, id=TagetID) 
    TupleofChapter=arrange_Line_FirstNum(texts[0].text,url)#divide text by firstNumber to get each verse in chapter
    return TupleofChapter

def getHtmlWithDecode(url,codeType):#Decode Html from URL with codeType，return StringHtml
    response=urllib.request.urlopen(url)
    htmlBytes=response.read()
    StringHtml=htmlBytes.decode(codeType)
    return StringHtml

def getHtml(url,codeType):#get Html Without decode,return html
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

'''
Arrange The Text and combine some different Bible as one as getting the some verse together
'''
def arrange_Line_FirstNum(tmpStr,url): #divide line to a list by the beginning number,return new list，根据每句开头数字分行,并返回分行后新表
    positionN = 0  #N是Next，切片下一次的开始位置
    positionL = 0  #L是Last，切片上一次的结束位置
    Tmp_Tuple = ()
    chaNum = 0
    secNum = 0
  
    tmpStr = tmpStr.replace('\n','').replace('+','').replace('*','').replace('. ','.').replace('。 ','。').replace('? ','?').replace('! ','!')
      
    for char in tmpStr:#有数字开头的分行
          
        if char.isdigit() and positionN > 0 :                  #如果用isnumeric那么中文的数字也算进去了
              
            #左边不是数字和字符的标点符号,开始有章节题目，章节没有标点，可能会存在标点后面接数字且数字和下一节或下一章相等的bug
            pat =u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])"# 
              
            if  re.match(pat,tmpStr[positionN-1]) != None or chaNum==0 :    
                chaNum=getChapterNumber(url)                            #Get chapter string from url
               # chaNum=cut_out('/','#study=discover',url)              #Get chapter string from url
                digitPos = getLeftNumber(tmpStr[positionN:positionN+3])  #没有3位数以上的章节,因此只判断3位数 
                  
                if digitPos != 4:                                      #digit position of chapter is not longer than 3,没有3位数及以上的章节   
                     
                    aheadstr = tmpStr[positionN:positionN+digitPos]    #句头数字
                      
                    if aheadstr ==str(secNum+1) or (aheadstr == chaNum and secNum == 0): #first Number is number of verse or chapter句头数字等于节数或章数
                          
                        Tmp_Tuple += (tmpStr[positionL:positionN],)
                        positionL = positionN  
                        secNum += 1                        
        positionN += 1
   
    Tmp_Tuple += (tmpStr[positionL:positionN],)#add the last line 加入最后一行数据
    return Tmp_Tuple
          
def combine_Tuples(versionT,*tupleX): #zip tuples as a list with dictionary item,return the list
    printList=[] 
    newList=[] 
    for tup in zip(*tupleX):#zip tuples to list with dictionary item
        n=0
        for line in tup:
#              line=" ".join(line.split())#replace \xa0 if print as dictionary
            tmpDicA={line:versionT[n]}
            printList.append(tmpDicA)
            n+=1 
            
    for x in printList[::len(versionT)]:#merge same content of different version(content are keys,version are value of dictionary) from many dictionary
        newList.append(merg_dict(printList[:len(versionT)]))
        printList=printList[len(versionT):]
        newList.append('')
    
    return newList

def printListWithDictUnit(newList):#Print every List Unit which is Dictionary 
    for dict in newList:#print result 
        if dict!='':
            for key,value in dict.items():
                print('{key} {value}'.format(key = key, value = value))
        else:
            print(dict)

def merg_dict(list):#merg many dictionary of a list,return a dictionary
    dict2={}
    for dict1 in list:
        dict2=dict_union(dict1, dict2)
        
    return dict2   

def dict_union(dica, dicb):#unite 2 dictionary to new one,return the new dictionary
    dic={}
    for key in dica:
        if dicb.get(key):#if key are same,plus their vaules
            dic[key]=dica[key]+dicb[key]
        else:
            dic[key]=dica[key]
    for key in dicb:
        if dica.get(key):
            pass
        else:
            dic[key]=dicb[key]

    return dic

'''
 UI interface backward #draft
'''
def MainUI():#draft
    top=Tk.Tk()
    B = Tk.Button(top, text ="Run", command = CallAllBack)
    B.pack()
    top.mainloop() 

class Application(Frame):#draft
    def ___init___(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.quitButton= Button(self, text ="Run", command = self.quit)
        self.quitButton.grid()

def CallAllBack():
    CodeStyle='UTF-8'
    TargetTitle='div'
    TargetID="article"
    book='43'
    chapter='7'
     #input url where the book and the chapter should be the same
    url1='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/nwt/'+book+'/'+chapter+'#study=discover'
    url2='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/bi12/'+book+'/'+chapter+'#study=discover'
    url3='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/sbi1/'+book+'/'+chapter+'#study=discover'
    url4='https://wol.jw.org/en/wol/b/r1/lp-e/nwt/'+book+'/'+chapter+'#study=discover'

    version1=getVersion(url1)
    version2=getVersion(url2)
    version3=getVersion(url3)
    version4=getVersion(url4)
    versionT=(version1,version2,version3,version4)

    Tuple1=get_TupleofChapter_FromUrl(url1,CodeStyle,TargetTitle,TargetID)
    Tuple2=get_TupleofChapter_FromUrl(url2,CodeStyle,TargetTitle,TargetID)
    Tuple3=get_TupleofChapter_FromUrl(url3,CodeStyle,TargetTitle,TargetID)
    Tuple4=get_TupleofChapter_FromUrl(url4,CodeStyle,TargetTitle,TargetID)

    newList=combine_Tuples(versionT,Tuple1,Tuple2,Tuple3,Tuple4)
    printListWithDictUnit(newList)

def callAllback1(bookNum,Chapter,*URL):#draft
    CodeStyle='UTF-8'
    TargetTitle='div'
    TargetID="article"
    for url in URL:
        cut_out(StrA, StrB, Tstr)
if __name__ == '__main__':
#      app=Application()
#      app.master.title("Sample Application")
#      app.mainloop()

#      CallAllBack()

    MainUI()

