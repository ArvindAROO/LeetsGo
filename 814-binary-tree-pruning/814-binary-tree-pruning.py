# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def containsOne(self, root):
        if root.left and root.right:
            return any([self.containsOne(root.left), self.containsOne(root.right), root.val == 1])
        if root.left:
            return any([self.containsOne(root.left), root.val == 1])
        if root.right:
            return any([self.containsOne(root.right), root.val == 1])
        return root.val == 1
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root.left:
            self.pruneTree(root.left)
            if not self.containsOne(root.left):
                root.left = None
        if root.right:
            self.pruneTree(root.right)
            if not self.containsOne(root.right):
                root.right = None
        if not root.left and not root.right:
            return None if root.val == 0 else root
        
        return root