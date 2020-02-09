import copy
class Solution:
    def sumNumbers(self, root):
      # an intuitive idea 
      # get all root-to-leaf path -> calculate -> sum together
      if not root:
        return 0
      result = 0
      paths = []
      self.helper(root, paths, "")
      for path in paths:
        result += int(path)
      return result

    def helper(self, root, paths, temp):
      if not root.left and not root.right:
        temp += root.val
        paths.append(copy.deepcopy(temp))
      
      temp += root
      self.helper(root.left, paths, temp)
      self.helper(root.right, paths, temp)