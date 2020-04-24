class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                twoSumTarget = target - nums[i] - nums[j]
                minTwoSum = nums[j + 1] + nums[j + 2]
                maxTwoSum = nums[n - 1] + nums[n - 2]
                if twoSumTarget < minTwoSum or twoSumTarget > maxTwoSum:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    twoSum = nums[left] + nums[right]
                    if twoSum < twoSumTarget:
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                    elif twoSum > twoSumTarget:
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    nums.sort()
    print(nums)