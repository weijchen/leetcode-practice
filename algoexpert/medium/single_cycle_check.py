"""
Smallest Difference
- Medium
"""


# Solution 1: 解題思路 -> 記錄所有走過的 index，當出現走到重複 index 時，1. 計算已走過的 index 數量是否等同 array 長度，以及 2. 是否走回原點 / 需要額外處理迴圈的情形
# Time: O(n) | Space: O(n)
def hasSingleCycle(array):
    # Write your code here.
    numOfEl = len(array)
    curInd = 0
    passedSet = {}

    while curInd not in passedSet.keys():
        passedSet[curInd] = True

        curInd += array[curInd]
        if curInd < 0:
            curInd += numOfEl
        curInd %= numOfEl

    return len(passedSet.keys()) == numOfEl and curInd == 0
