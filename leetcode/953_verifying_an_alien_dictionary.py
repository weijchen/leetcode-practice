"""
953. Verifying an Alien Dictionary
- Easy
- Hash Table
- Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
"""


# Solution 1: Hash Table
# Time: O(N * M) | Space: O(M), where M is 26
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        dic = {k: i for i, k in enumerate(order)}

        for i in range(1, len(words)):
            prev, cur = words[i-1], words[i]
            if not self.checkOrder(dic, prev, cur):
                return False
        return True

    def checkOrder(self, dic, prev, cur):
        if prev == cur:
            return True
        iter_length = max(len(prev), len(cur))

        for i in range(iter_length):
            if i >= len(prev):
                return True
            if i >= len(cur):
                return False
            prev_chr, cur_chr = prev[i], cur[i]
            if dic[prev_chr] > dic[cur_chr]:
                return False
            elif dic[prev_chr] < dic[cur_chr]:
                return True
            else:
                continue


# Solution 2: Hash Table + zip function
# Time: O(N * M) | Space: O(M), where M is 26
def isAlienSorted(self, words, order):
    m = {c: i for i, c in enumerate(order)}
    words = [[m[c] for c in w] for w in words]
    return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
