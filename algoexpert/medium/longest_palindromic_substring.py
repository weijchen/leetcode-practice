"""
Longest Palindromic Substring
- Medium
- String
"""


# Time: O(n^2) | Space: O(1)
def longestPalindromicSubstring(string):
    # Write your code here.
    longest = ""
    for i in range(0, len(string)):
        for j in range(i, len(string)):
            checkedString = string[i: j+1]
            if len(checkedString) > len(longest):
                if isPalindrome(checkedString):
                    longest = checkedString
    return longest


def isPalindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True
