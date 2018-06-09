#coding=utf-8
#Exercise12.3
flist=[]
def most_frequent():
    global flist
    list1=[]
    fin=open('D:\编程\Python\Mobywords.txt')
    for word1 in fin:
        word1=word1.strip()
        list1=metatheisi_pair(word1)
       
    return flist

def metatheisi_pair(word):
    pairlist=[]
    for i in word:
        pairlist.append(i)

    return pairlist
print(most_frequent())    
