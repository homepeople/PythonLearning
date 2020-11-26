# -*- coding: utf-8 -*-

'''
compare different version of Bible by each verse,and put the different verse together, 
if the verse content are exactly same then the verse print once and plus their version info together
比较不同版本的圣经的每一节经文，并将不同版本的同一节经文放在一起，相同经文只打印一次并把版本信息合并
'''
import urllib.request
from bs4 import BeautifulSoup
import re
import itertools
import sys
import ThreadWithReturnValue


'''
Regular Expression function for string
'''
def get_left_number(tmpStr):#input string,return all number of string at left side,return it as a string.输入字符串，返回靠左连续数字的位数
    for numberLength in range(len(tmpStr),0,-1):
        tmpStr = tmpStr[0:numberLength]
        
        if tmpStr.isdigit():
            return numberLength


def cut_string_out(StrA,StrB,Tstr):#find the value between StrA and StrB within Tstr,return it as a string.在Tstr中截取StrA到StrB之间的值

    result = re.findall(".*%s(.*)%s.*" %(StrA,StrB),Tstr)
    return result[0]  


'''
Get Information from Original URL
'''
def get_version(url):#get language + version of Bible from original url,return it as a string
    
    version = '('+ cut_string_out('lp-','/\d+/\d+',url) + ')'   
    return version  


def get_book_number(url):#get BookNumber of Bible from original url,return it as a string.从原URL中获取圣经书籍数字，并返回该数字的值
    
    BookNumber = cut_string_out('/\w+/','/\d+',url)
    return BookNumber


def get_chapter_number(url):#get Chapter of Bible from original url,return it as a string
    
    ChapterNumber = cut_string_out('/\d+/','#study=discover',url)   
    return ChapterNumber


'''
Get Text from Html of URL
'''
def get_Chapter_text_Tuple(url):#get Text from html by BeautifulSoup,return it as a tuple
    
    TargetTitle = 'div'
    TargetID = "article"
    
    htmls = connect_URL_test(get_html_with_decode,url) #with or without decode,which one is better?
    
    bf =  BeautifulSoup(htmls,"html.parser")

    texts = bf.find_all(TargetTitle, id=TargetID) 

    ChapterTextTuple = divide_string_by_beggin_Number_of_senctence_withException(texts[0].text,url)#divide text by firstNumber to get each verse in chapter

    return ChapterTextTuple


def connect_URL_test(get_html_fun,url):
    try:
        print("Now loading : %s" % url)
        html = get_html_fun(url)
    except urllib.request.HTTPError as exp:
        print(exp.code)
        sys.exit(0)
    except urllib.request.URLError as exp:
        print(exp.reason)
        sys.exit(0)
    else:
        print("loaded: %s" % url);
        return html


def get_html_with_decode(url):#Decode Html from URL with codeType，return StringHtml

    response = urllib.request.urlopen(url)
    
    htmlBytes = response.read()
    
    StringHtml = htmlBytes.decode('utf-8')
    
    return StringHtml


def get_html(url):#get Html Without decode,return html

    response =  urllib.request.urlopen(url)
    
    html = response.read()
    
    return html


'''
Arrange The Text and combine some different Bible as one as getting the some verse together
'''

def divide_string_by_beggin_Number_of_senctence_withException(tmpStr,url): #divide a long string to a Tuple by the number at begging of sentence,return new Tuple，根据每句开头数字分行建立新表,并返回分行后的新表
    positionN = 0  #N是Next，切片下一次的开始位置
    positionL = 0  #L是Last，切片上一次的结束位置
    Tmp_Tuple = ()
    chaNum = 0
    verNum = 0 
    
    tmpStr = tmpStr.replace('\n',' ').replace('+','').replace('*','').replace('. ','.').replace('。 ','。').replace('? ','?').replace('! ','!')
   
    for char in tmpStr:#有数字开头的分行
          
        if char.isdigit() and positionN > 0 :                  #如果用isnumeric那么非阿拉伯数字也会算进去
            
            pat = u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])" 
         
            nextValue = tmpStr[positionN-1]
            if  re.match(pat,nextValue) != None or chaNum == 0 : #右边边不是数字，字符，中文字等一切符号或者是第一次调入
                chaNum=get_chapter_number(url)  
                chapterLength = get_left_number(tmpStr[positionN:positionN+3])  
                  
                if chapterLength < 4:                                      #length of chapter and verse number is less than 4,章节数小于4位   
                     
                    aheadstr = tmpStr[positionN:positionN + chapterLength]    
                    
                    if  int(aheadstr) - verNum == 1 or (aheadstr == chaNum and verNum == 0): #first number is number of verse or chapter#句头数字等于节数或章数
                      
                        if  len(tmpStr[positionN:]) > 8:#for Numbers chapter 20 verse 29
                            Tmp_Tuple += (tmpStr[positionL:positionN],)
                            positionL = positionN
                            verNum += 1
                              
                    elif len(tmpStr[positionL:positionN]) < 5 and verNum == 1:#THE Exception for book 43 chapter 8,because the chapter start at verse 12 #小于5因为最大章数为3位数然后加1个空格，适用于所有开始节数大于2的空白章
                        Tmp_Tuple += (tmpStr[positionL:positionN],)
                        
                        while len(Tmp_Tuple) < int(aheadstr) :
                            verNum += 1
                            Tmp_Tuple += (verNum,)
                            
                        positionL = positionN 
                        verNum +=  1
                      
        positionN += 1
   
    Tmp_Tuple += (tmpStr[positionL:positionN],)#add the last line 加入最后一行数据
    return Tmp_Tuple


