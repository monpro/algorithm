class Node:
    def __init__(self, key, val, prev=None, next=None, group=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freqGroup = group


class FreqGroup:
    def __init__(self, freq, head=None, tail=None, prev=None, next=None):
        self.freq = freq
        self.head = head
        self.tail = tail
        self.prev = prev
        self.next = next


class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.freqGroupTail = None
        self.freqMap = {}

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        if key in self.freqMap:
            node = self.freqMap[key]
            node.val = value
            self.moveUp(node)

        else:
            if len(self.freqMap) == self.capacity:
                del self.freqMap[self.freqGroupTail.tail.key]
                self.removeNode(self.freqGroupTail.tail)

            # check and init freqGroup of 0
            if self.freqGroupTail is None or self.freqGroupTail.freq > 0:
                newGroup = FreqGroup(0, prev=self.freqGroupTail)
                if self.freqGroupTail is not None:
                    self.freqGroupTail.next = newGroup
                self.freqGroupTail = newGroup

            # insert node to freqGroupTail.head
            newNode = Node(key, value, group=self.freqGroupTail)
            if self.freqGroupTail.head is not None:
                newNode.next = self.freqGroupTail.head
                self.freqGroupTail.head.prev = newNode
            self.freqGroupTail.head = newNode

            # check and assign tail
            if self.freqGroupTail.tail is None:
                self.freqGroupTail.tail = newNode

            # put node to map
            self.freqMap[key] = newNode

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        if key not in self.freqMap:
            return -1

        node = self.freqMap[key]
        self.moveUp(node)
        return node.val

    def moveUp(self, node):
        originGroup = node.freqGroup
        newGroup = originGroup.prev

        # check and create prev group if necessary
        if newGroup is None or newGroup.freq != originGroup.freq + 1:
            newGroup = FreqGroup(freq=originGroup.freq + 1, \
                                 prev=originGroup.prev, \
                                 next=originGroup)

            if originGroup.prev is not None:
                originGroup.prev.next = newGroup
            originGroup.prev = newGroup

        # remove node
        self.removeNode(node)

        # add to new group and to head
        node.freqGroup = newGroup
        node.next = newGroup.head
        if newGroup.head is not None:
            newGroup.head.prev = node
        newGroup.head = node

        # check for tail
        if newGroup.tail is None:
            newGroup.tail = node

    def removeNode(self, node):
        # one node only, remove the group
        if node.freqGroup.tail is node.freqGroup.head:
            self.removeGroup(node.freqGroup)
            return

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        if node.freqGroup.head is node:
            node.freqGroup.head = node.next
        if node.freqGroup.tail is node:
            node.freqGroup.tail = node.prev

        node.freqGroup = None
        node.prev = None
        node.next = None

    def removeGroup(self, group):
        if group.prev is not None:
            group.prev.next = group.next
        if group.next is not None:
            group.next.prev = group.prev
        if self.freqGroupTail is group:
            self.freqGroupTail = group.prev