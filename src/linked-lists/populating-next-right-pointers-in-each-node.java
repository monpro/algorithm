class Solution {
    public Node connect(Node root) {
        if(root == null){
            return null;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        Node prev = null;
        Node node = null;
        while(!queue.isEmpty()){
            int size = queue.size();
            prev = null;
            for(int i = 0; i < size; i++){
                node = queue.poll();
                if(prev != null){
                    prev.next = node;
                }   
                prev = node;
                
                if(node.left != null){
                    queue.offer(node.left);
                }
                if(node.right != null){
                    queue.offer(node.right);
                }
            }
        }
        return root;
    }
}