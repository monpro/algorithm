class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = dict()
        for i in nums:
          if i not in hashmap:
            hashmap[i] = 1
          else:
            return True
        return False

if __name__ == "__main__":
    l = Solution()
    print(l.containsDuplicate([]))