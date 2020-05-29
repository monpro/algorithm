package history.heap;

import java.util.*;

class ListNode {
  int value;
  ListNode next;

  ListNode(int value) {
    this.value = value;
  }
}

class MergeKSortedLists {

  public static ListNode merge(ListNode[] lists) {
    if(lists.length == 0){
        return null;
    }
    PriorityQueue<ListNode> minHeap = new PriorityQueue<>((n1, n2) -> n1.value - n2.value);
    for(ListNode node: lists){
        if(node != null){
            minHeap.add(node);
        }
    }
    ListNode head = null, tail = null;
    ListNode node = null;
    while(!minHeap.isEmpty()){
      node = minHeap.poll();
      if(head == null && tail == null){
        head = node;
        tail = node;
      }else{
        tail.next = node;
        tail = tail.next;
      }
      if(node.next != null){
        minHeap.add(node.next);
      }
    }

    return head;
  }

  public static void main(String[] args) {
    ListNode l1 = new ListNode(2);
    l1.next = new ListNode(6);
    l1.next.next = new ListNode(8);

    ListNode l2 = new ListNode(3);
    l2.next = new ListNode(6);
    l2.next.next = new ListNode(7);

    ListNode l3 = new ListNode(1);
    l3.next = new ListNode(3);
    l3.next.next = new ListNode(4);

    ListNode result = MergeKSortedLists.merge(new ListNode[] { l1, l2, l3 });
    System.out.print("Here are the elements form the merged list: ");
    while (result != null) {
      System.out.print(result.value + " ");
      result = result.next;
    }
  }
}
