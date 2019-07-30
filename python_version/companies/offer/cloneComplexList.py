class RandomListNode:
    def __init__(self,x):
        self.label = x
        self.next = None
        self.random = None

    def Clone(self, pHead):
        if not pHead:
            return None
        newHead = RandomListNode(pHead.label)
        dummy = RandomListNode(-1)
        dummy.next = pHead
        next_map = {}
        random_map = {}
        while pHead:
            next_map[pHead] = pHead.next
            random_map[pHead] = pHead.random
            pHead = pHead.next

        pHead = dummy.next
        dummy_two = RandomListNode(-1)
        dummy_two.next = newHead
        while pHead:
            if pHead.next:
                newHead.next = RandomListNode(next_map[pHead].label)
            if pHead.random:
                newHead.random = RandomListNode(random_map[pHead].label)
            pHead = pHead.next
            newHead = newHead.next
        return dummy_two.next

    def CloneWithoutExtraSpace(self, pHead):
        if not pHead:
            return None

        # insert nextnode
        dummy = RandomListNode(-1)
        dummy.next = pHead

        while pHead:
            pHeadClone = RandomListNode(pHead.label)
            pHeadClone.next = pHead.next
            pHead.next = pHeadClone
            pHead = pHeadClone.next

        # insert randomNode
        pHead = dummy.next
        while pHead:
            pHeadClone = pHead.next
            if pHead.random:
                pHeadClone.random = pHead.random.next
            pHead = pHeadClone.next

        #split node
        pHead = dummy.next

        pHeadClone = pHead.next
        currNode = pHead
        while currNode.next:
            tmp = currNode.next
            currNode.next = tmp.next
            currNode = tmp
        return pHeadClone