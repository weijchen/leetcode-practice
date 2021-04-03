"""
Smallest Difference
- Medium
- Array, Two Pointers
"""


# Solution 1
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    p1 = 0
    p2 = 0
    tmpSmallest = abs(arrayOne[p1] - arrayTwo[p2])
    curPair = [arrayOne[p1], arrayTwo[p2]]

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        diffOne, diffTwo = float('inf'), float('inf')
        if p1 + 1 < len(arrayOne):
            diffOne = abs(arrayOne[p1+1] - arrayTwo[p2])
        if p2 + 1 < len(arrayTwo):
            diffTwo = abs(arrayOne[p1] - arrayTwo[p2+1])

        if diffOne < diffTwo:
            p1 += 1
            if tmpSmallest > abs(arrayOne[p1] - arrayTwo[p2]):
                tmpSmallest = abs(arrayOne[p1] - arrayTwo[p2])
                curPair = [arrayOne[p1], arrayTwo[p2]]
        elif diffOne > diffTwo:
            p2 += 1
            if tmpSmallest > abs(arrayOne[p1] - arrayTwo[p2]):
                tmpSmallest = abs(arrayOne[p1] - arrayTwo[p2])
                curPair = [arrayOne[p1], arrayTwo[p2]]
        else:
            return curPair

    return curPair


# Solution 2: 解題思路 -> 找出差距最小的兩個數字，將兩列表做 sorting，依序比較兩邊的大小，每次比較對兩數進行比較，移動小數的位置，直到兩數越接近越好
# Time: O(mlogm + nlogn) -> for sorting algo | Space: O(1)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    p1, p2 = 0, 0
    curDiff = float('inf')
    ret = []

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        num1 = arrayOne[p1]
        num2 = arrayTwo[p2]
        if num1 < num2:
            tmpDiff = abs(num1 - num2)
            p1 += 1
        elif num1 > num2:
            tmpDiff = abs(num1 - num2)
            p2 += 1
        else:
            return [num1, num2]
        if tmpDiff < curDiff:
            curDiff = tmpDiff
            ret = [num1, num2]
    return ret
