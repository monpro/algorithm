class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag1 = False
        flag2 = True
        for i in range(len(nums) -1, -1, -1):

            if i > 0 and nums[i] > nums[i - 1]:
                if flag1:
                    break
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        flag2 = False
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        left = i
                        right =len(nums) - 1
                        flag1 = True
                        while left < right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1

                        print(nums)
                        break

        if flag2:
            nums.reverse()
        print(nums)
l = Solution()
l.nextPermutation([1,2,3])