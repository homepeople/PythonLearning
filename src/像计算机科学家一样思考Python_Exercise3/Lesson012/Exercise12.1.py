#coding=utf-8
#Exercise12.1
import string
# def get_letterdict():
#     wDict = {} 
#     letter_list = string.ascii_letters
#     letter_list=letter_list[0:26]
#     for word in letter_list:
#         wDict[word]=0
#     return wDict
wDict = {}
def make_histogram(str):
    global wDict

    for x in str:
        wDict[x] = wDict.get(x, 0) + 1
#     return wDict   
 
def most_frequent():
    fin=open('D:\编程\Python\Mobywords.txt')  
    for word in fin:
        word=word.strip()
        make_histogram(word)
    return wDict
   
def percent_letter(wDict):
    WholeNum=0
    for x in wDict:
        WholeNum=wDict[x]+WholeNum
    for x in wDict:
        wDict[x]=wDict[x]/WholeNum
    return wDict
 
print(percent_letter(most_frequent()))
 