"""
136. Single Number
- Easy
- Hash Table Bit Manipulation
- Link: https://leetcode.com/problems/single-number/
"""


"""
Solution 1: Hash Table
Time: O(n) | Space: O(n)
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ht = {}
        for num in nums:
            if num in ht:
                del ht[num]
            else:
                ht[num] = num

        return list(ht.keys())[0]


"""
Solution 2: Bit Manipulation
a XOR 0 = a
a XOR a = 0
a XOR b XOR = a XOR a XOR b = 0 XOR b = b
Time: O(n) | Space: O(1)
"""


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
