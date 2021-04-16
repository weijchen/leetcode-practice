"""
33. Search in Rotated Sorted Array
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


# One-pass Binary Search
# Time: O(logN) | Space: O(1)
# ***Think simple***
# 當中點非搜索值時，對單側而言可能的情況只會有兩種，sorted and non-sorted，將圖畫出來後針對兩個 case 寫判斷式
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(nums, lo, hi, target):
            found = -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] == target:
                    return mid
                # 以下為兩個情況時各自的判斷式
                elif nums[mid] >= nums[lo]: # sorted
                    if nums[lo] <= target and nums[mid] > target: # in sorted
                        hi = mid - 1
                    else: # in non-sorted
                        lo = mid + 1
                else: # non-sorted
                    if nums[mid] < target and nums[hi] >= target: # in non-sorted
                        lo = mid + 1
                    else: # sorted
                        hi = mid - 1

            return found

        return binarySearch(nums, 0, len(nums) - 1, target)
