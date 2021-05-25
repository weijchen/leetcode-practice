#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
# Solution 1: Math
# Time: O(N) | Space: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        numOfZero = 0
        for i in range(1, n + 1):
            n = i
            while n % 50 == 0 or n % 10 == 0 or n % 5 == 0:
                if n % 50 == 0:
                    n //= 50
                    numOfZero += 2
                if n % 10 == 0:
                    n //= 10
                    numOfZero += 1
                if n % 5 == 0:
                    n //= 5
                    numOfZero += 1
                
        return numOfZero
    # @lc code=end

# Solution 2: Math, with efficient Factor of 5 Counting
# Time: O(logN) | Space: O(1)
# 當下的數字大於 "當下的 5 的倍數"時，更新"當下的 5 的倍數"，來加快計算
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        current_multiple = 5
        while n >= current_multiple:
            zero_count += n // current_multiple
            current_multiple *= 5
        return zero_count
