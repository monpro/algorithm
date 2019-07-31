from utils.Node import RandomListNode

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        # copy the next and random and the label
        if head is None:
            return None
        myMap = {}
        new_head = RandomListNode(head.label)
        myMap[head] = new_head
        n1 = head
        n2 = new_head

        # copy neighboor
        # use hashmap to avoid dependencies already existed
        while n1 is not None:
            n2.random = n1.random

            if n1.next is not None:
                n2.next = RandomListNode(n1.next.label)
                myMap[n1.next] = n2.next

            else:
                n2.next = None

            n1 = n1.next
            n2 = n2.next

        # deep copy Random

        copy_random_node = new_head

        while copy_random_node is not None:
            if copy_random_node.random is not None:
                copy_random_node.random = myMap[copy_random_node.random]

            copy_random_node = copy_random_node.next

        return new_head
