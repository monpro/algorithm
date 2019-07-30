from .TreeNode import TreeNode

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        stack = []
        stack.append(root)
        result = []
        while len(stack) > 0:
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                result.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return result
