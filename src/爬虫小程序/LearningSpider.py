#coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import requests
#这个方法输入url地址和code类型，就可以打印出Html，测试python3有效
def printHtml(url,codeType):
    res=urllib.request.urlopen(url)
    htmlBytes=res.read()
    result=htmlBytes.decode(codeType)
#     print(htmlBytes.decode(codeType))
    return result

if __name__ == '__main__':
    target = 'https://www.biqukan.com/1_1094/5403177.html'
    url='https://wol.jw.org/cmn-Hans/wol/b/r23/lp-chs/nwt/CHS/2019/1/1#study=discover'
    novel=printHtml(target, 'gbk')
    html=printHtml(url, 'utf-8')
    bf = BeautifulSoup(novel)
    texts = bf.find_all('div', class_="showtxt") 
    print(texts[0].text.replace('\xa0'*8,'\n\n'))