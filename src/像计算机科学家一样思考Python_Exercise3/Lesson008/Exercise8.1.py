#coding=utf-8
#Exercise8.1
def show_fruit():
    fruit='banana'
    letter=fruit[0]
    print(letter)
    length=len(fruit)
    print(fruit[-6])
    
# show_fruit()

def printletter():
     prefixes='JKLMNOPQ'
     suffix='ack'

     for letter in prefixes:
         if letter == "Q":
             letter = "Qu"
         print(letter + suffix)
        
# printletter()

def print_slice():
    s='Monty Python'
    result=s[0:5]
    print(result)
    result=s[6:12]#python 要头不要尾，因此12不在范围内
    print(result)

# print_slice()

def findword():
     word='bobs'
     result=word.find('ob',0,3)
     print(result)

# findword()

def in_both(word1,word2):
    j=len(word1)
    for i in range(j):
        letter=word1[i]
        if letter in word2:
            print(letter,i)

# in_both('banana','nana' )#exchange the order you will find the difference

def beforeOrafter(word):
    if word=='Banana':
        print('All right Bananas')
    elif word>'Banana':
        print('Your word '+ word + ', comes after Banana')
    elif word<'Banana':
        print ('Your word '+ word + ', comes before Banana')
        
# beforeOrafter('Banana')

def is_reverse(word1, word2):
    if len(word1) != len(word2):
         return False
    i=0
    j=len(word2)-1
    
    while j>0:
        print(i,j)
        if word1[i] != word2[j]:
             return False
        i=i+1
        j=j-1
    return True
#          
# is_reverse('pots','stop')
def openfile():
    fin=open('D:\编程\Python\Mobywords.txt')
    line=fin.readline()
    print(line)
    
openfile()