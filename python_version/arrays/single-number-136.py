class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result




if __name__ == "__main__":
    l = Solution()
    print(l.singleNumber([1,2,3,3,2]))
        