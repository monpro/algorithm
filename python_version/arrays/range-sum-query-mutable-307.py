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
        def createTree(nums, l, r):
          if l > r:
            return None
          
          if l == r:
            n = Node(l, r)
            n.total = nums[l]
            return n

          mid = (l + r) // 2
          root = Node(l, r)

          root.left = createTree(nums, l, mid)
          root.right = createTree(nums, mid + 1, r)

          root.toal = root.left.total + root.right.total

          return root
        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.result[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:
          return
        return sum(self.result[i: j + 1])
        
         
        