import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, n):
        # print(n, root.val, self.maps)
        if (n + 1) not in self.maps:
            self.maps[n + 1] = float('-inf')
        self.maps[n] = max(self.maps[n], root.val)

        if root.left:
            self.traverse(root.left, n + 1)
        if root.right:
            self.traverse(root.right, n + 1)
        
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.maps = {0: float('-inf')}
        self.traverse(root, 0)
        # print(self.maps)
        return list(self.maps.values())[:-1]