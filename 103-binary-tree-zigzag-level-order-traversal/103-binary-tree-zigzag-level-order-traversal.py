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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = {}
        self.helper(root, 0)
        res = []
        flag = True
        for i in self.res:
            if flag:
                res.append(self.res[i])
            else:
                res.append(self.res[i][::-1])
            flag = not flag
        return res