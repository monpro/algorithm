package Linked_List_Array;

import java.util.HashMap;
import java.util.Map;

public class linked_list_cycle {
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        Map<ListNode, Boolean> map = new HashMap<>();
        ListNode cur = head;
        while(cur.next != null){
            map.put(cur,true);
            if(map.containsKey(cur.next)){
                return true;
            }
            cur = cur.next;
        }
        return false;
    }
}
