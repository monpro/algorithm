class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0 for i in range(len(nums) + 1)]
        
        for i in range(1, len(nums) + 1):
          self.dp[i] = self.dp[i - 1] + nums[i - 1]
        print(self.dp)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:
          return 0
        else:
          return self.dp[j + 1] - self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    # l = NumArray([-2, 0, 3, -5, 2, -1])
    # print(l.sumRange(0, 2))
    # print(l.sumRange(2, 5))
    # print(l.sumRange(0, 5))
    l = NumArray([-1])
    print(l.sumRange(0, 0))