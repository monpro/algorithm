class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[cur] = nums[i]
                cur += 1
        nums = nums[:cur]
        return cur

if __name__ == "__main__":
    l = Solution()
    print(l.removeElement([3,2,2,3], 2))