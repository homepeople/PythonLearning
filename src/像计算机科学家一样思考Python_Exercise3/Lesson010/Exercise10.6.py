#coding=utf-8
#Exercise10.6
def is_anagram(word1,word2):
     wordarr1=[]
     wordarr2=[]
     i=0
     j=0
     for i in range(len(word1)-1):
         wordarr1.append(word1[i])
     for j in range(len(word2)-1):
         wordarr2.append(word2[j])   
     wordarr1.sort() 
     if wordarr1==wordarr2:
         return True
     else:
         return False
print(is_anagram('bac', 'abc'))
