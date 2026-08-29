import java.util.*;

class Solution {
    public final TreeNode getTargetCopy(final TreeNode original,
                                        final TreeNode cloned,
                                        final TreeNode target) {
        if(original == null || original == target) return cloned;
        var res = getTargetCopy(original.left, cloned.left, target);
        if(res == null) return getTargetCopy(original.right, cloned.right, target);
        return res;
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
