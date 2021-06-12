"""
841. Keys and Rooms
- Medium
- DFS
- Link: https://leetcode.com/problems/keys-and-rooms/
"""


# Solution 1: DFS
# Time: O(N+E), where N is the number of rooms and E is the total number of keys | Space: O(N)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        st = [0]

        while st:
            roomId = st.pop()
            for nei in rooms[roomId]:
                if seen[nei] == False:
                    seen[nei] = True
                    st.append(nei)
        return all(seen)
