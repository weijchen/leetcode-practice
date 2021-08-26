"""
735. Asteroid Collision
- Medium
- Array, Stack
- Link: https://leetcode.com/problems/asteroid-collision/
"""


# Solution 1: Stack
# Time: O(N) | Space: O(N)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = [asteroids[0]]

        for ast in asteroids[1:]:
            if len(st) == 0:
                st.append(ast)
            else:
                prev = st[-1]

                if prev < 0:
                    st.append(ast)
                elif prev > 0 and ast > 0:
                    st.append(ast)
                elif prev > 0 and ast < 0:
                    # the same
                    if prev == abs(ast):
                        st.pop()
                        continue

                    # incoming crash previous
                    while len(st) > 0 and st[-1] < abs(ast) and st[-1] > 0:
                        st.pop()

                    if len(st) == 0:
                        st.append(ast)
                        continue

                    if st[-1] == abs(ast):
                        st.pop()
                    elif st[-1] < 0:
                        st.append(ast)

        return st


# Solution 2: Stack (cleaner)
# Time: O(N) | Space: O(N)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids:
            while st and ast < 0 < st[-1]:
                if st[-1] < -ast:
                    st.pop()
                    continue
                elif st[-1] == -ast:
                    st.pop()
                break
            else:
                st.append(ast)
        return st
