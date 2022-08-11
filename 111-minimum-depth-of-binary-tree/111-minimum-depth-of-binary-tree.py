# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, depth):
        if not root:
            return
        print(root.val)
        if not root.left and not root.right:
            if depth < self.min:
                self.min = depth
                return
        if root.left:
            self.dfs(root.left, depth + 1)
            
        if root.right:
            self.dfs(root.right, depth + 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min = 10000000
        if not root:
            return 0
        self.dfs(root, 1)
        return self.min