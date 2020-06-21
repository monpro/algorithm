package designs;

import java.util.*;

class Node {
    Node prev, next;
    int key, value;

    public Node(int key, int value){
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    Node head = new Node(-1, -1);
    Node tail = new Node(-1, -1);
    Map<Integer, Node> map = new HashMap<>();
    int capacity = 0;
    int size = 0;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            Node node = map.get(key);
            remove(node);
            insert(node);
            return node.value;
        }else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            remove(map.get(key));
        }
        if(size == capacity){
            remove(tail.prev);
        }
        insert(new Node(key, value));
    }
    
    private void remove(Node node){
        map.remove(node.key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
        size -= 1;
    }
    
    private void insert(Node node){
        map.put(node.key, node);
        Node headNext = head.next;
        head.next = node;
        node.prev = head;
        headNext.prev = node;
        node.next = headNext;
        size += 1;
    }
}
