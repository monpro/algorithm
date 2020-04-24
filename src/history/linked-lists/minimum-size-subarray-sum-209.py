class Solution:
    def minSubArrayLen(self, s, nums):
        sum_temp, left, result = 0, 0, float('Inf')
        for i in range(len(nums)):
            sum_temp += nums[i]
            while sum_temp >= s:
                result = min(result, i - left + 1)
                sum_temp -= nums[left]
                left += 1
        if result == float('Inf'):
            return 0
        else:
            return result 

if __name__ == "__main__":
    l = Solution()
    print(l.minSubArrayLen(7,[2,3,1,2,4,3]))