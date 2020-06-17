class Node(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.total = 0
    self.left = None
    self.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.root = self.createTree(nums, 0, len(nums) - 1)
    def createTree(self, nums, l, r):
      if l > r:
        return None
      
      if l == r:
        n = Node(l, r)
        n.total = nums[l]
        return n

      root = Node(l, r)
      mid = (l + r) // 2

      root.left = self.createTree(nums, l, mid)
      root.right = self.createTree(nums, mid + 1, r)

      root.total = root.left.total + root.right.total

      return root
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        def updateVal(root, i, val):
          if root.start == root.end:
            root.total = val
            return val
          mid = (root.start + root.end) // 2

          if i <= mid:
            updateVal(root.left, i, val)
          else:
            updateVal(root.right, i, val)
          root.total = root.left.total + root.right.total

          return root
        
        return updateVal(self.root, i, val)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangeSum(root, i, j):
          if root.start == i and root.end == j:
            return root.total
          
          mid = (root.start + root.end) // 2

          if j <= mid:
            return rangeSum(root.left, i, j)
          elif i >= mid + 1:
            return rangeSum(root.right, i, j)
          else:
            return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)