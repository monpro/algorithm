class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = [0 for _ in range(n)]
        pre = [0 for _ in range(n)]
        nums.sort()
        maxVal, index = 0, -1
        result = []
        for i in range(n):
          count[i] = 1
          pre[i] = -1
          for j in range(i - 1, -1, -1):
            if nums[i] % nums[j] == 0:
              if count[i] < 1 + count[j]:
                count[i] = 1 + count[j]
                pre[i] = j
          if count[i] > maxVal:
            maxVal = count[i]
            index = i
        while index != -1:
          result.append(nums[index])
          index = pre[index]
        
        return result

            



if __name__ == "__main__":
    l = Solution()
    test = [2,1,3,5,4]
    test.sort()
    print(test)
