#coding=utf-8
#Exercise10.5
def is_sorted(list):
    templist=list[:]
    list.sort()
#if use 'is' to instead of '=='then 
# it would need exactly same 
# not noly value but also the memory address
    if templist == list:
        return True
    else:
        return False

print(is_sorted([1,2,3]))
print(is_sorted(['b','d','c']))