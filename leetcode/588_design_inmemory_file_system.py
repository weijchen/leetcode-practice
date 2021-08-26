"""
588. Design In-Memory File System
- Hard
- Hash Table, String, Design, Trie
- Link: https://leetcode.com/problems/design-in-memory-file-system/
"""


# Solution 1: Two HashTable
# Time: O() | Space: O()
class FileSystem:
    def __init__(self):
        self.system = {"/": set()}
        self.files = dict()

    def ls(self, path: str) -> List[str]:
        fileName = path.split('/')[-1]
        if fileName in self.files:
            return [fileName]
        else:
            return sorted(self.system[path])

    def mkdir(self, path: str) -> None:
        if not path:
            return
        routes = path.split('/')
        curRoute = "/"

        if curRoute not in self.system:
            self.system[curRoute] = set()
        if len(routes) > 1:
            self.system[curRoute].add(routes[1])

        routes.pop(0)
        while routes:
            route, _next = routes.pop(0), routes[0] if routes else None
            curRoute = curRoute + "{}/".format(route)
            if curRoute[:-1] not in self.system:
                self.system[curRoute[:-1]] = set()
            if _next:
                self.system[curRoute[:-1]].add(_next)

    def addContentToFile(self, filePath: str, content: str) -> None:
        path, fileName = '/'.join(filePath.split('/')
                                  [:-1]),  filePath.split('/')[-1]
        path = path if path else "/"
        if path not in self.system:
            self.system[path] = set()
        if fileName not in self.files:
            self.files[fileName] = content
        else:
            self.files[fileName] += content
        self.system[path].add(fileName)

    def readContentFromFile(self, filePath: str) -> str:
        fileName = filePath.split('/')[-1]
        return self.files[fileName]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
