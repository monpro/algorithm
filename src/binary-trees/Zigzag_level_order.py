"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    time complexity is: O(n)
    space complexity is : O(1)
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        '''
        if root == None:
            return []
        result,queue,mid_result = [],[],[]
        # write your code here
        queue.append(root)
        left_to_right = False
        while queue != []:
            mid_result = []
            result.append([i.val for i in queue])
            if left_to_right == True and len(queue) > 1:
                e = queue[1]
            else:
                e = queue[0]
            if left_to_right == True:
                if e.left is not None:
                    mid_result.append(e.left)
                if e.right is not None:
                    mid_result.append(e.right)
                left_to_right = False
            elif left_to_right == False:
                if e.right is not None:
                    mid_result.append(e.right)
                if e.left is not None:
                    mid_result.append(e.left)
                left_to_right = True
            queue = mid_result
            
        return result
        '''
        if root is None:
            return []
        
        queue,result = [root],[]
        left_to_right = False
        while queue != []:
            length = len(queue)
            left_to_right = not left_to_right
            mid_result = []
            for i in range(length):
                if left_to_right:
                    node = queue.pop(0)
                else:
                    node = queue.pop(-1)
                mid_result.append(node.val)
                print(mid_result)
                
                if left_to_right:
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                else:
                    if node.right is not None:
                        queue.insert(0,node.right)
                    if node.left is not None:
                        queue.insert(0,node.left)
            
            result.append(mid_result)
            
        return result
        
        
            
