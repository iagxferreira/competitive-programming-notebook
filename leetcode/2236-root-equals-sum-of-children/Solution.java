import java.util.*;

class Solution {
    public boolean checkTree(TreeNode root) {
        return root.val == root.right.val + root.left.val;
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
