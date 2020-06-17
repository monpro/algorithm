import java.util.ArrayList;
import java.util.List;
import java.util.Map;

class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
class Solution {
    public Node cloneGraph(Node node) {
        if(node == null)
            return null;
        
        Map<Node, Node> map = new HashMap<>();
        Node head = new Node(node.val);
        map.put(node, head);
        dfs(map, node);
        
        return head;
    }
    
    public void dfs(Map<Node, Node> map, Node node){
        if(node == null)
            return;
        for(Node neighbor: node.neighbors){
            if(!map.containsKey(neighbor)){
                Node newNode = new Node(neighbor.val);
                map.put(neighbor, newNode);
                dfs(map, neighbor);
            }
            map.get(node).neighbors.add(map.get(neighbor));
        }
    }
}