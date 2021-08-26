"""
937. Reorder Data in Log Files
- Easy
- Array, String, Sorting
- Link: https://leetcode.com/problems/reorder-data-in-log-files/
"""


# Solution 1: Sorting
# Time: O(MN logN) | Space: O(MN), where M is the maximum length of a single log
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [], []
        for log in logs:
            _id, content = log.split(' ')[0], log.split(' ')[1:]
            if content[0][0] in '0123456789':
                dig.append(log)
            else:
                let.append((_id, content))
        let.sort(key=lambda x: (x[1], x[0]))
        let_post = []
        for _id, content in let:
            out = _id + ' ' + ' '.join(content)
            let_post.append(out)
        return let_post + dig


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def getKey(x):
            words = x.split(' ')
            identifier = words[0]
            logtype = words[1:]

            if 'a' <= logtype[0][0] <= 'z':
                return (0, logtype, identifier)
            return (1, )
        logs.sort(key=lambda x: getKey(x))
        return logs
