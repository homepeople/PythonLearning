#coding=utf-8
#Exercise12.2
from __future__ import print_function, division

def signature(s):
    """Returns the signature of this string.
  
    Signature is a string that contains all of the letters in order.
  
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    f=[]
    i,j=0
    for i in range(len(s)):
        for j in range (len(s)-1):
            if i!=j:
                t[i],t[j]=t[j],t[i]
                z=''.join(t)
                f.append(z)
    return f
  
def all_anagrams(filename):
    """Finds all anagrams in a list of words.
  
    filename: string filename of the word list
  
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
#         t = signature(word)
  
        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
            
    return d
  
def print_anagram_sets(d):
    """Prints the anagram sets in d.
  
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)
          
def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.
  
    d: map from words to list of their anagrams
    """
    # make a tuple of (length(list), list[word pairs])
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v)) #12.2
#             t.append(v)#12.1
    # sort in ascending order of length
    t.sort()
#     print(t)
    # print the sorted list,but cannt print them all in one page
    for x in t:
        print(x)
  
  
def filter_length(d,n):
    """Select only the words in d that have n letters.
  
    d: map from word to list of anagrams
    n: integer number of letters
  
    returns: new map from word to list of anagrams
    """
    res = {}
#     n = len(d)
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res
  
if __name__ == '__main__':
    anagram_map = all_anagrams('D:\编程\Python\Mobywords.txt')
    print_anagram_sets_in_order(anagram_map)
#     print_anagram_sets(anagram_map)
    eight_letters = filter_length(anagram_map,8)
    print_anagram_sets_in_order(eight_letters)
     