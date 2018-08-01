"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        # copy the next and random and the label
        if head == None:
            return None

        myMap = {}
        new_head = RandomListNode(head.label)

        myMap[head] = new_head

        n1 = head
        n2 = new_head

        # copy neighboor
        # use hashmap to avoid dependencies already existed
        while n1 != None:
            n2.random = n1.random

            if n1.next != None:
                n2.next = RandomListNode(n1.next.label)
                myMap[n1.next] = n2.next

            else:
                n2.next = None

            n1 = n1.next
            n2 = n2.next

        # deep copy Random

        copy_random_node = new_head

        while copy_random_node != None:
            if copy_random_node.random != None:
                copy_random_node.random = myMap[copy_random_node.random]

            copy_random_node = copy_random_node.next

        return new_head
