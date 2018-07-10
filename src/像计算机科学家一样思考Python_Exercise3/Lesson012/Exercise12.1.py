#coding=utf-8
#Exercise12.1
# from __future__ import print_function, division
import string

wDict = {}
def make_histogram(word):
    global wDict
    for x in word:
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
 
if __name__ == '__main__':      
    d=percent_letter(most_frequent())
    print(sorted(d.items(),key = lambda item:item[0]))#item[0] sort Keys，item[1] sort Values


# def read_file(filename):
#     """Returns the contents of a file as a string."""
#     return open(filename).read()
# def make_histogram(s):
#     """Make a map from letters to number of times they appear in s.
#     s: string
#     Returns: map from letter to frequency
#     """
#     hist = {}
#     for x in s:
#         hist[x] = hist.get(x, 0) + 1
#     return hist
# 
# def most_frequent(s):
#     """Sorts the letters in s in reverse order of frequency.
# 
#     s: string
# 
#     Returns: list of letters
#     """
#     s=s.strip()
#     s=s.strip('\n')
#     hist = make_histogram(s)
#     t = []
#     for x, freq in hist.items():
#         t.append((freq, x))
# 
#     t.sort(reverse=True)
# 
# #     res = []
# #     for freq, x in t:
# #         res.append(x)
# 
#     return t
#     
# if __name__ == '__main__':
#     string = read_file('D:\编程\Python\Mobywords.txt')
#     letter_seq = most_frequent(string)
#     for x in letter_seq:
#         print(x)