import java.util.*;

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null) return null;
        Node copy = new Node(node.val);
        Node[] visited = new Node[101];
        Arrays.fill(visited,null);
        dfs(node, copy, visited);
        return copy;
    }

    public void dfs(Node node, Node copy, Node[] visited){
        visited[copy.val] = copy;
        for(Node n : node.neighbors){
            if(visited[n.val] != null){
                copy.neighbors.add(visited[n.val]);
            }else{
                var dummy = new Node(n.val);
                copy.neighbors.add(dummy);
                dfs(n, dummy, visited);
            }
        }
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
