class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here

        if len(nums) == []:
            return 0

        hash_set = set()
        left, right, total = 0, 0, 0
        while right < len(nums):
            while left < len(nums) and nums[left] not in hash_set:
                hash_set.add(nums[left])
                left += 1
                right += 1
                total += 1

            while right < len(nums) and nums[right] in hash_set:
                right += 1

            if left < right and right < len(nums):
                nums[left] = nums[right]
                hash_set.add(nums[left])
                left += 1
                right += 1
                total += 1

        return total