"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self, root, order):
        for i in root.children:
            self.dfs(i, order + 1)
        if order not in self.maps:
            self.maps[order] = [root.val]
            return
        self.maps[order].append(root.val)
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.maps = {}
        if root:
            self.dfs(root, 0)
            
        return [self.maps[i] for i in sorted(list(self.maps.keys()))]