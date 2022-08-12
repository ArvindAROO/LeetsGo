# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return
        self.sol.append(root.val)
        self.helper(root.left)
        self.helper(root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.sol = []
        self.helper(root)
        return self.sol