class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = dict()
        for i in range(len(nums)):
          if nums[i] not in hashmap:
            hashmap[nums[i]] = i
          else:
            if i - hashmap[nums[i]] <= k:
              return True
            else:
              hashmap[nums[i]] = i
        return False
    def useSet(self,nums, k):
      result = set()
      for i in range(len(nums)):
        if i > k:
          result.remove(nums[i - k - 1])
        
        if nums[i] not in result:
          result.add(nums[i])
        elif nums[i] in result:
          return True
      return False


if __name__ == "__main__":
    l = Solution()
    print(l.useSet([1,2,3,1,2,3],2))