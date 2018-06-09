#coding=utf-8
#Exercise10.9
from __future__ import print_function, division
import time

def listwords(words):
    wordlist=[]
    for line in words:
         word=line.strip()
         wordlist.append(word)
    return wordlist
    print(wordlist)
    
def listwords2(words):
    wordlist=[]
    for line in words:
         word=line.strip()
         wordlist=wordlist+[word]
    return wordlist
#     print(wordlist) 
    
words=open('D:\编程\Python\Mobywords.txt')       
start_time = time.time()
t = listwords(words)
elapsed_time = time.time() - start_time
 
print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

# start_time = time.time()
# t = listwords2(words)
# elapsed_time = time.time() - start_time
# 
# print(len(t))
# print(t[:10])
# print(elapsed_time, 'seconds')