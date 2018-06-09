#coding=utf-8
#Exercise10.8
#if they was born at same year,then get the posibilty of the same birday in one 23 students class
def ramdon_birthday(students):
     pos=0.0
     for i in range(students):
        pos=i/365+pos
     print(pos)
ramdon_birthday(27)   