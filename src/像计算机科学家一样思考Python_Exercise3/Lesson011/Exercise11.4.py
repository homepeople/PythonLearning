#coding=utf-8
#Exercise11.4

from __future__ import print_function, division
import time

def has_duplicates(t):#快一点点，很奇怪，看来未必行数少就越快
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False
def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)
if __name__=='__main__':    
    start_time = time.time()
    for i in range(1000):
        t=[1,2,3,4,5]
        print(has_duplicates(t))
        t.append(1)
        print(has_duplicates(t))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'seconds')

# t=[1,2,3,4,5]
# print(has_duplicates2(t))
# t.append(1)
# print(has_duplicates2(t))