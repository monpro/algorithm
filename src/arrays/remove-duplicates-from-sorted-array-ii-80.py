class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        index = 1
        cnt = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
                cnt = 1
            else:
                if cnt < 2:
                    nums[index] = nums[i]
                    index += 1
                    cnt += 1

        return index