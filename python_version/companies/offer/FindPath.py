from .TreeNode import TreeNode



class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        result = []
        self.helper(root, expectNumber, result,[])
        return result

    def helper(self,root,expectNumber, result, path):
        if root is None:
            return
        if root.left is None and root.right is None and root.val == expectNumber:
            path.append(root.val)
            result.append(path)
            return
        path.append(root.val)
        self.helper(root.left, expectNumber - root.val, result, [i for i in path])
        self.helper(root.right, expectNumber - root.val, result, [i for i in path])

