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
    public boolean isNodeValid(TreeNode root, Integer low, Integer high) {
        if(root == null) return true;
        
        if((low != null && low >= root.val) || (high != null && high <= root.val)) return false;
        
        return isNodeValid(root.left, low, root.val) && isNodeValid(root.right, root.val, high);
    }
    
    public boolean isValidBST(TreeNode root) {
        return isNodeValid(root, null, null);
    }
}
