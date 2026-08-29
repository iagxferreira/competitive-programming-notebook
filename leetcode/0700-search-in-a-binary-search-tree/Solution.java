import java.util.*;

class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if(root == null) return null;
        if(val > root.val) return searchBST(root.right, val);
        if (val < root.val) return searchBST(root.left, val);
        return root;
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
