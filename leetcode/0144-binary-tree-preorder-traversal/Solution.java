import java.util.*;

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode current = root;
        while(current != null || !stack.isEmpty()){
            if(current != null){
                stack.push(current);
                result.add(current.val);
                current = current.left;
            }else{
                TreeNode node = stack.pop();
                current = node.right;
            }
        }
        return result;
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
