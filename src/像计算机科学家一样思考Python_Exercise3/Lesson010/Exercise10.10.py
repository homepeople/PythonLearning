#coding=utf-8
#Exercise10.10
# from __future__ import print_function, division
import bisect
import time

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


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)


def in_bisect_fast(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    returns: order number of word if the word is in the list; None otherwise
    if return False,because 0 == False would cause problem about the first word of the list
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return None
    elif  word_list[i] == word:
        return i

#     i = bisect.bisect_left(word_list, word)
#     if i==len(word_list):
#         return None
#     return i


if __name__ == '__main__':
    word_list = make_word_list()
#     start_time = time.time()
#     for word in ['aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob']:
#         print(word, 'in list', in_bisect(word_list, word))
#     elapsed_time = time.time() - start_time
# 
#     print(elapsed_time, 'seconds')
    
    start_time = time.time()
#     for word in ['aa']:
    for word in ['aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob']:
        if in_bisect_fast(word_list, word)== None:
             print(word, 'not in the list')
        else:
             print(word, 'in list', in_bisect_fast(word_list, word))
    elapsed_time = time.time() - start_time
 
    print(elapsed_time, 'seconds')
