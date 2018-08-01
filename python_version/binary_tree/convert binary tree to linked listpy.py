"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []
        result, queue = [],[]
        out_put_result = []
        queue.append(root)
        
        while queue != []:
            mid_result = []
            result.append([i.val for i in queue])
            for i in queue:
                if i.left is not None and i.left != '#':
                    mid_result.append(i.left)
                if i.right is not None and i.right != '#':
                    mid_result.append(i.right)
            
            queue = mid_result
            
        print(result)
        for arr in result:
            if len(arr) == 1:
                print(True)
                head = ListNode(arr[0])

                out_put_result.append(head)
            else:
                dummy = ListNode(-1)
                
                for i in range(len(arr) - 1):
                    if i == 0:
                        head = ListNode(arr[i])
                        dummy.next = head
                        next_node = ListNode(arr[i + 1])
                        head.next = next_node
                    else:
                        head = next_node
                        next_node = ListNode(arr[i + 1])
                        head.next = next_node
                

                out_put_result.append(dummy.next)
                        
                    
                
            
        return out_put_result
        
