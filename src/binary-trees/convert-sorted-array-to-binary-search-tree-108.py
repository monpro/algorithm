class Solution:
    def sortedArrayToBST(self, nums):
      if not nums:
        return None
      if len(nums) == 1:
        return TreeNode(nums[0])
      treeIndex = len(nums) // 2
      treeNode = TreeNode(nums[treeIndex])
      leftNums = nums[:treeIndex]
      rightNums = nums[treeIndex + 1:]
      treeNode.left = self.sortedArrayToBST(leftNums)
      treeNode.right = self.sortedArrayToBST(rightNums)
      return treeNode
        