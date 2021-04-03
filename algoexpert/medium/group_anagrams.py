"""
Group Anagrams
- Medium
- String
"""


def groupAnagrams(words):
    # Write your code here.
    ht = {}
    for i, word in enumerate(words):
        k = ''.join(sorted(word))
        if k in ht.keys():
            ht[k].append(word)
        else:
            ht[k] = [word]

    ret = []
    for k in ht.keys():
        ret.append(ht[k])

    return ret
