"""
Quick Sort
- Medium
"""


# Time: O(nlog(n)) | Space: O(log(n))
def quickSort(array):
    # Write your code here.
    quickSortHelper(array, 0, len(array) - 1)

    return array


def quickSortHelper(array, start, end):
    if (start > end):
        return
    pivot = start
    l = start+1
    r = end

    while r >= l:
        if array[r] < array[pivot] and array[l] > array[pivot]:
            swap(array, l, r)
        if array[r] >= array[pivot]:
            r -= 1
        if array[l] <= array[pivot]:
            l += 1

    swap(array, pivot, r)
    quickSortHelper(array, start, r-1)
    quickSortHelper(array, r+1, end)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
