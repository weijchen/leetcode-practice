# entire string
def isPalindrome(s):
  n = len(s)
  for i in range(n // 2 + 1):
    if s[i] !=  s[n - i - 1]: return False
  return True

# substring s[l~r]
def isPalindrome(s, l, r):
  while l < r:
    if s[l] != s[r]: return False
    l += 1
    r -= 1
  return True
