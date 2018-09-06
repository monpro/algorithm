

class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                result = self.sameTree(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)


        return result

    def sameTree(self, root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.sameTree(root1.left,root2.left) and  self.sameTree(root1.right, root2.right)