class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #       [2, 3, 4, 5]
        # left: [1, 2, 2*3, 2*3*4]
        # right:[3*4*5, 4*5, 5, 1]

        p = 1
        n = len(nums)
        left = []
        for i in range(n):
            left.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(n - 1, -1, -1):
            left[i] *= p
            p *= nums[i]

        return left

if __name__ == "__main__":
    l = Solution()
    print(l.productExceptSelf([1, 2, 3, 5]))