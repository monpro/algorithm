
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution {
    public Node copyRandomList(Node head) {
        if(head == null)
            return null;
        Node cur = head, nextNode = null;
        
        //list becomes: origin - copy - origin - copy - origin - copy
        while(cur != null){
            nextNode = cur.next;
            cur.next = new Node(cur.val);
            cur.next.next = nextNode;
            cur = nextNode;
        }
        //assign copyNode random pointer
        cur = head;
        while(cur != null){
            if(cur.random != null){
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }
        
        cur = head;
        Node copyHead = cur.next;
        
        //restore node
        while(cur != null){
            nextNode = cur.next.next;
            Node copyNode = cur.next;
            cur.next = nextNode;
            if(nextNode != null)
                copyNode.next = nextNode.next;
            cur = nextNode;
        }
        
        return copyHead;
        
    }
}