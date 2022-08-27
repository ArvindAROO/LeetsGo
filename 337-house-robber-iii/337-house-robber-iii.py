# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def toBeOrNotToBe(self, root):
        if not root:
            return [0,0]
        left_side = self.toBeOrNotToBe(root.left)
        right_side = self.toBeOrNotToBe(root.right)
        
        toBe = root.val + left_side[1] + right_side[1]
        notToBe = max(left_side) + max(right_side)
        
        return [toBe, notToBe]
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.toBeOrNotToBe(root))
        