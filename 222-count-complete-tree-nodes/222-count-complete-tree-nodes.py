# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.count += 1
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        return self.count