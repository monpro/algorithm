import heapq
from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists, start, end):
        if start == end:
            return lists[start]

        if start < end:
            mid = (start + end) // 2
            l1 = self.partition(lists, start, mid)
            l2 = self.partition(lists, mid + 1, end)
            return self.merge(l1, l2)
        else:
            return None

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

    def mergeKListsHeap(self, lists):
        result, heap = [], []
        for list in lists:
            while list:
                heapq.heappush(heap, list.val)
                list = list.next

        while heap:
            result.append(heapq.heappop(heap))
        return result

    def mergeKListsPriorityQueue(self, lists):
        dummy = ListNode(None)
        current = dummy
        queue = PriorityQueue()
        for index,node in enumerate(lists):
            if node:
                queue.put((node.val, index, node))
        while not queue.empty():
            _, index, next_node = queue.get()
            current.next = next_node
            current = current.next
            if current.next:
                queue.put((current.next.val, index, current.next))
        return dummy.next
