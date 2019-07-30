class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    '''
    def moveZeroes(self, nums):
        # write your code here
        digit = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[digit] = nums[i]
                digit += 1


        for i in range(digit, len(nums)):
            nums[i] = 0



        return nums
    '''

    def moveZeroes(self, nums):
        if len(nums) == 0:
            return nums
        zero_pointer = 0
        digit_pointer = 0
        while digit_pointer < len(nums):
            while nums[zero_pointer] != 0:
                zero_pointer += 1
                if zero_pointer == len(nums):
                    return nums

            digit_pointer = zero_pointer
            while nums[digit_pointer] == 0:
                digit_pointer += 1
                if digit_pointer == len(nums):
                    return nums

            nums[zero_pointer], nums[digit_pointer] = nums[digit_pointer], nums[zero_pointer]

        return nums