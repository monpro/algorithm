package Linked_List_Array;

import bfs.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

public class convert_binary_search_tree_to_doubly_linked_list {
    public DoublyListNode bstToDoublyList(TreeNode root) {
        // write your code here
        //review 中序遍历
        if(root == null){
            return null;
        }
        DoublyListNode left = bstToDoublyList(root.left);
        DoublyListNode right = bstToDoublyList(root.right);

        DoublyListNode newNode = new DoublyListNode(root.val);
        if(left != null){
            while (left.next != null){
                left = left.next;
            }
            left.next = newNode;
            newNode.prev = left;
        }

        if(right !=null){
            while(right.prev != null){
                right = right.prev;
            }
            newNode.next = right;
            right.prev = newNode;
        }
        while (newNode.prev != null){
            newNode = newNode.prev;
        }

        return newNode;


    }
    public DoublyListNode bstToDoublyListWithModel(TreeNode root){
        Queue<Integer> queue = new LinkedList<>();
        //先通过中序遍历 将node放在queue里
        in_traverse(queue,root);
        DoublyListNode dummy = new DoublyListNode(0);
        DoublyListNode curr = dummy;
        //然后利用queue先进先出的特性，构建doublelinkedlist
        while (!queue.isEmpty()){
            DoublyListNode next = new DoublyListNode(queue.poll());
            curr.next = next;
            next.prev = curr;
            curr = next;

        }
        //最后别忘 把 headnode和 dummynode的联系切断
        if(dummy.next != null){
            dummy.next.prev = null;
        }
        return dummy.next;
    }

    private void in_traverse(Queue<Integer> queue, TreeNode root){
        if(root == null){
            return;
        }
        in_traverse(queue,root.left);
        queue.add(root.val);
        in_traverse(queue,root.right);
    }


}
