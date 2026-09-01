import java.util.*;

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode current = root;
        while(current != null || !stack.isEmpty()){
            if(current != null){
                result.add(current.val);
                stack.push(current);
                current = current.right;
            }else{
                current = stack.pop();
                current = current.left;
            }
        }
        Collections.reverse(result);
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
