class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

if __name__ == "__main__":
    l = Solution()
    print(l.search([1,3],0))