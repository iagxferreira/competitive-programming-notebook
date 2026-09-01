import java.util.*;

class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        var leftDepth = maxDepth(root.left);
        var rightDepth = maxDepth(root.right);
        return 1 + Math.max(leftDepth, rightDepth);
    }
}

// LeetCode provides this. Kept here so the file compiles locally.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}
