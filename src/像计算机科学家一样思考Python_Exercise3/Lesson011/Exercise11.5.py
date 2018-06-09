#coding=utf-8
#Exercise11.5
import time
def rotate_word(word):
    rotate_word=word[::-1]
    return rotate_word

def make_word_dict():
    d=dict()
    fin=open('D:\编程\Python\Mobywords.txt')
    for word in fin:
        word =word.strip()
        d[word] =None
    return d

if __name__=='__main__':
     word_dict=make_word_dict()
     for word in word_dict:
         if rotate_word(word) in word_dict:
             word_dict[word]=rotate_word(word)
             print(word,rotate_word(word))
#      print(word_dict)        
