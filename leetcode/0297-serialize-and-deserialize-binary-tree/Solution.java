import java.util.*;

class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        // TODO: solve
        return null;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        // TODO: solve
        return null;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

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
