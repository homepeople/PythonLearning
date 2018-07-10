#coding=utf-8
#Exercise8.2
from urllib import request
# def is_palindrome(word):
#      if word==word[::-1]:
#          return True
#      else:
#          return False

     
# print(is_palindrome('level')) 


# import chardet
# if __name__ == "__main__":
#     
#     req = request.Request("http://fanyi.baidu.com/")
#     response=request.urlopen(req)
#     html = response.read()
#     html = html.decode("utf-8")
# #     charset=chardet.detect(html)
#     print(html)


# if __name__ == "__main__":
#     req = request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     print("geturl打印信息：%s"%(response.geturl()))
#     print('**********************************************')
#     print("info打印信息：%s"%(response.info()))
#     print('**********************************************')
#     print("getcode打印信息：%s"%(response.getcode()))

from urllib import parse
import json

if __name__ == "__main__":
    #对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    #创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['i'] = 'cat'
    Form_Data['from'] = 'en'
    Form_Data['to'] = 'zh-CHS'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1517388088019'
    Form_Data['sign'] = 'a9b4ab56147b5cc51bc5ce2d2c66a67b'
    Form_Data['doctype'] = 'json'
    Form_Data['Version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'lan-select'
    Form_Data['typoResult'] = 'false'
    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
    #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译信息
    print("翻译的结果是：%s" % translate_results)