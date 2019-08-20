class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        result = []
        self.helper(root,sum,0,[],result)
        return result

    def helper(self,root,sum,temp,path,result):
        if not root:
            return
        if temp + root.val == sum and not root.left and not root.right:
            result.append(path)
        temp += root.val
        path.append(root.val)
        self.helper(root.left, sum, temp, [i for i in path],result)
        self.helper(root.right,sum, temp, [i for i in path],result)

        