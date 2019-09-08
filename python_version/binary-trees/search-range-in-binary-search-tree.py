class Solution:
  """
  @param root: param root: The root of the binary search tree
  @param k1: An integer
  @param k2: An integer
  @return: return: Return all keys that k1<=key<=k2 in ascending order
  """

  def searchRange(self, root, k1, k2):
    if not root:
      return []

    if k1 <= root.val <= k2:
      return self.searchRange(root.left, k1, k2) + [root.val] + self.searchRange(root.right, k1, k2)
    elif root.val > k2:
      return self.searchRange(root.left, k1, k2)
    elif root.val < k1:
      return self.searchRange(root.right, k1, k2)

