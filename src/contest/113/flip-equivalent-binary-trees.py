# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None or root2 is None:
            return root1 == root2
        
        return root1.val == root2.val and ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
                                          (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))
                                          
        
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None or root2 is None:
            return root1 == root2
        
        queue1 = [root1]
        queue2 = [root2]
        
        while queue1 and queue2:
            node1, node2 = queue1.pop(0), queue2.pop(0)
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None or node1.val != node2.val:
                return False
            
            if node1.left == node2.left == None or node1.left and node2.left and node1.left.val == node2.left.val:
                queue1.append(node1.left)
                queue1.append(node1.right)
            
            else:
                queue1.append(node1.right)
                queue1.append(node1.left)
            
            queue2.append(node2.left)
            queue2.append(node2.right)
            
            
        return len(queue1) == 0 and len(queue2) == 0