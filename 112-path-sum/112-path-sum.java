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
    boolean sol = false;
    int target;
    public void dfs(TreeNode root, int sumSoFar){

        if(root == null) return;
        // System.out.println(root.val + " " + sumSoFar);
        if ((root.val + sumSoFar == this.target) && (root.left == null) && (root.right == null)) {
            this.sol = true;
            return;
        }
        if(root.left != null)
            dfs(root.left, root.val + sumSoFar);
        if (root.right != null)
            dfs(root.right, root.val + sumSoFar);
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        this.sol = sol;
        this.target = targetSum;
        dfs(root, 0);
        return this.sol;
    }
}