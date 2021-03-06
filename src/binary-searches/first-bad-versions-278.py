# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def isBadVersion(self, index):
      return index
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
              right = mid
            else:
              left = mid + 1
        return left