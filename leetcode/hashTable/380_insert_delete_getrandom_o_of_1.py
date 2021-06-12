"""
380. Insert Delete GetRandom O(1)
- Medium
- Array, Hash Table, Design
- Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
"""


# Solution 1: Hash Table
# Time: O(1) | Space: O(N)
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d.keys():
            return False
        self.d[val] = 1
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d.keys():
            return False
        del self.d[val]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand = random.randint(0, self.size-1)
        return list(self.d)[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()
        self.st = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dic:
            self.dic[val] = len(self.st)
            self.st.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            last_el = self.st[-1]
            idx = self.dic[val]
            self.st[idx]  = last_el
            self.dic[last_el] = idx
            self.st.pop()
            del self.dic[val]
            return True
        return False
            
            
            

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.st)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
