class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        sum_amount = 0

        sum_dict = {0: -1}

        for i in range(len(nums)):
            sum_amount += nums[i]
            if sum_amount in sum_dict:
                return [sum_dict[sum_amount] + 1, i]

            sum_dict[sum_amount] = i

        return
