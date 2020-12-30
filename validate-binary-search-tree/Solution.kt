/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun isNodeValid(root: TreeNode?, low: Int?, high: Int?): Boolean {
        if(root == null) return true;
        
        if((low != null && low >= root.`val`) || (high != null && high <= root.`val`)) return false;
        
        return isNodeValid(root.left, low, root.`val`) && isNodeValid(root.right, root.`val`, high);
    }
    
    fun isValidBST(root: TreeNode?): Boolean {
        return isNodeValid(root, null, null);
    }
}
