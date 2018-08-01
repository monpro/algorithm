package Linked_List_Array;

import java.util.HashMap;
import java.util.Map;

public class copy_list_with_random_pointer {
    public RandomListNode copyRandomList(RandomListNode head) {
        if(head == null){
            return head;
        }

        RandomListNode p = head;
        while(p != null){
            RandomListNode node = new RandomListNode(p.label);
            node.next = p.next;
            p.next = node;
            p = p.next.next;
        }
        // p = head; p是head的别名 你怎么操作p，仍然可以通过head找到原位置，想想指针
        p = head;

        while(p!= null){
            if(p.random != null){
                p.next.random = p.random.next;
            }
            p = p.next.next;
        }
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode tail = dummy;
        p = head;
        while (p != null){
            RandomListNode copynode = p.next;
            p.next = copynode.next;
            tail.next = copynode;
            tail = copynode;
            p = p.next;

        }
        return dummy.next;
   }

   public RandomListNode copyWithHashMap(RandomListNode head){
        if(head == null){
            return head;
        }
        Map<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode cur = head;
        while (cur != null){
            map.put(cur, new RandomListNode(cur.label));
            cur = cur.next;
        }
        cur = head;
        while (cur != null){
            map.get(cur).next = map.get(cur.next);
            map.get(cur).random = map.get(cur.random);
            cur = cur.next;
        }

        return map.get(head);
   }
}
