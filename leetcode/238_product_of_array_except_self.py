"""
238. Product of Array Except Self
- Medium
- Array
- Link: https://leetcode.com/problems/product-of-array-except-self/
"""


# Solution 1: left and right product
# Time: O(N) | Space: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [0] * len(nums)
        product_right = [0] * len(nums)

        cur = 1
        for i in range(len(nums)):
            if i == 0:
                product_left[i] = cur
            else:
                cur *= nums[i-1]
                product_left[i] = cur

        cur = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                product_right[i] = cur
            else:
                cur *= nums[i+1]
                product_right[i] = cur

        ans = [product_left[i] * product_right[i] for i in range(len(nums))]
        return ans


# Solution 2 (optimized): left and right product, while using output array as left/right product
# Time: O(N) | Space: O(1), since we do not consider output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        cur = 1
        for i in range(len(nums)):
            if i == 0:
                ans[i] = cur
            else:
                cur *= nums[i-1]
                ans[i] = cur

        cur = 1
        for i in reversed(range(len(nums))):
            ans[i] *= cur
            cur *= nums[i]

        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        answer = [0]*length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
