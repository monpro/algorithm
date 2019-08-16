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
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if (target - nums[-1]) * (nums[mid] - nums[-1]) > 0:
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            elif target > nums[-1]:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

if __name__ == "__main__":
    l = Solution()
    print(l.search([1,3],0))