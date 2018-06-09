#coding=utf-8
#Exercise10.11
from __future__ import print_function, division
import bisect
def make_word_list():
    """Reads lines from a file and builds a list using append.
    returns: list of strings
    """
    word_list = []
    fin=open('D:\编程\Python\Mobywords.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def get_palindrome(word):
    """
    returns:reverse word
    """
    word=word[::-1]
    return word
     
def in_bisect_fast(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return None
    elif  word_list[i] == word:
        return i

if __name__ == '__main__':
    wordlist=make_word_list()
    result=[]
    for word in make_word_list(): 
        numorg=in_bisect_fast(wordlist, word)
        palindrome=get_palindrome(word)
        numpal=in_bisect_fast(wordlist, palindrome)
        if numpal != None and word not in result:
            result.append(numorg)
            result.append(word)
            result.append(numpal)
            result.append(palindrome)
            result.append('')
    for i in result:
         print(i)
#             print (word,numorg,palindrome,numpal)
    