"""
Three Number Sort
- Medium
- Bucket sort
"""


# Time: O(n) | Space: O(1)
def threeNumberSort(array, order):
    # Write your code here.
    b1, b2, b3 = 0, 0, 0
    for e in array:
        if e == order[0]:
            b1 += 1
        elif e == order[1]:
            b2 += 1
        else:
            b3 += 1

    for i in range(len(array)):
        if b1 > 0:
            array[i] = order[0]
            b1 -= 1
        else:
            if b2 > 0:
                array[i] = order[1]
                b2 -= 1
            else:
                if b3 > 0:
                    array[i] = order[2]
                    b3 -= 1
    return array
