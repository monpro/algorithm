class Solution:
    def threeSum(self, nums):
        # find a + b = -c
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        result = []
        for index in range(len(nums) - 2 ):
            if index >= 1 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[index] < 0:
                    left += 1
                else:
                   result.append([nums[index],nums[left],nums[right]])
                   while left < right and nums[left] == nums[left + 1]:
                       left += 1
                   while left < right and nums[right] == nums[right - 1]:
                       right -= 1
                   left += 1
                   right -= 1
        return result


if __name__ == "__main__":
    l = Solution()
    print(l.threeSum([0,0,0,0]))
