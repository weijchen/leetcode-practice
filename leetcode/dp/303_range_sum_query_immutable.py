"""
303. Range Sum Query - Immutable
- Easy
- DP
- Link: https://leetcode.com/problems/range-sum-query-immutable/
- 解題: 如果用 brute force 的方式，時間複雜度為 O(M*N)，M 為 sumRange() 執行次數，N 為 length of nums
        該題希望能把 sumRange() 的時間複雜度改為 O(1)
"""


# Solution 1: DP
# Time: O(M) | Space: O(M)
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            self.arr[i] = nums[i-1] + self.arr[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