def combine_Tuples(versionT,tupleChapter): #zip tuples as a list with dictionary item,return the list,if version number is one ,this function would be faster than combine_Tuples_simple
    printList = [] 
    newList = [] 

    for tup in itertools.zip_longest(*tupleChapter):#zip tuples to list with dictionary item
        n = 0
        for line in tup:
#              line=" ".join(line.split())   #replace \xa0 if print as dictionary
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


def print_dict_unit_within_list(newList):#Print every List Unit which is Dictionary 
    
    for dic in newList:#print result 
        if dic != '':
            for key,value in dic.items():
                print('{key} {value}'.format(key = key, value = value))
        else:#print the empty line
            print(dic)

def return_dict_unit_within_list(newList):#Print every List Unit which is Dictionary 
    result='<meta charset="utf-8"/>'
    for dic in newList:#print result 
        if dic != '':
            for key,value in dic.items():
               result =result +'<div>' + '{key} {value}'.format(key = key, value = value) +'</div>'
        else:#print the empty line
            result = result +'<br>'
    return result

def merg_dict(list):#merg many dictionary of a list,return a dictionary
    dict2 = {}
    
    for dict1 in list:
        dict2 = dict_union(dict1, dict2)
        
    return dict2   


def dict_union(dica, dicb):#unite 2 dictionary to new one,plus value of same key,return dictionary
    newDic = {}
    
    for key in dica:
        if dicb.get(key) and type(dica[key]) != type(dicb[key]):
            newDic[key] = str(dica[key]) + str(dicb[key]) 
            
        elif dicb.get(key) and type(dica[key]) == type(dicb[key]):
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

def get_textT_from_URLT_Multi_Thread(get_str_from_Url,urlTuple):#get text tuple from url tuple,return a tuple
    textTuple = ()  
    threads=[]
    
    for url in urlTuple:
        tempStr = ThreadWithReturnValue.ReturnValue(target=get_str_from_Url, args=(url,))
        threads.append(tempStr)
        
    for x in threads:
        x.start()
        
    for x in threads:#join to hold the progress and return the value
        textTuple = (x.join(),) + textTuple
    
    return textTuple  
  

def call_main(urlTuple):

    versionTuple = get_textT_from_URLT(get_version, urlTuple)#get version as tuple

    ChapterTextTuple = get_textT_from_URLT_Multi_Thread(get_Chapter_text_Tuple, urlTuple)#get chapter text as tuple
 
    newList = combine_Tuples(versionTuple,ChapterTextTuple)#combine tuples as a list with dicttionary unit
    
    # print_dict_unit_within_list(newList) #print result
    result=return_dict_unit_within_list(newList)
    return result

'''
 UI interface backward #draft
'''
from cefpython3 import cefpython as cef
# import sys
import platform

# HTML_code = """
# <div>hello there</div>
# """

def main(HTML_code):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    cef.CreateBrowserSync(url=cef.GetDataUrl(HTML_code),
                           window_title='Book '+BOOK+': CHAPTER '+ CHAPTER)
    cef.MessageLoop()
    cef.Shutdown()

def main_web():
    # check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://wol.jw.org/",
                          window_title="Hello Friend!")
    cef.MessageLoop()
    cef.Shutdown()



def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"
    
if __name__ == '__main__':
        # main_web()
        BOOK='41'          #BOOK 1 is Genesis, 66 is Revelation,and so on
        TempChap = 0
        CHAPTER=""
        Chapters = ('16','15')
        
        while TempChap <  len(Chapters):
            CHAPTER=Chapters[TempChap]
            url1='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/nwt/'+BOOK+'/'+CHAPTER+'#study=discover'#新世界13年译本
            url2='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/bi12/'+BOOK+'/'+CHAPTER+'#study=discover'#新世界83年译本
            url3='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/sbi1/'+BOOK+'/'+CHAPTER+'#study=discover'#和合本
            url4='https://wol.jw.org/en/wol/b/r1/lp-e/nwt/'+BOOK+'/'+CHAPTER+'#study=discover'#New World Translation 2013
            url5= 'https://wol.jw.org/en/wol/b/r1/lp-e/by/'+BOOK+'/'+CHAPTER+'#study=discover'#The Bible in Living English
            url6='https://wol.jw.org/en/wol/b/r1/lp-e/bi22/'+BOOK+'/'+CHAPTER+'#study=discover'#American Standard Version
            url7='https://wol.jw.org/en/wol/b/r1/lp-e/bi10/'+BOOK+'/'+CHAPTER+'#study=discover'#King James Version

            TempChap += 1
            urlTuple=(url2,url5,url4)
            # call_main(urlTuple)
            HTML_code= call_main(urlTuple)
            #print(HTML_code)
          
            main(HTML_code)