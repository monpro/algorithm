class Solution(object):
    """
    """
    def copyRandomList(self, head):
        dic, prev, node = {}, None, head
        while node:
            if node not in dic:
                # Use a dictionary to map the original node to its copy
                dic[node] = Node(node.val, node.next, node.random)
            if prev:
                # Make the previous node point to the copy instead of the original.
                prev.next = dic[node]
            else:
                # If there is no prev, then we are at the head. Store it to return later.
                head = dic[node]
            if node.random:
                if node.random not in dic:
                    # If node.random points to a node that we have not yet encountered, store it in the dictionary.
                    dic[node.random] = Node(node.random.val, node.random.next, node.random.random)
                # Make the copy's random property point to the copy instead of the original.
                dic[node].random = dic[node.random]
            # Store prev and advance to the next node.
            prev, node = dic[node], node.next
        return head