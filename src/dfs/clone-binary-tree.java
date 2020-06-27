package dfs;

import java.util.*;

class Node {
    int val;
    Node left;
    Node right;
    Node random;
    Node() {}
    Node(int val) { this.val = val; }
    Node(int val, Node left, Node right, Node random) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.random = random;
    }
  }

class Solution {
    Map<Node, Node> map = new HashMap<>();
    public Node copyRandomBinaryTree(Node root) {
        if(root == null){
            return null;
        }
        if(map.containsKey(root)){
            return map.get(root);
        }
        Node newNode = new Node(root.val);
        map.put(root, newNode);
        
        newNode.left = copyRandomBinaryTree(root.left);
        newNode.right = copyRandomBinaryTree(root.right);
        newNode.random = copyRandomBinaryTree(root.random);
        
        return newNode;
    }
    
}