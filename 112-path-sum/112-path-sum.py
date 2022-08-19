# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, sumTillNow):
        # print(sumTillNow, root.val)
        if not root:
            return
        if root.val + sumTillNow == self.target and root.left == root.right == None:
            self.sol = True
            return
        if root.left:
            self.dfs(root.left, sumTillNow + root.val)
        if root.right:
            self.dfs(root.right, sumTillNow + root.val)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target = targetSum
        self.sol = False
        if not root:
            return False
        self.dfs(root, 0)
        return self.sol