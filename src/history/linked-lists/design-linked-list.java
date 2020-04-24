class MyLinkedList {
    
    private class Node{
        public int val;
        public Node next;

        public Node(int val, Node next){
            this.val = val;
            this.next = next;
        } 
    }
    
    private Node head;
    private int size;
    
    public MyLinkedList() {
        head = new Node(0, null);
        size = 0;
    }

    public int get(int index) {
        if(index < 0 || index >= size) return -1;
        Node prev = head.next;
        for(int i = 0; i < index; i++)
            prev = prev.next;
        return prev.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if(index < 0 || index > size) return;
        Node prev = head;
        for(int i = 0; i < index; i++)
            prev = prev.next;
        prev.next = new Node(val, prev.next);
        size += 1;
    }
    
    public void deleteAtIndex(int index) {
        if(index < 0 || index >= size) return;
        Node prev = head;
        for(int i = 0; i < index; i++)
            prev = prev.next;
        Node targetNode = prev.next;
        prev.next = targetNode.next;
        targetNode.next = null;
        size -= 1;
    }
}
