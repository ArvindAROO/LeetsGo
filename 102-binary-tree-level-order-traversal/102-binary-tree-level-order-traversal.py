# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, n):
        if not root:
            return
        if n in self.res:
            self.res[n].append(root.val)
        else:
            self.res[n] = [root.val]
        self.helper(root.left, n + 1)
        self.helper(root.right, n + 1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = {}
        self.helper(root, 0)
        res = []
        for i in self.res:
            res.append(self.res[i])
        return res