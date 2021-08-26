"""
211. Design Add and Search Words Data Structure
- Medium
- String, DFS, Design, Trie
- Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


# Solution 1: Trie
# Time: O(M) ~ O(N*M^26) | Space: O(1) ~ O(M), 依據 word definess 來決定
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]

        node['*'] = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for idx, w in enumerate(word):
                if w not in node:
                    if w == '.':
                        for n in node:
                            if n != "*" and search_in_node(word[idx+1:], node[n]):
                                return True
                    return False
                else:
                    node = node[w]

            return '*' in node

        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
