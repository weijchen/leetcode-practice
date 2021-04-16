"""
Group Anagrams
- Medium
- String
"""


# Time: O(w*n*log(n)) - w is the number of words and n is the length of the longest word | Space: O(wn)
def groupAnagrams(words):
    # Write your code here.
    ht = {}
    for i, word in enumerate(words):  # w
        k = ''.join(sorted(word))  # nlog(n)
        if k in ht.keys():
            ht[k].append(word)
        else:
            ht[k] = [word]

    ret = []
    for k in ht.keys():
        ret.append(ht[k])

    return ret
