"""
66. Plus One
- Easy
- Array
- Link: https://leetcode.com/problems/plus-one/
"""


# Time: O(n) | Space: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        curPos = len(digits) - 1

        while carry:
            if curPos == -1:
                digits.insert(0, 1)
                carry = 0
                break
            if digits[curPos] + carry < 10:
                carry = 0
                digits[curPos] += 1
            else:
                digits[curPos] = 0
                curPos -= 1

        return digits
