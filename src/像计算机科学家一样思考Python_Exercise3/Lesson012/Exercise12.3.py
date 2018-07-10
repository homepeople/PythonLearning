#coding=utf-8
#Exercise12.3
def signature(s):
    """Returns the signature of this string.
  
    Signature is a string that contains all of the letters in order.
  
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t
  
def all_anagrams(filename):
    """Finds all anagrams in a list of words.
  
    filename: string filename of the word list
  
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
  
        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
            
    return d
def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.
  
    d: map from words to list of their anagrams
    """
    # make a tuple of (length(list), list[word pairs])
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort(reverse=True)
    print(t)
    
if __name__ == '__main__':
