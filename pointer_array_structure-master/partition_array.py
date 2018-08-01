class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        # write your code here
        if len(nums) <= 1:
            return nums

        odd, even = 0, len(nums) - 1
        while odd < even:
            while odd < even and nums[odd] % 2 == 1:
                odd += 1

            while even > odd and nums[even] % 2 == 0:
                even -= 1

            if odd < even:
                nums[odd], nums[even] = nums[even], nums[odd]
                odd += 1
                even -= 1

        return nums

    def sortLetters(self, chars):
        # write your code here
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        left, end = 0, len(chars) - 1

        while left < end:
            while left < end and chars[left] in lowercase:
                left += 1

            while left < end and chars[end] in uppercase:
                end -= 1

            if left < end:
                chars[left], chars[end] = chars[end], chars[left]

                left += 1

                end -= 1


