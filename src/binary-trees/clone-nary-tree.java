import java.util.*;

class Node {
    public int val;
    public List<Node> children;

    
    public Node() {
        children = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        children = new ArrayList<Node>();
    }
    
    public Node(int _val,ArrayList<Node> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
    public Node cloneTree(Node root) {
        if(root == null){
            return null;
        }
        Node newRoot = new Node(root.val);
        
        for(Node node: root.children){
            newRoot.children.add(cloneTree(node));
        }
        
        return newRoot;
    }
}