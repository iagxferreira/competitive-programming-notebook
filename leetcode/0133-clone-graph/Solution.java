import java.util.*;

class Solution {
    public Node cloneGraph(Node node) {
        // TODO: solve
        return null;
    }
}

// LeetCode provides this. Kept here so the file compiles locally.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() { this.val = 0; this.neighbors = new ArrayList<>(); }
    public Node(int val) { this.val = val; this.neighbors = new ArrayList<>(); }
    public Node(int val, ArrayList<Node> neighbors) {
        this.val = val; this.neighbors = neighbors;
    }
}
