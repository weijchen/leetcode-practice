"""
33. Search in Rotated Sorted Array
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
- 當中點非搜索值時，對單側而言可能的情況只會有兩種，sorted and non-sorted，將圖畫出來後針對兩個 case 寫判斷式
"""


# One-pass Binary Search
# Time: O(logN) | Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l - r) // 2 + r
            if nums[mid] == target:
                return True
            # 以下為兩個情況時各自的判斷式
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # in sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # in non-sorted
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # non-sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                # sorted
                else:
                    r = mid - 1
        return False
