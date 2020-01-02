# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        queue_1 = []
        queue_2 = []
        result = []
        self.inorder(root1, queue_1)
        self.inorder(root2, queue_2)
        
        while len(queue_1) > 0 or len(queue_2) > 0:
            if len(queue_1) == 0:
                result.append(queue_2.pop(0))
            
            elif len(queue_2) == 0:
                result.append(queue_1.pop(0))
            else:
                if queue_1[0] > queue_2[0]:
                    result.append(queue_2.pop(0))
                else:
                    result.append(queue_1.pop(0))
        
        return result
    
    def inorder(self, root, queue):
        if not root:
            return
        self.inorder(root.left, queue)
        queue.append(root.val)
        self.inorder(root.right, queue)

    def getAllElementsUsingSorted(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root1)
        inorder(root2)
        
        return sorted(result)