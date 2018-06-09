#coding=utf-8 
#Exercise11.6
# word_dic=dict()
def saperate_WandP(wordandpronounce,j):
    word_dic={}
    for i in range(len(wordandpronounce)):
                 if wordandpronounce[i]==' ' and i ==j:
                     word_dic[wordandpronounce[0:i]]=wordandpronounce[i:len(wordandpronounce)]
                     return word_dic   
                 
def find_wordandpronounce(j):
    word_d={}
    fin=open('D:\编程\Python\Wordsandpronounce.txt') 
    i=0
    for wordandpronounce in fin:
        wordandpronounce=wordandpronounce.strip()
        word_d=saperate_WandP(wordandpronounce,j)
    
    return word_d

for x in find_wordandpronounce(5):
    for y in find_wordandpronounce(4):
        if word_dic[x] == word_dic[y]:
           print(x,y)
