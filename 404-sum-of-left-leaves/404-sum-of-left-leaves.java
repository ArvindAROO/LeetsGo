/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum;
    public void dfs(TreeNode root, boolean isleft){
        if (root == null)
            return;
        if (isleft && root.left == null && root.right == null)
            this.sum += root.val;
        if (root.left != null)
            dfs(root.left, true);
        if (root.right != null)
            dfs(root.right, false);
    }
    
    public int sumOfLeftLeaves(TreeNode root) {
        this.sum = 0;
        if (root != null)
            dfs(root, false);
        return this.sum;
    }
}