#coding=utf-8
#Exercise10.12
from findpalindrome import in_bisect_fast, make_word_list
# from itertools import chain
def saperate_word(word,oddoreven):
    newword=''
    i=0
    if oddoreven =='odd':
        for i in range(1, len(word), 2):
             newword=newword+word[i]
    else:
        for i in range(0, len(word), 2):
             newword=newword+word[i]
    return newword  
def saperate_wordto3(word,oddoreven):
    newword=''
    i=0
    if oddoreven =='odd':
        for i in range(1, len(word), 3):
             newword=newword+word[i]
    elif oddoreven =='even':
        for i in range(0, len(word), 3):
             newword=newword+word[i]
    else:
        for i in range(2, len(word), 3):  
             newword=newword+word[i]      
    return newword  
def find_chainwords(wordlist):  
    chainwords=[]
    for wholeword in wordlist:
        evenword=saperate_wordto3(wholeword, 'even')
        if in_bisect_fast(wordlist,evenword)!=None:
            oddword=saperate_wordto3(wholeword, 'odd')
            if in_bisect_fast(wordlist,oddword)!=None:
                 thirdword=saperate_wordto3(wholeword, 'third')
                 if in_bisect_fast(wordlist,thirdword)!=None:
                     chainwords.append(wholeword)
                     chainwords.append(evenword)
                     chainwords.append(oddword)
                     chainwords.append(thirdword)
                     chainwords.append('')
    return chainwords

if __name__=='__main__':
    wordlist=make_word_list()
    for i in find_chainwords(wordlist):
        print(i)